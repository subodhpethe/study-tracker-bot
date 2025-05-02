import os
import time
print("✅ Script started at", time.strftime('%Y-%m-%d %H:%M:%S'))
import schedule
from twilio.rest import Client

# ✅ Load credentials correctly from environment variables
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_whatsapp_number = 'whatsapp:+14155238886'

# Create Twilio client
try:
    client = Client(account_sid, auth_token)
    print("✅ Twilio client initialized")
except Exception as e:
    print("❌ Error initializing client:", e)

# Student numbers
student_numbers = [
    'whatsapp:+919823036706',
    'whatsapp:+919823046706',
]

# Function to send messages
def send_study_message_to_all():
    print(f"⏰ Triggered at {time.strftime('%Y-%m-%d %H:%M:%S')}")
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

# TEMP: Call directly for test
send_study_message_to_all()

print("🚀 Bot is running... waiting for 10:00 PM IST (04:50 UTC)")

# Optional: heartbeat log
schedule.every(1).minutes.do(lambda: print(f"💓 Alive at {time.strftime('%H:%M:%S')}"))

while True:
    schedule.run_pending()
    time.sleep(10)