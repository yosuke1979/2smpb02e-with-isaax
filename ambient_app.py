# coding: utf-8
# Sample that outputs the value acquired by 2SMPD-02E.

from __future__ import print_function

import os
import time
import datetime

import ambient
import grove_2smpb_02e

# ambient instance
try:
    AMBIENT_CHANNEL_ID = int(os.environ['AMBIENT_CHANNEL_ID'])
    AMBIENT_WRITE_KEY = os.environ['AMBIENT_WRITE_KEY']
    CHECK_SPAN = int(os.environ.get('CHECK_SPAN', '30'))
    am = ambient.Ambient(AMBIENT_CHANNEL_ID, AMBIENT_WRITE_KEY)
except KeyError:
    print(KeyError)
    exit(1)

# sensor instance
sensor = grove_2smpb_02e.Grove2smpd02e()

def main():
    
    print ("start")
    
    while True:
        press, temp = sensor.readData()
        now = datetime.datetime.today()
        payload = {
          "d1": press,
          "d2": temp,
          "created": now.strftime("%Y/%m/%d %H:%M:%S")
        }
        try:
          am.send(payload)
        except Exception as e:
          print(e)

        time.sleep(5)

if __name__ == '__main__':
    main()
