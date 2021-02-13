import os
from twilio.rest import Client

# SID
account_sid = os.environ['AC961acf88bdad22d571745b2e452f4ce8']
# Authorization token
auth_token     = os.environ['079096026140e35d6041441e894929f5']

client = Client(account_sid, auth_token)