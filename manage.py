#!/usr/bin/env python
import os
import sys
import threading
import mosquittoMQTTSub
import paho.mqtt.client as mqtt
def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RbiCloud.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
# def mosquitto_mqtt_sub():
#     CLOUD_URL = '192.168.1.45'
#     TOPIC = "+/+"
#     PORT = 1883
#     client = mqtt.Client()
#     client.connect(CLOUD_URL,PORT)

#     client.on_connect = mosquittoMQTTSub.on_connect
#     client.on_message = mosquittoMQTTSub.on_message
#     client.subscribe(TOPIC, 0)
#     rc = 0
#     while rc == 0:
#         rc = client.loop()
#     print('rc: ' + str(rc))
if __name__ == "__main__":
    # thread1 = threading.Thread(target=main)
    # thread2 = threading.Thread(target=mosquitto_mqtt_sub)
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    main()
