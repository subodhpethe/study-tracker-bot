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
    'whatsapp:+919823036706',
    'whatsapp:+919021325237',
    'whatsapp:+918788621932',
    'whatsapp:+918788621932',
    'whatsapp:+919975297297',
    'whatsapp:+919284662915',
    'whatsapp:+918530613417',
    'whatsapp:+917020050581',
    'whatsapp:+918530613417',
    'whatsapp:+919284604584',
    'whatsapp:+919370414467',
    'whatsapp:+919422356245',
    'whatsapp:+919637578485',
    'whatsapp:+917276963301',
    'whatsapp:+918180064028',
    'whatsapp:+919764075718',
    'whatsapp:+919529592938',
    'whatsapp:+919112791515',
    'whatsapp:+919422911849',
    'whatsapp:+919284662915',
    'whatsapp:+917499157278',
    'whatsapp:+917559426954',
]# add all 120 numbers here

# Create Twilio client
client = Client(account_sid, auth_token)

# Function to send message to all students
def send_study_message_to_all():
    for number in student_numbers:
        message = client.messages.create(
            body="🌟 Hi! How many hours did you study today? Please reply honestly. 📚",
            from_=twilio_whatsapp_number,
            to=number
        )
        print(f"Message sent successfully to {number} at {time.strftime('%Y-%m-%d %H:%M:%S')}")

# Schedule the job
schedule.every().day.at("11:15").do(send_study_message_to_all)

print("Bot is running... and will send messages everyday at 11:15")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(10)
