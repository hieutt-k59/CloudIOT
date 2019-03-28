import paho.mqtt.client as mqtt
import json
import argparse
from datetime import datetime
# from cloud.process.RBI import DM_CAL

# This is the Publisher
# d = DM_CAL.DM_CAL(HighlyEffectDeadleg=True, ContainsDeadlegs=False, OnlineMonitoring="Sulfuric acid (H2S/H2) corrosion high velocity - Key process parameters")
# print(d.DF_THIN(5.08))
def set_data(humi, tem):
    data = []
    t = datetime.now()
    data.append(int(t.year))
    data.append(int(t.month))
    data.append(int(t.day)) 
    data.append(int(t.hour)) 
    data.append(int(t.minute)) 
    data.append(float(humi)) 
    data.append(float(tem))
    return data
def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server_ip', default='localhost', help='Server IP address')
    parser.add_argument('--port', default=1883, help='Port listen')
    parser.add_argument('--humi', default=0, help='Humidity value')
    parser.add_argument('--tem', default=0, help="Temperature value")
    parser.add_argument('--sensor', default="01", help="MAC Sensor")
    return parser.parse_args()
def main():
    args = parse_command_line_args()
    CLOUD_URL = args.server_ip
    PORT = int(args.port)
    TOPIC = "sensor/" + str(args.sensor)
    client = mqtt.Client()
    client.connect(CLOUD_URL, PORT, 60)
    data = set_data(args.humi, args.tem)
    send_data = json.dumps(data)
    print(send_data)
    print(TOPIC)
    client.publish(TOPIC, send_data)
    client.disconnect()


if __name__ == "__main__":
    main()


