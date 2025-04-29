# Import libraries
from twilio.rest import Client
import schedule
import time

# Your Twilio account details
account_sid = 'AC103f8bb439c5a04d17b03d9ee8d6d99b'
auth_token = '903654107cffcb0d89c703e605573dd5'
twilio_whatsapp_number = 'whatsapp:+14155238886'

# List of student WhatsApp numbers
student_numbers = [
    'whatsapp:+919823036706',
    'whatsapp:+919823046706',
    'whatsapp:+919325622859',
    'whatsapp:+919021325237',
]# add all 120 numbers here

# Create Twilio client
client = Client(account_sid, auth_token)

# Function to send message to all students with delay and error handling
def send_study_message_to_all():
    print("⏰ Function called! Sending messages...")
    for number in student_numbers:
        try:
            message = client.messages.create(
                body="🌟 Hi! How many hours did you study today?",
                from_=twilio_whatsapp_number,
                to=number
            )
            print(f"✅ Sent to {number} at {time.strftime('%H:%M:%S')}")
        except Exception as e:
            print(f"❌ Error for {number}: {e}")
        time.sleep(1)

# TEMP TEST TIME — set 1-2 minutes ahead of current time
send_study_message_to_all()

print("⏳ Bot is running and waiting for the scheduled time...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(10)
