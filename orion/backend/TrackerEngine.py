from PySide6.QtWidgets import QFileDialog, QMessageBox
import pandas as pd
from pathlib import Path
import shutil
from .database.database_csv import createNewRecord, loadCsvNames, deleteRecord

class TrackerEngine:
    
    def __init__(self):
        self.reset()

    def reset(self):
        
        self.csvList = self.getStoredCsvs() # must be absolute paths
        self.df = None

    def addCsv(self, file_path):

        # add selected file path.name to local storage
        data_dir = Path(__file__).resolve().parent.parent / "data"
        data_dir.mkdir(exist_ok=True)
        destination = data_dir / file_path.name
        shutil.copy(file_path, destination)

        # add csv name to database 
        createNewRecord(file_path.name)

   
    def deleteCsv(self, file_name):

        # delete from local storage
        path_to_delete = Path(__file__).resolve().parent.parent / "data" / file_name
        path_to_delete.unlink()
        print(f"File {file_name} deleted from local storage")

        # delete from engine
        for path in self.csvList:
            if path.name == file_name:
                self.csvList.remove(path)

        # delete from database
        deleteRecord(file_name)




    
    def getStoredCsvs(self):
        data_dir = Path(__file__).resolve().parent.parent / "data"
        return [f.absolute() for f in data_dir.rglob('*') if f.is_file()]
    
    def getDatabaseStoredCsvs(self):
        for i in loadCsvNames():
            print(i)
            

    def getStoredPath(self, path_name) -> Path:
        for i in self.csvList:
            if i.name == path_name:
                return i
        return None
    
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
    

    def activate(self):
        print("Tracker active")
