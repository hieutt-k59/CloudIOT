import argparse

import json

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

write_to_file()
f = open('./json/temperature.json', mode='r')
data = json.load(f)
f.close()
tmp = data["data"]
tmp.append([2010, 29])
data['data'] = tmp
f = open('./json/temperature.json', mode='w')
json.dump(data, f)



