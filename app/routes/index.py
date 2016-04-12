from app import app
from flask import redirect, render_template, render_template_string, request, url_for, json
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        Fname = request.form['first']
        Lname = request.form['last']
        email = request.form['email']
        netId = request.form['netId']
        heard = request.form['heard']
        dietary = request.form['dietary']
        hearmore = request.form['hearmore']

        #Authenticate and create google sheet Obj -------

        json_key = json.load(open('rally-126a3be978da.json'))
        scope = ['https://spreadsheets.google.com/feeds']
        credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
        gc = gspread.authorize(credentials)
        wks = gc.open("testy").sheet1
        # -----------------------------------------------

        # Iterate through sheet find next empty cell-----
        def cellIterate():
            val = wks.acell('A1').value
            counter = 1
            while val:
                counter += 1
                cell = str('A' + str(counter))
                val = wks.acell(cell).value
                print counter
                pass
            return counter
        # -----------------------------------------------

        # Add person to google sheet --------------------

        cellNumber = cellIterate()
        wks.update_acell('A' + str(cellNumber), Fname)
        wks.update_acell('B' + str(cellNumber), Lname)
        wks.update_acell('C' + str(cellNumber), email)
        wks.update_acell('D' + str(cellNumber), netId)
        wks.update_acell('E' + str(cellNumber), heard)
        wks.update_acell('F' + str(cellNumber), dietary)
        wks.update_acell('G' + str(cellNumber), hearmore)
        #wks.update_acell('F' + str(cellNumber), ethnicity)
        # -----------------------------------------------
    return app.send_static_file('index.html')


@app.route('/shareEmailFacebook', methods=['GET', 'POST'])
def emailFb():
    return app.send_static_file('emailfb.html')