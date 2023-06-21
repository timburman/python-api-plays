import requests
import warnings
from datetime import datetime
import smtplib
import time

warnings.filterwarnings(action="ignore")

LAT = 28.704060
LONG = 77.102493
EMAIL = "pythontutorials69@gmail.com"
PASSWORD = "mbxmapngtkhvjkhw"

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json", verify=False)
    data = response.json()

    iss_long = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])
    iss_timestamp = data['timestamp']



    if (LAT-5 <= iss_latitude >= LAT+5) or (LONG-5 <= iss_long >= LONG+5 ):
        return True

def is_night():
    parameters = {
        'lat':LAT,
        'long': LONG,
        'formatted':0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", verify=False, params=parameters)
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    current_time = datetime.now().hour

    if current_time > sunset or current_time < sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, 
                            to_addrs='crplayer181102@gmail.com',
                            msg="Subject:International Space Station\n\nThe International space station is passing by look up")
