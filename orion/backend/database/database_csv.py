from pathlib import Path
import sqlite3
import json

def createNewRecord(csvname):
  try:
        with sqlite3.connect('profiles.db') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO record (name) VALUES (?)",
                (csvname,)   # ← comma is EVERYTHING
            )
        
  except Exception as e:
      print(f"Error creating default profile: {e}")
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