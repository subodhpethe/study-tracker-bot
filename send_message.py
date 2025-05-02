# Import libraries
from twilio.rest import Client
import schedule
import time

# Your Twilio account details
account_sid = 'AC103f8bb439c5a04d17b03d9ee8d6d99b'
auth_token = '3e1fd58ad1875c45ef6339862654d005'
twilio_whatsapp_number = 'whatsapp:+14155238886'

# List of student WhatsApp numbers
student_numbers = [
    'whatsapp:+919823036706',
    'whatsapp:+919823046706',
    'whatsapp:+919325622859',
    'whatsapp:+919422356245',
    'whatsapp:+919637578485',
]# add all 120 numbers here

# Create Twilio client
client = Client(account_sid, auth_token)

# Function to send message to all students
def send_study_message_to_all():
    print("⏰ Function triggered — sending messages...")
    for number in student_numbers:
        try:
            message = client.messages.create(
                body="🌟 Hi! How many hours did you study today? Please reply honestly. 📚",
                from_=twilio_whatsapp_number,
                to=number
            )
            print(f"✅ Sent to {number} at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"❌ Error for {number}: {e}")
        time.sleep(1)

schedule.every().day.at("04:02").do(send_study_message_to_all)

print("Bot is running... and will send messages everyday at 04:02 PM IST")

while True:
    schedule.run_pending()
    time.sleep(10)
   
