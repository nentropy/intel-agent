import subprocess
import sys

def build_docs():
    try:
        result = subprocess.run(['sphinx-build', '-b', 'html', 'docs/source', 'docs/build/html'], check=True)
        print(result.stdout)
        print(result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    build_docs()
