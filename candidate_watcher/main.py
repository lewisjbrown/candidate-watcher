import argparse
import os
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":

    # Parse the command line
    parser = argparse.ArgumentParser(description='Watch a candidate file for changes.')
    parser.add_argument('path', metavar='path', type=str, help='the path to the file.')
    args = parser.parse_args()

    # Extract the file to watch. The file will be volume mounted at /app/data
    file_to_watch = os.path.join("/app/data", args.path)

    while True:
        # To get user-friendly error messages, check the file exists. If not, print and go around the loop.
        if not os.path.isfile(file_to_watch):
            print(f"File not found: {args.path}. Waiting...")
            time.sleep(1)
        else:
            # The file definitely exists
            print("Watching file for changes...")

            # Create an instance of a Watchdog observer, and point it to the file_to_watch.
            event_handler = LoggingEventHandler()
            observer = Observer()
            observer.schedule(event_handler, file_to_watch, recursive=False)
            observer.start()

            try:
                while True:
                    # Keep the app alive while the observer is observing.
                    time.sleep(1)

                    # Corner case. If the file is deleted, the Watchdog Observer will essentially become defunct.
                    # So check for a missing file, and if so then break out of the inner while loop.
                    # This will cause the app to go back around the outer while loop and recreate the observer when the file
                    # eventually exists again.
                    if not os.path.isfile(file_to_watch):
                        break

            finally:
                observer.stop()
                observer.join()
    