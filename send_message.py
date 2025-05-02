import os
import time
print("✅ Script started at", time.strftime('%Y-%m-%d %H:%M:%S'))
import schedule
from twilio.rest import Client

# Load Twilio credentials securely
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_whatsapp_number = 'whatsapp:+14155238886'  # Your sandbox number

# Create Twilio client
client = Client(account_sid, auth_token)

# Student numbers list
student_numbers = [
    'whatsapp:+919823036706',
    'whatsapp:+919823046706',
    # add more numbers here
]

# Function to send messages one per second
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
        time.sleep(1)  # 1 message/sec rate limit

# Use this during testing only
# send_study_message_to_all()

# Schedule at 10:00 PM IST = 16:30 UTC
#schedule.every().day.at("04:50").do(send_study_message_to_all)
send_study_message_to_all()
print("🚀 Bot is running... waiting for 10:00 PM IST (04:50 UTC)")

while True:
    schedule.run_pending()
    time.sleep(10)
