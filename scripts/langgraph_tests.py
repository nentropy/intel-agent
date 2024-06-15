import subprocess
import sys
import os

SUBMODULE_PATH = './langgraph'  # Update with your submodule path

if os.path.isdir(SUBMODULE_PATH):
    result = subprocess.run([sys.executable, '-m', 'pytest', SUBMODULE_PATH])
    sys.exit(result.returncode)
else:
    print(f"Submodule path '{SUBMODULE_PATH}' does not exist.")
    sys.exit(1)
