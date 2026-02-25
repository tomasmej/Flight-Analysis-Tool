from pathlib import Path
import sqlite3
import json

def database_init(): 
  """ Creates database """ 
  try:
    conn = sqlite3.connect('profiles.db')
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            description TEXT NOT NULL,
            x_attributes TEXT,
            y_attributes TEXT
        )
                   
''')
    
    


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS record (
            recordId INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
                   
''')

            # profileId INTEGER,
            # FOREIGN KEY(profileId) REFERENCES profile(id)

    conn.commit()
    

    conn.close()
  except Exception as e:
        print("Database error: {e}")
        raise


def createDefaultProfile() -> bool:
  """ Create default, starting profile"""
  try:
      with sqlite3.connect('profiles.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT EXISTS (SELECT 1 FROM profile)") # 0 if profile list is empty, else 1
        check = cursor.fetchone()  
        if check[0] == 0:
           
            x_key = ["time_elapsed"]
            x_data = json.dumps(x_key)

            y_key = ["acceleration_y"]
            y_data = json.dumps(y_key)
           
            cursor.execute(
                "INSERT INTO profile (name, description, x_attributes, y_attributes) VALUES (?, ?, ?, ?)",
                (
                 str("Default"), 
                 str("Default profile created at app startup."),
                 x_data,
                 y_data,
                 )
            )

            conn.commit()
            print("Default profile created!")
           

  except Exception as e:
      print(f"Error creating default profile: {e}")
      raise  
         
         
def loadProfileNames():
    try:
        with sqlite3.connect('profiles.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM profile")
            return [row[0] for row in cursor.fetchall()]
    except Exception as e:
        print(f"Error fetching profile names: {e}")
        raise

def getProfileDescription(profileName):
    try:
       with sqlite3.connect('profiles.db') as conn:
          cursor = conn.cursor()
          cursor.execute("SELECT description FROM profile WHERE name = ?", (profileName,))
          row = cursor.fetchone()
          return row[0] if row else None
    except Exception as e:
        print(f"Error fetching profile description: {e}")
        raise
          


def createProfile(profileName, description):
    try:
       with sqlite3.connect('profiles.db') as conn:
        cursor = conn.cursor()

        x_key = ["time_elapsed"]
        x_data = json.dumps(x_key)

        y_key = ["acceleration_y"]
        y_data = json.dumps(y_key)

        cursor.execute(
                "INSERT INTO profile (name, description, x_attributes, y_attributes) VALUES (?, ?, ?, ?)",
                (
                   profileName, 
                   description,
                   x_data,
                   y_data,
                ),
            )
        conn.commit()
        print(f"Profile: {profileName} created!" )
    except Exception as e:
        print(f"Error creating profile: {e}")
        raise    

def deleteProfile(profileName):
   try:
       with sqlite3.connect('profiles.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
                "DELETE FROM profile WHERE name = ?" ,
                (profileName,)
            )
        conn.commit()
        print(f"Profile: {profileName} deleted!" )
   except Exception as e:
        print(f"Error deleting profile: {e}")
        raise    

def getProfileXAttributes(profileName):
   try:
       with sqlite3.connect('profiles.db') as conn:
          cursor = conn.cursor()
          cursor.execute("SELECT x_attributes FROM profile WHERE name = ?", (profileName,))
          row = cursor.fetchone()
          retrieved_list = json.loads(row[0])
        #   print(retrieved_list)
          if retrieved_list is not None:
            return retrieved_list
          else:
             return
   except Exception as e:
        print(f"Error fetching x attributes: {e}")
        raise
   
def getProfileYAttributes(profileName):
   try:
       with sqlite3.connect('profiles.db') as conn:
          cursor = conn.cursor()
          cursor.execute("SELECT y_attributes FROM profile WHERE name = ?", (profileName,))
          row = cursor.fetchone()
          retrieved_list = json.loads(row[0])
        #   print(retrieved_list)
          if retrieved_list is not None:
            return retrieved_list
          else:
             return
   except Exception as e:
        print(f"Error fetching y attributes: {e}")
        raise
   

def addXAttribute(profileName, newAttribute):
   try:
       with sqlite3.connect('profiles.db') as conn:
          #Fetch attributes 
          cursor = conn.cursor()
          cursor.execute("SELECT x_attributes FROM profile WHERE name = ?", (profileName,))
          row = cursor.fetchone()
          retrieved_list = json.loads(row[0])
          
          # Add or delete attribute  
          if retrieved_list is not None:
            if newAttribute not in retrieved_list:
                retrieved_list.append(newAttribute)
          else:
             return
          
          # Update attribute list
          cursor.execute(
                "UPDATE profile SET x_attributes = ? WHERE name = ?",
                (
                   json.dumps(retrieved_list), 
                   profileName
                )
            )

          conn.commit()
   except Exception as e:
        print(f"Error fetching x attributes: {e}")
        raise
   
def deleteXAttribute(profileName, selectedAttribute):
    try:
       with sqlite3.connect('profiles.db') as conn:
          #Fetch attributes 
          cursor = conn.cursor()
          cursor.execute("SELECT x_attributes FROM profile WHERE name = ?", (profileName,))
          row = cursor.fetchone()
          retrieved_list = json.loads(row[0])
          
          # Add or delete attribute  
          if retrieved_list is not None:
                retrieved_list.remove(selectedAttribute)
          
          # Update attribute list
          cursor.execute(
                "UPDATE profile SET x_attributes = ? WHERE name = ?",
                (
                   json.dumps(retrieved_list), 
                   profileName
                )
            )

          conn.commit()
    except Exception as e:
        print(f"Error fetching x attributes: {e}")
        raise

def addYAttribute(profileName, newAttribute):
   try:
       with sqlite3.connect('profiles.db') as conn:
          #Fetch attributes 
          cursor = conn.cursor()
          cursor.execute("SELECT y_attributes FROM profile WHERE name = ?", (profileName,))
          row = cursor.fetchone()
          retrieved_list = json.loads(row[0])
          
          # Add or delete attribute  
          if retrieved_list is not None:
            if newAttribute not in retrieved_list:
                retrieved_list.append(newAttribute)
          else:
             return
          
          # Update attribute list
          cursor.execute(
                "UPDATE profile SET y_attributes = ? WHERE name = ?",
                (
                   json.dumps(retrieved_list), 
                   profileName
                )
            )

          conn.commit()
   except Exception as e:
        print(f"Error fetching y attributes: {e}")
        raise
   
def deleteYAttribute(profileName, selectedAttribute):
    try:
       with sqlite3.connect('profiles.db') as conn:
          #Fetch attributes 
          cursor = conn.cursor()
          cursor.execute("SELECT y_attributes FROM profile WHERE name = ?", (profileName,))
          row = cursor.fetchone()
          retrieved_list = json.loads(row[0])
          
          # Add or delete attribute  
          if retrieved_list is not None:
                retrieved_list.remove(selectedAttribute)
          
          # Update attribute list
          cursor.execute(
                "UPDATE profile SET y_attributes = ? WHERE name = ?",
                (
                   json.dumps(retrieved_list), 
                   profileName
                )
            )

          conn.commit()
    except Exception as e:
        print(f"Error fetching y attributes: {e}")
        raise

