import time
import os


def logs_generator():
    with open('akamill') as akamill:
        for lines in akamill.readlines():
            line_list = lines.split(",")
            find_what = line_list[1]
    print("Find what ", find_what)
    with open('akamill', 'r') as akamill:
        file_data = akamill.read()

    epoch_time = int(time.time())
    epoch_time_string = str(epoch_time)
    print("Replace with ", epoch_time)
    # Replace the target string
    file_data = file_data.replace(find_what, epoch_time_string)

    # Write the file out again
    with open('akamill', 'w') as file:
        file.write(file_data)

    os.system(
        'scp -o StrictHostKeyChecking=no -oHostKeyAlgorithms=+ssh-dss -2 akamill  root@198.18.85.50:/qosfs/incoming/qos/')
    print("Uploaded to Beacon server ")



for i in range(100000):
    print(i)
    logs_generator()
