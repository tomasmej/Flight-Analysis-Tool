from pathlib import Path
import sqlite3
import json
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

def verifyDatabaseToDisk(db_path, csvList):
   if checkEmpty() and not checkIfDiskEmpty(db_path):
       repopulateRecords(csvList)
       return True
   return False