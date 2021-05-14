import time
import requests
import argparse
from twilio.rest import Client
from datetime import datetime, timedelta

account = ""
token = ""
client = Client(account, token)
from_mobile = ""
to_mobile = ""

parser = argparse.ArgumentParser(description="Cowin Slot date and time finder")
parser.add_argument("pin", help="The pin code of the area of the vaccination centre")

parser.add_argument("-age", help="The age of the patient taking the vaccination, default is 50", default=50, type=int)

parser.add_argument("-days", "--no-of-days", help="Max number of days to check from the current date, default is 2",
                    default=2, type=int)

args = parser.parse_args()
age = args.age
pin_codes = [args.pin]
num_days = 2

print_flag = 'Y'

print("Searching in progress !")
print("On March 22, at 5 o clock, we should stand on our doorways, balconies, in our windows and keep "
      "clapping hands and ringing the bells for 5 mins to salute and encourage them. If we can do this, "
      "we can fight any battle in the world. \t\n - Narendra Modi")

actual = datetime.today()
list_format = [actual + timedelta(days=i) for i in range(num_days)]
actual_dates = [i.strftime("%d-%m-%Y") for i in list_format]

while True:
    counter = 0

    for pin_code in pin_codes:
        for given_date in actual_dates:

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".\
                format(pin_code, given_date)
            header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/56.0.2924.76 Safari/537.36'}

            result = requests.get(URL, headers=header)

            if result.ok:
                response_json = result.json()

                flag = False
                if response_json["centers"]:
                    if print_flag.lower() == 'y':
                        for center in response_json["centers"]:
                            for session in center["sessions"]:
                                if session["min_age_limit"] <= age and session["available_capacity"] > 0:
                                    print('Pincode: ' + pin_code)
                                    print("Available on: {}".format(given_date))
                                    print("\t", center["name"])
                                    print("\t", center["block_name"])
                                    print("\t Price: ", center["fee_type"])
                                    print("\t Availablity : ", session["available_capacity"])

                                    if session["vaccine"] != '':
                                        print("\t Vaccine type: ", session["vaccine"])
                                        print("\n")
                                    print("Congratulations you are the one in a million who's finally able to book a slot")
                                    # message = client.messages.create(to=to_mobile, from_=from_mobile, body="Slots found for pincode: {0}, date: {1}, .\
                                    #         centre_name: {2}".format(pin_code, given_date,center["name"]))
                                    counter = counter + 1
                                else:
                                    pass
                else:
                    pass

            else:
                print("No Response!")

    if counter == 0:
        print("Sorry no vaccination available, Go on twitter and blame Modiji with hashtag #ModiResign")
    else:
        print("Search Completed!")

    dt = datetime.now() + timedelta(minutes=3)

    while datetime.now() < dt:
        time.sleep(1)
