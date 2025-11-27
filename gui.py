
import tkinter as tk
from tkinter import filedialog
from watcher import start_watching
import threading
from file_handler import organize_folder   # for initial sorting

class OrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Organizer")
        self.folder_path = tk.StringVar()

        tk.Label(root, text="Select Folder:").pack(pady=5)
        tk.Entry(root, textvariable=self.folder_path, width=40).pack()
        tk.Button(root, text="Browse", command=self.browse_folder).pack(pady=5)
        tk.Button(root, text="Start Watching", command=self.start).pack(pady=5)

        self.log_box = tk.Text(root, height=10, width=50)
        self.log_box.pack(pady=5)

    def browse_folder(self):
        path = filedialog.askdirectory()
        self.folder_path.set(path)

    def start(self):
        folder = self.folder_path.get()

        # --- STEP 0: Sort everything initially ---
        organize_folder(folder)
        self.log_box.insert(tk.END, "Initial sorting completed ✓\n")

        # --- Start watcher in background thread ---
        t = threading.Thread(target=start_watching, args=(folder,), daemon=True)
        t.start()
        self.log_box.insert(tk.END, f"Now watching: {folder}\n")

# ------ GUI launcher ------
def start_gui():
    root = tk.Tk()
    app = OrganizerApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_gui()
