from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import os
import json
import base64

app = Flask(__name__)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Load credentials from BASE64 encoded environment variable
credentials_b64 = os.environ['GOOGLE_CREDENTIALS_B64']
credentials_json = base64.b64decode(credentials_b64).decode('utf-8')
credentials_info = json.loads(credentials_json)

creds = ServiceAccountCredentials.from_json_keyfile_dict(credentials_info, scope)
client = gspread.authorize(creds)

sheet = client.open("Study Hours Tracker").sheet1

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    from_number = request.form.get('From')
    body = request.form.get('Body')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    sheet.append_row([now, from_number, body])
    print(f"Saved: {now} | {from_number} | {body}")
    
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
