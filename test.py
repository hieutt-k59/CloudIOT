import os
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'RbiCloud.settings'
application = get_wsgi_application()
from cloud import models
import argparse

import json

from datetime import datetime

def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '--registry_id', required=True, help='Cloud IoT Core registry id')
    parser.add_argument(
            '--device_id', required=True, help='Cloud IoT Core device id')

    return parser.parse_args()


def main():
    args = parse_command_line_args()
    registry_id = args.registry_id
    print(registry_id)

def write_to_file():
    f = open('./json/temperature.json', 'w')
    data = {
        "label": "Sensor32",
        "data": [[1999,31], [2000,31.4], [2001, 32], [2002, 33], [2003, 33.1], [2004, 33.2], [2005, 33.2], [2006, 33.2], [2007,33.1], [2008, 30]]
    }
    json.dump(data, f)
# if __name__ == '__main__':
#     main()

# write_to_file()
# f = open('./json/temperature.json', mode='r')
# data = json.load(f)
# f.close()
# cnt = 0
# for item in data:
#         cnt = cnt + 1
# # tmp.append([2010, 29])
# # data['data'] = tmp
# print(cnt)
# f = open('./json/temperature.json', mode='w')
# json.dump(data, f)

f = open('./json/temperature.json', mode='r')
data = json.load(f)
json_data = json.dumps(data)
# print(data["label"])
data_sensor = {}
for sensor in data:
        if sensor["label"] == 32:
                data_sensor = sensor
f.close()
sensor = json.dumps(data_sensor)
# # print(sensor)
# print(datetime.now())
############ test append ################
# a = models.DataSensor.objects.get(data_id=2)
# arr = []
# t = a.time_get
# arr.append([int(t.year), int(t.month), int(t.day), int(t.hour), int(t.minute), float(a.temp)])
# print(arr)
########### test compare str ###################
# str = "hello/goodbye"
# arr = str.split('/')
# if arr[0] == "hello":
#         print("True")
# else:
#         print("False")
# print(arr[0] + ' ' + arr[1])
s = [[1,2,3,4,5]]
print(s[0][1])

