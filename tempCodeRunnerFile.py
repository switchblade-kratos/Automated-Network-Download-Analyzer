# scheduler.py

import time
from downloader import download_file
from logger import log_data

# Stable server
HOST = "speedtest.tele2.net"
PORT = 80
PATH = "/1MB.zip"
def run():
    try:
        file_size, time_taken, speed = download_file(HOST, PORT, PATH)

        speed_kb = speed / (1024)

        print(f"Downloaded: {file_size} bytes")
        print(f"Time: {time_taken:.2f} sec")
        print(f"Speed: {speed_kb:.2f} KB/s")

        log_data(file_size, time_taken, speed_kb)

    except Exception as e:
        print("Error:", e)

i = 0
while(1):
    print(f"\nRun {i+1}")
    i += 1
    run()

    time.sleep(5)  