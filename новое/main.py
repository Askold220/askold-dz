import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, timedelta

credentials = ServiceAccountCredentials.from_json_keyfile_name('secrets.json', ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'])
client = gspread.authorize(credentials)

spreadsheet = client.create('Your Spreadsheet Name')
worksheet = spreadsheet.get_worksheet(0)
dates = [datetime.now() + timedelta(days=i) for i in range(4)]
date_column = worksheet.col_values(1)
for date in dates:
    date_column.append(date.strftime('%Y-%m-%d'))
worksheet.update('A:A', [[date] for date in date_column])

print("Дати були успішно записані в Google Sheets.")
