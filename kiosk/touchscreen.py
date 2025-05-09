
import tkinter as tk
import requests

def send_selection(category):
    try:
        requests.post("http://localhost:5000/update", json={"category": category})
    except Exception as e:
        print("Failed to send selection:", e)

root = tk.Tk()
root.title("Media Selector")

for cat in ["Campus", "Robotics", "Clubs"]:
    btn = tk.Button(root, text=cat, command=lambda c=cat: send_selection(c))
    btn.pack(fill="x", padx=10, pady=10)

root.mainloop()
