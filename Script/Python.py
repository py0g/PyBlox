import requests
from flask import Flask
import threading
import tkinter as tk

app = Flask(__name__)

@app.route('/create-part', methods=['POST'])
def create_part():
    print("Part creation triggered")
    return "Part creation triggered", 200

def run_server():
    app.run(port=5000)

def create_part_request():
    url = "http://localhost:5000/create-part"
    try:
        requests.post(url)
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {e}")

def start_gui():
    root = tk.Tk()
    root.title("Roblox Part Creator")

    button = tk.Button(root, text="New Part", command=create_part_request)
    button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    start_gui()
