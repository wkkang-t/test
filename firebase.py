#!/usr/bin/env python3
import time
import serial
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('test-6127b-firebase-adminsdk-7vcwg-c79cfceb70.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-6127b-default-rtdb.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = ref = db.reference('/')

try:
    ser = serial.Serial()
    ser.port = '/dev/ttyACM0'
    ser.baudrate = 115200
    ser.bytesize = serial.EIGHTBITS
    ser.parity =serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.timeout = 1
    ser.open()
    ser.write(b'\r\r')
    time.sleep(1)
    ser.write(b'lep\r')
    ser.close()

except Exception as e:
    print(e)
    pass
print(ser)

ser.open()

while True:
    try:
        data=str(ser.readline())

        if data[2] == "P":
            print(data)
            ref.push().set(data)
            time.sleep(1)

        time.sleep(0.01)
    except Exception as e:
        print(e)
        pass
    except KeyboardInterrupt:
        ser.close()
        

