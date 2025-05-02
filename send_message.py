import os
import time
from dotenv import load_dotenv
import schedule
from twilio.rest import Client

print("✅ Script started at", time.strftime('%Y-%m-%d %H:%M:%S'))

# ✅ Load environment variables from .env or Render env vars
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_whatsapp_number = 'whatsapp:+14155238886'  # Twilio Sandbox Number

print("SID:", account_sid)
print("Token starts:", auth_token[:5], "...")

# ✅ Create Twilio client
try:
    client = Client(account_sid, auth_token)
    print("✅ Twilio client initialized")
except Exception as e:
    print("❌ Failed to initialize Twilio client:", e)

# ✅ Your sandbox-verified student numbers
student_numbers = [
    'whatsapp:+919823036706',
    'whatsapp:+919823046706',
    # Add more only if they've joined the sandbox
]

# ✅ Send daily message
def send_study_message_to_all():
    print(f"⏰ Sending daily message at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    for number in student_numbers:
        try:
            client.messages.create(
                body="🌟 Hi! How many hours did you study today? Please reply honestly. 📚",
                from_=twilio_whatsapp_number,
                to=number
            )
            print(f"✅ Sent to {number}")
        except Exception as e:
            print(f"❌ Error for {number}: {e}")
        time.sleep(1)

# ✅ Schedule: 10:00 PM IST = 16:30 UTC
schedule.every().day.at("11:22").do(send_study_message_to_all)

# Optional heartbeat to prove the script is alive
schedule.every(1).hours.do(lambda: print(f"💓 Still running: {time.strftime('%H:%M:%S')}"))

print("🚀 Bot is running and waiting for schedule...")

while True:
    schedule.run_pending()
    time.sleep(10)

