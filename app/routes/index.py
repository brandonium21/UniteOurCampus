from app import app
from flask import redirect, render_template, render_template_string, request, url_for, json
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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


@app.route('/sendTheemailToTheMasses', methods=['GET', 'POST'])
def send():
    #Authenticate and create google sheet Obj -------

    json_key = json.load(open('rally-126a3be978da.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope)
    gc = gspread.authorize(credentials)
    wks = gc.open("testy").sheet1
    # -----------------------------------------------

    val = wks.acell('C2').value
    listEmails = []
    counter = 1
    while val:
        counter += 1
        cell = str('C' + str(counter))
        val = wks.acell(cell).value
        listEmails.append(val)
        pass
    #print listEmails
    if request.method == 'POST':
        for person in listEmails:
            gmail_user = 'brandonium21'
            gmail_pwd = 'dragon49'
            smtpserver = smtplib.SMTP("smtp.gmail.com",587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo
            smtpserver.login(gmail_user, gmail_pwd)
            header ='Subject:testing \n'
            msg = header + '\n this is test msg from mkyong.com \n\n'
            msg = MIMEMultipart('alternative')
            msg['To'] = person
            msg['From'] = gmail_user
            msg['Subject'] = 'Unite Our Campus'

            text = ' Unite Our campus please share our event with this link. http://www.uniteourcampus.com/shareEmailFacebook'
            html = '''
                <!DOCTYPE html>
            <html style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">
            <head>
            <meta name="viewport" content="width=device-width">
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
            <title>Really Simple HTML Email Template</title>
            </head>
            <body bgcolor="#f6f6f6" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; -webkit-font-smoothing: antialiased; height: 100%; -webkit-text-size-adjust: none; width: 100% !important; margin: 0; padding: 0;">

            <!-- body -->
            <table class="body-wrap" bgcolor="#f6f6f6" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; width: 100%; margin: 0; padding: 20px;"><tr style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">
            <td style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;"></td>
                <td class="container" bgcolor="#FFFFFF" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; clear: both !important; display: block !important; max-width: 600px !important; Margin: 0 auto; padding: 20px; border: 1px solid #f0f0f0;">

                  <!-- content -->
                  <div class="content" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; display: block; max-width: 600px; margin: 0 auto; padding: 0;">
                  <table style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; width: 100%; margin: 0; padding: 0;"><tr style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">
            <td style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">
                        <!--<p style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6em; font-weight: normal; margin: 0 0 10px; padding: 0;">Hi there,</p>
                        <p style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6em; font-weight: normal; margin: 0 0 10px; padding: 0;">Sometimes all you want is to send a simple HTML email with a basic design.</p>-->
                        <h1 style="font-family: 'Helvetica Neue', Helvetica, Arial, 'Lucida Grande', sans-serif; font-size: 36px; line-height: 1.2em; color: #111111; font-weight: 200; margin: 40px 0 10px; padding: 0;">Unite Our Campus</h1> 
                        <p style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6em; font-weight: normal; margin: 0 0 10px; padding: 0;">Thank you for registering for our event. but in hopes to get more people to sign up we would like for you to share the event on Facebook and by talking with friends. We really believe that starting a conversation about unfair media representaion will turn the tides of history.</p>
                        <h2 style="font-family: 'Helvetica Neue', Helvetica, Arial, 'Lucida Grande', sans-serif; font-size: 28px; line-height: 1.2em; color: #111111; font-weight: 200; margin: 40px 0 10px; padding: 0;">Press the button below to share on Facebook</h2>
                        <p style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6em; font-weight: normal; margin: 0 0 10px; padding: 0;">We have over 40,000 students on campus, and with your help we can reach them.</p>
                        <!-- button -->
                        <table class="btn-primary" cellpadding="0" cellspacing="0" border="0" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; width: auto !important; Margin: 0 0 10px; padding: 0;"><tr style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">
            <td style="font-family: 'Helvetica Neue', Helvetica, Arial, 'Lucida Grande', sans-serif; font-size: 14px; line-height: 1.6em; border-radius: 25px; text-align: center; vertical-align: top; background: #348eda; margin: 0; padding: 0;" align="center" bgcolor="#348eda" valign="top">
                              <a href="http://www.uniteourcampus.com/shareEmailFacebook" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 2; color: #ffffff; border-radius: 25px; display: inline-block; cursor: pointer; font-weight: bold; text-decoration: none; background: #348eda; margin: 0; padding: 0; border-color: #348eda; border-style: solid; border-width: 10px 20px;">Share</a>
                            </td>
                          </tr></table>
            <!-- /button --><p style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6em; font-weight: normal; margin: 0 0 10px; padding: 0;">Feel free forward any question or concerns to our facebook page.</p>
                        <p style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6em; font-weight: normal; margin: 0 0 10px; padding: 0;">Thanks, have a lovely day.</p>
                        <p style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 1.6em; font-weight: normal; margin: 0 0 10px; padding: 0;"><a href="http://www.facebook.com/UniteOurCampusUIUC" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; color: #348eda; margin: 0; padding: 0;">Link to Facebook page</a></p>
                      </td>
                    </tr></table>
            </div>
                  <!-- /content -->
                  
                </td>
                <td style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;"></td>
              </tr></table>
            <!-- /body --><!-- footer --><table class="footer-wrap" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; clear: both !important; width: 100%; margin: 0; padding: 0;"><tr style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">
            <td style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;"></td>
                <td class="container" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; clear: both !important; display: block !important; max-width: 600px !important; margin: 0 auto; padding: 0;">
                  
                  <!-- content -->
                  <div class="content" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; display: block; max-width: 600px; margin: 0 auto; padding: 0;">
                    <table style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; width: 100%; margin: 0; padding: 0;"><tr style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">
            <td align="center" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">
                          <p style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 12px; line-height: 1.6em; color: #666666; font-weight: normal; margin: 0 0 10px; padding: 0;">Don't like these annoying emails? <a href="#" style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; color: #999999; margin: 0; padding: 0;"><unsubscribe style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;">Unsubscribe</unsubscribe></a>.
                          </p>
                        </td>
                      </tr></table>
            </div>
                  <!-- /content -->
                  
                </td>
                <td style="font-family: 'Helvetica Neue', 'Helvetica', Helvetica, Arial, sans-serif; font-size: 100%; line-height: 1.6em; margin: 0; padding: 0;"></td>
              </tr></table>
            <!-- /footer -->
            </body>
            </html>
            '''
            part1 = MIMEText(text, 'plain')
            part2 = MIMEText(html, 'html')
            msg.attach(part1)
            msg.attach(part2)
            smtpserver.sendmail(gmail_user, person, msg.as_string())
            smtpserver.close()

    return render_template("emailItOut.html", emails=listEmails)
