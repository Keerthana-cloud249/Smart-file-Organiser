from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from file_handler import organize_folder

class Watcher(FileSystemEventHandler):
    def __init__(self, folder):
        self.folder = folder

    # Trigger on ANY change: created, modified, moved, deleted
    def on_any_event(self, event):
        if not event.is_directory:   # ignore folder changes
            print(f"Event detected: {event.event_type} → {event.src_path}")
            organize_folder(self.folder)

def start_watching(folder_path):
    event_handler = Watcher(folder_path)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()
    print("Watching started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()



