# Download the twilio-python library from httptwilio.comdocslibraries
from twilio.rest import TwilioRestClient
 
# Find these values at httpstwilio.comuseraccount
account_sid = "AC47a1f93e545b90a05c441a91e75998dd"
auth_token = "94602879a01ffb378a6335040e053a36"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+15622219630", from_="+15629916834",
                                     body="Hi this is a test of Twilio sending a text")