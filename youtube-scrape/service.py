import gspread

## Verifying Service Account bot access to Google Sheets. ##

client = gspread.service_account()
spreadsheet = client.open('JBP YouTube Data | 7/16/22 7:32PM')

#for num in range(2, 32):
#    print(spreadsheet.Newest.get('B' +  str(num)))
