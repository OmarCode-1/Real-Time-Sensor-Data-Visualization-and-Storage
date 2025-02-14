import sqlite3 as db
import json 
import numpy as np

# connect to dataBase :
my_database = db.connect("DataAnalysis.db")

# set Cursor .
cr = my_database.cursor()

#  create records table if it not exists .
cr.execute("CREATE TABLE IF NOT EXISTS record(id INTEGER PRIMARY KEY AUTOINCREMENT, name, start_time, end_time, date, duration, len_records, port_name, baud_rate, records, _values, time, sub_time, dates)")

def saveDataBase():
    """
        this function to commit the data base .
    """
    my_database.commit()

def closeDataBase():
    """ 
        this function to close the data base .
    """
    my_database.close()


def addRecordInDataBase(name : str, start_time : str, end_time : str, date : str, duration : str, len_records : int, port_name : str, baud_rate : str, records : list, _values : list, time: list, sub_times : list, dates : list) -> None:
    """
        this function to store the record in database .
    """
    #  convert lists to store in data base as a list :
    dates = json.dumps(dates)
    _values = json.dumps(_values)
    time = json.dumps(time)
    sub_times = json.dumps(sub_times)

    # Store it . 
    cr.execute(f"INSERT INTO record(name, start_time, end_time, date, duration, len_records, port_name, baud_rate, records, _values, time, sub_time, dates) Values('{name}', '{start_time}', '{end_time}', '{date}', '{duration}', '{len_records}', '{port_name}', '{baud_rate}', '{records}', '{_values}', '{time}', '{sub_times}', '{dates}')")
    
    #! you should save the database after add record.
    saveDataBase()

def getInformationAboutRecord(name : str) -> list:
    """
        this function will return the information about the id .
    """
    record = list(cr.execute(f"SELECT * FROM record where name LIKE '%{name}%'").fetchone())
    for i in range(9, 14):
        record[i] = json.loads(record[i])
    return record

def allRecords() -> np.array:
    """
        this function to return the all records in data base.
    """
    return np.array(cr.execute("SELECT * from record").fetchall())

def delRecord(name : str) -> None:
    """
        this function will remove the record .
    """
    cr.execute(f"DELETE from record where name = '{name}'")
    #! you should save the database after add record.
    saveDataBase()

