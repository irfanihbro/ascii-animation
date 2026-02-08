import sys
import time
import os

def Animasi():
    folder = "frame"
    if not os.path.exists(folder):
        print(f"folder '{folder}' tidak ditemukan!")
        return

    frames = [
        {"nama_file": "1.txt", "waktu": 0.1},
        {"nama_file": "2.txt", "waktu": 0.1},
        {"nama_file": "3.txt", "waktu": 0.1},
        {"nama_file": "4.txt", "waktu": 0.1},
        {"nama_file": "5.txt", "waktu": 0.1},
        {"nama_file": "4.txt", "waktu": 0.1},
        {"nama_file": "3.txt", "waktu": 0.1},
        {"nama_file": "2.txt", "waktu": 0.1},
    ]

    while True:
        for frame in frames:
            frame_path = os.path.join(folder, frame["nama_file"])
            if os.path.exists(frame_path):
                with open(frame_path, "r") as f:
                    content = f.read()
                sys.stdout.write("\033c")  
                sys.stdout.write(content)
                sys.stdout.flush()
                time.sleep(frame["waktu"])

Animasi()