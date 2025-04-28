from flask import Flask, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

# Flask app
app = Flask(__name__)

# Setup Google Sheets connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet by name
sheet = client.open("Study Hours Tracker").sheet1

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    from_number = request.form.get('From')
    body = request.form.get('Body')
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Add new row to Sheet
    sheet.append_row([now, from_number, body])
    
    print(f"Saved: {now} | {from_number} | {body}")
    return "OK", 200

if __name__ == "__main__":
    app.run(port=5000)
