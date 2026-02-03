from PySide6.QtWidgets import QFileDialog, QMessageBox
import pandas as pd
from pathlib import Path
import shutil

class TrackerEngine:
    
    def __init__(self):
        self.reset()

    def reset(self):
        
        self.csvList = self.getStoredCsvs()
        self.df = None

    def addCsv(self, file_path):

        source = Path(file_path)

        data_dir = Path(__file__).resolve().parent.parent / "data"
        data_dir.mkdir(exist_ok=True)

        destination = data_dir / source.name
        shutil.copy(source, destination)

        return file_path
    
    def getStoredCsvs(self):
        data_dir = Path(__file__).resolve().parent.parent / "data"
        return [f.absolute() for f in data_dir.rglob('*') if f.is_file()]
            


    def extract(self, path):
        try:
            self.df = pd.read_csv(path)
        except Exception as e:
            print(f"Failed to read CSV: {e}")
            return None, None
        
        time_col = "time_elapsed"
        value_col = "acceleration_y"

        # __ over ___ function
        if time_col not in self.df.columns or value_col not in self.df.columns:
            print(f"Required columns not found: need '{time_col}' and '{value_col}'")
            return
        
        return self.df[time_col], self.df[value_col]