import subprocess
from pathlib import Path

# Delete all the old figures first
for file in Path('./figures').iterdir():
    file.unlink()

# Define the notebooks directory relative to this script's location
notebooks_dir = Path('./notebooks')

# Function to run notebooks
def run_notebook(notebook_path):
    result = subprocess.run([
        "jupyter", "nbconvert", 
        "--to", "notebook", 
        "--execute",
        "--inplace",
        "--ExecutePreprocessor.timeout=600",
        str(notebook_path)
    ], capture_output=True, text=True)
    return result

# Iterate over each notebook in the directory and run it
for notebook_file in notebooks_dir.glob('*.ipynb'):
    print(f"Running {notebook_file}...")
    result = run_notebook(notebook_file)
    if result.returncode == 0:
        print(f"Finished running {notebook_file}.\n")
    else:
        print(f"Error running {notebook_file}: {result.stderr}\n")
