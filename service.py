import gspread

## Authorizing Service Account bot access to Google Sheets. ##

client = gspread.service_account()
spreadsheet = client.open('JBP YouTube Data 7/16/22')

#for num in range(2, 32):
#    print(spreadsheet.Newest.get('B' +  str(num)))
