import subprocess
import sys
import os
import yaml
import time
from ..utils import load_config

#Langchain Tool Creation
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool, StructuredTool, tool

# Run Nmap scan
@tool
def run_nmap_scan(config="./config.yaml", target_range,):
    """Run an NMAP scan based on the config file"""
    RANGE=True
    nmap_config = config['tools']['nmap']
    constants = config['CONSTANTS']

    # Determine target based on local_only setting
    if constants.get('local_only', False):
        target = constants.get('local_ip', '127.0.0.1')
    else:
        target = constants.get('host_ip', '192.168.1.1')

    # Prepare the Nmap command
    nmap_command = [nmap_config['path']] + nmap_config['options'] + ['-p-', target]  # Scan all ports

    # Set the output file
    output_file = nmap_config.get('output_file', 'nmap_results.xml')
    nmap_command.append(f"-oX {output_file}")

    # Run the Nmap command with retry logic
    for attempt in range(constants.get('retry_times', 3)):
        try:
            result = subprocess.run(nmap_command, capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
            if result.returncode == 0:
                break
        except Exception as e:
            print(f"Error running Nmap: {e}")
            time.sleep(constants.get('delay', 2.0))
        else:
            if attempt == constants.get('retry_times', 3) - 1:
                print("Nmap scan failed after several attempts.")
                sys.exit(1)

if __name__ == "__main__":
    config = load_config()
    run_nmap_scan(config)
