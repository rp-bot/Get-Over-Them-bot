from twilio.rest import Client
import keys
import time
import random

client = Client(keys.account_sid, keys.auth_token)


def send_msg():
    message = client.messages.create(
        body="Stop checking your phone.",
        from_=keys.twilio_number, to=keys.target_number
    )
    print(message.body)


if __name__ == '__main__':
    while True:
        mins = random.randint(1, 5)

        time.sleep(mins*60)
        send_msg()
