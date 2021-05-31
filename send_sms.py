
# 1N7yNf5TUaxGPeGPijXhHkYYXmDJcDhMwA5OVW23 קוד למקרה שהטלפון נאבד

import os
from twilio.rest import Client
account_sid = 'AC9e4120ed8c67d56694404691d647aa9e'
auth_token = '0fee436091a1e789c9318a7709f98780'
phone_numbers = (['+972524560626'], ['+972526506946'])
Client = Client(account_sid, auth_token)

Client.messages.create(
    to='+972526506946',
    from_="+15087097328",
    body="עכשיו צריך שגוף ההודעה יהיה הפלט של הקוד"
)