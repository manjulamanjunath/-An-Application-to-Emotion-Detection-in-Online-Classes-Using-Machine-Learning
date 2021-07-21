from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC33917b16d95bf53a3227ad4f99aa4122"
auth_token = "d28f103bcdea8e00a595b47764776784"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+91-8073129216",
    from_="+19093652750" ,  #+1 210-762-4855"
    body=" Detected" )
