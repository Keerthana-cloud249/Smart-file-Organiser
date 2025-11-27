Smart File Organizer (Python Project)

A desktop application that automatically organizes files inside any selected folder by sorting them into categories like Documents, Images, Videos, Music, Archives, and Others.
The tool performs initial sorting and then continues to monitor the folder in real-time using Watchdog.

Built using:
Python
Tkinter (GUI)
Watchdog (Real-time monitoring)

*Features
1. Initial Sorting
When the user selects a folder and clicks “Start Watching,” all existing files in the folder are immediately sorted.
2. Real-Time Auto Sorting
New files added to the folder are automatically detected and sorted into their correct category.
3. Duplicate File Handling
If a file with the same name already exists, the app creates a unique name like:
file (1).pdf, file (2).jpg, etc.
4. Simple & Clean GUI
Developed using Tkinter, allowing users to choose folders easily.
5. Background Processing
The watcher runs in a separate thread, ensuring the GUI remains responsive.

 How It Works
There are three major components:

1. file_handler.py
Handles:
Sorting logic
Moving files
Creating category folders
Managing duplicate names

2. watcher.py
Uses Watchdog to:

Detect file events (created/modified/moved/deleted)
Trigger automatic sorting

3. gui.py

Creates the user interface:
Browse folders
Start watching
Display logs

 Project Structure
Smart-File-Organizer/
│── gui.py
│── watcher.py
│── file_handler.py
│── main.py
│── screenshots/
│     ├── gui_start.png
│     ├── before_sorting.png
│     ├── after_sorting.png
│     ├── event_detected.png
│
└── README.md

How to Run the Program
Step 1: Install dependencies
Open CMD and run:
pip install watchdog

Tkinter comes pre-installed with Python.

Step 2: Run the Application
python main.py
python gui.py


*File Categories Supported
Category	Extensions
Documents	.pdf, .docx, .txt
Images	.jpg, .jpeg, .png
Videos	.mp4, .mov
Music	.mp3, .wav
Archives	.zip, .rar
Others	Any unsupported extension

*Future Enhancements
Add user custom categories
Provide theme options in GUI
Include progress bar during sorting
Add notification pop-ups

 Developed by

Keerthana Nair
B.Tech Student
Smart File Organizer – College Python Mini Project
