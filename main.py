import json
import sqlite3
import openpyxl

# Create a database based on json
def db_from_json(json_input, db_file_path):
  conn = sqlite3.connect(db_file_path)
  cur = conn.cursor()
  cur.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT, json_data TEXT)''')
  cur.execute('''INSERT INTO data (json_data) VALUES (?)''', (json_input,))
  conn.commit()
  conn.close()

# Exports the data into a spreadsheet
def db_to_spreadsheet(db_file_path, spreadsheet_file_path):
  conn = sqlite3.connect(db_file_path)
  cur = conn.cursor()
  cur.execute('''SELECT json_date FROM data''')
  wb = openpyxl.Workbook()
  ws = wb['Sheet 1']

  # Iterate over the rows in the database and write them to the spreadsheet.
  for row in cur.fetchall():
    ws.append(row)
  wb.save(spreadsheet_file_path)
  conn.close()

def main():
  # Take json as input
  json_input = input('Enter data as json: ')

  # Create a database based on json
  try:
    db_from_json(json_input, 'database.db')
    print('Database Created!')
  except:
    print('Something went wrong in creating database')
  
  # Export data into a spreadsheet
  try:
    db_to_spreadsheet('database.db', 'spreadsheet.xlsx')
    print('Data exported into Spreadsheet!')
  except:
    print('Something went wrong while exporting data into a spreadsheeet')

if __name__ == '__main__':
  main()