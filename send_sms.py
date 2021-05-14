

import os
from twilio.rest import client
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = client(account_sid, auth_token)
client.messages.create(
    to=os.environ["MY_PHONE_NUMBER"],
    from_="+9720526506946"
    body="test"
)