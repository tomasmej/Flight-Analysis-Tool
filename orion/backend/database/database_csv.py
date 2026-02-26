from pathlib import Path
import sqlite3
import json
import os
from ..utils.paths import *


def createNewRecord(csvname):
  try:
        with sqlite3.connect('profiles.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO record (name) VALUES (?)",
                (csvname,)   
            )

            conn.commit()
        
  except Exception as e:
      print(f"Error creating csv record: {e}")
      raise  
  

  
def deleteRecord(csvname):
    try:
        with sqlite3.connect('profiles.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM record WHERE name = ?" ,
                (csvname,)
            )

            conn.commit()
        
    except Exception as e:
      print(f"Error deleting rcord with csvname: {e}")
      raise  
  
def loadCsvNames():
    try:
        with sqlite3.connect('profiles.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM record")
            return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error fetching csv names: {e}")
        raise

def repopulateRecords(csvlist):
    try:
        with sqlite3.connect('profiles.db') as conn:
            cursor = conn.cursor()
            for path in csvlist:
                cursor.execute(
                    "INSERT INTO record (name) VALUES (?)",
                    (path.name,)   
                )

            conn.commit()
    except Exception as e:
        print(f"Error repopulating csvs: {e}")
        raise        

def checkEmpty():
    try:
        with sqlite3.connect('profiles.db') as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT 1 FROM record LIMIT 1")
            row = cursor.fetchone()
            
            return row is None  # Returns True if no row is found
    except Exception as e:
        print(f"Error checking if empty: {e}")
        raise    


# Check every csv in disk , ex. a.csv b.csv and c.csv
# Disk to database checks for csv files deleted from disk and removes those records,
# and adds records for new csvs added
# if database was deleted, add back all disk csvs into the new database

# database = {"csv.a", "csv.b", "csv.c"}
# disk = {"csv.b", "csv.c", "csv.d"}

# to_delete = database.difference(disk) -> csv.a
# to_add = database.difference(disk) -> csv.d

def verifyDatabaseToDisk(db_path, csvList):
    if checkEmpty() and not checkIfDiskEmpty(db_path):
       repopulateRecords(csvList)
       return 
   

    try:
        disk_set = set()
        for path in data_path().iterdir():
            disk_set.add(path.name)

        db_set = set()
        for csv_name in loadCsvNames():
            db_set.add(csv_name)

        to_delete = db_set.difference(disk_set) 
        to_add = disk_set.difference(db_set) 
    
        if to_delete:
            for name in to_delete:
                deleteRecord(name)

        if to_add:
            for name in to_add:
                createNewRecord(name)
    except Exception as e:
        print(f"Error validating database to disk: {e}")
        raise    

    


