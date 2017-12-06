import requests
import json
import threading
def get_commands():
    threading.Timer(30.0, get_commands).start()
    print("\n" * 80)
    result1 = requests.get('http://10.76.100.160:5000/')
    result2 = requests.get('http://10.76.100.160:5000/')

    result1.raise_for_status()
    result2.raise_for_status()

    data1 = json.loads(result1.text)
    data2 = json.loads(result2.text)


    for message in data1:
        print(message)
    for message in data2:
        print(message)




get_commands()
