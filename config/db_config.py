import datetime
import os
import random
import shutil
import sqlite3
from datetime import timedelta

import pandas as pd
import requests

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds()))
    )


db_url = "https://github.com/lerocha/chinook-database/blob/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"
local_file = "../Chinook_Sqlite.sqlite"
# The backup lets us restart for each tutorial section
backup_file = "Chinook_Sqlite.backup.sqlite"
overwrite = False
if overwrite or not os.path.exists(local_file):
    response = requests.get(db_url)
    response.raise_for_status()  # Ensure the request was successful
    with open(local_file, "wb") as f:
        f.write(response.content)
    # Backup - we will use this to "reset" our DB in each section
    shutil.copy(local_file, backup_file)
# Convert the invoices to present time for our tutorial
conn = sqlite3.connect(local_file)
cursor = conn.cursor()

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';", conn
).name.tolist()

tdf = {}
for t in tables:
    tdf[t] = pd.read_sql(f"SELECT * from {t}", conn)

datetime_columns = [
    "InvoiceDate"
]
now = datetime.now()
six_months_ago = now - timedelta(days=180)

for column in datetime_columns:
    tdf["Invoice"][column] = (pd.to_datetime(random_date(now, six_months_ago)))

for table_name, df in tdf.items():
    df.to_sql(table_name, conn, if_exists="replace", index=False)
del df
del tdf
conn.commit()
conn.close()

db = local_file  # We'll be using this local file as our DB in this tutorial