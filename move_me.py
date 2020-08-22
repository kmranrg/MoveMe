from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import json

# Type this command in Terminal: pip install watchdog


class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

# setting-up the folder paths
folder_to_track = '/home/kmranrg/Documents/MoveMe/TrackingFolder'
folder_destination = '/home/kmranrg/Documents/MoveMe/DestinationFolder'


event_handler = MyHandler()
observer = Observer()

observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()

# NOTE: If you're on running on IDLE, just press `Ctrl + c` and wait for 10 seconds to stop the program.
