import os
import time
import schedule
from twilio.rest import Client

# Load Twilio credentials securely
account_sid = os.getenv("AC103f8bb439c5a04d17b03d9ee8d6d99b")
auth_token = os.getenv("3e1fd58ad1875c45ef6339862654d005")
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
schedule.every().day.at("04:50").do(send_study_message_to_all)

print("🚀 Bot is running... waiting for 10:00 PM IST (04:50 UTC)")

while True:
    schedule.run_pending()
    time.sleep(10)
