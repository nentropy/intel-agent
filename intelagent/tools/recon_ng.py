import subprocess

def run_recon_ng_script(script_path, workspace='default'):
    command = f"recon-ng -w {workspace} -r {script_path}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Example usage
script_path = '/path/to/your/reconng_script.rc'
recon_ng_result = run_recon_ng_script(script_path)
print(recon_ng_result)