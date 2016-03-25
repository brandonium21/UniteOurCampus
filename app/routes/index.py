from app import app
from flask import redirect, render_template, render_template_string, request, url_for, json
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        print name
        print email

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
            while val :
                counter +=1
                cell = str( 'A' + str(counter))
                val = wks.acell(cell).value
                print counter
                pass
            return counter
        # -----------------------------------------------

        # Add person to google sheet --------------------

        cellNumber = cellIterate()
        wks.update_acell('A' + str(cellNumber), name)
        wks.update_acell('B' + str(cellNumber), email)
        # -----------------------------------------------


    return render_template('register.html')
