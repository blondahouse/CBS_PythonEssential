# loading in modules
import sqlite3
from datetime import datetime, timezone

# Constants
# LOCATION_QUERY = """
# SELECT ModelPath
# FROM 'ModelStorageTable'
# """
# temporary query while WIP
LOCATION_QUERY = """
SELECT ModelPath
FROM 'ModelStorageTable'
WHERE ModelPath
LIKE '%MZ1-C02-00B%'
"""
MAX_DATE_QUERY = """
SELECT MAX(Time)
FROM 'ModelHistory'
"""
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%SZ'
SOURCE = 'C:\\ProgramData\\Autodesk\\Revit Server 2023\\Projects\\'
TARGET = 'T:\\Revit Server 2023\\'
MODEL = '\\Data\\Model.db3'

# connect to ModelLocationTable and request to get all available models
location_file = 'C:\\ProgramData\\Autodesk\\Revit Server 2023\\Projects\\ModelLocationTable.db3'
location_connection = sqlite3.connect(location_file)
location_cursor = location_connection.cursor()
location_paths = [a[0] for a in location_cursor.execute(LOCATION_QUERY)]
# Be sure to close the connection
location_connection.close()

# Concatenate paths with additions
model_paths = list(map(lambda a: SOURCE + a + MODEL, location_paths))

# Get date difference between now and last edit date in days
models_to_backup = []
for model_path in model_paths:
    # connect and request
    model_connection = sqlite3.connect(model_path)
    model_cursor = sqlite3.connect(model_path).cursor()
    model_date = model_cursor.execute(MAX_DATE_QUERY).fetchone()[0]
    # Be sure to close the connection
    model_connection.close()
    # datetime conversion and difference
    model_date_tz = datetime.strptime(model_date, DATETIME_FORMAT).astimezone(timezone.utc).replace(tzinfo=None)
    model_delta = datetime.now() - model_date_tz
    print(model_delta.days)
    if not model_delta.days:
        source_path = model_path.replace(MODEL, '')
        target_path = source_path.replace(SOURCE, TARGET)
        models_to_backup.append((source_path, target_path))

print(models_to_backup)
