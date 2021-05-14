# Cowin vaccine slot Notifier

It is a python script which notifies you by alerting in your laptop and sending a message to the mobile as soon as the slots will be available for the mentioned date and the age of the patient

## Installation

Use the Link given to download [python](https://www.python.org/downloads/)

## Twillio Login

You need to update the global variables in the script with the client ID and client Secret that would be available to you after you register in [twilio](https://www.twilio.com/) and the fromMobile also would be available once you login and the toMobile would be the client mobile number


## To run this:
- `virtualenv -p python3 venv`
- `source venv/bin/activate`
- `pip3 install -r requirements.txt`
-
    ```
    python cowin_slots_notifier.py --help
    ```
- For instance, to find the slots for a person age 40, and pincode 522006
    ```
    python cowin_slots_notifier.py -pin=522006 -age=40
    ```

## Usage

```
node cowin_slots_notifier.py --age
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
