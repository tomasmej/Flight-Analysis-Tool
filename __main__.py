import subprocess
import sys 
from pathlib import Path

if __name__ == "__main__":
  subprocess.run([sys.executable, "-m", "orion"], cwd = str(Path(__file__).parent))
