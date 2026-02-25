
from pathlib import Path


# returns path orion/
def root_path() -> Path:
    path = Path(__file__).parent.parent.parent
    # print(path)
    return path

# return data folder path orion/data
def data_path() -> Path:
      return root_path() / 'data'

# Checks if data folder is empty, false otherwise
def checkIfDiskEmpty(path):
        return not any(Path(path).iterdir())

