import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

name = 'Candde'
email = 'candee@gmail.com'

json_key = json.load(open('rally-126a3be978da.json'))
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)

gc = gspread.authorize(credentials)

wks = gc.open("testy").sheet1


def cellIterate():
    val = wks.acell('A1').value
    counter = 1
    while val :
        counter +=1
        cell = str( 'A' + str(counter))
        val = wks.acell(cell).value
        print counter
        pass
    return counter

def addPerson():
    cellNumber = cellIterate()
    wks.update_acell('A' + str(cellNumber), name)
    wks.update_acell('B' + str(cellNumber), email)

addPerson()
