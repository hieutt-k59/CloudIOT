import argparse

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


if __name__ == '__main__':
    main()



