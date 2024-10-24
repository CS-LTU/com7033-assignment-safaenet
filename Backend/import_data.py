import sqlite3
import pandas as pd

conn = sqlite3.connect('instance/database.db')
cursor = conn.cursor()

df = pd.read_csv('Backend/healthcare-dataset-stroke-data2.csv')

df.to_sql('patient_model', conn, if_exists='append', index=False)

conn.commit()
conn.close()