import tkinter as tk
from datetime import datetime
import requests
from PIL import Image, ImageTk  # <--- NYTT

# --- Konfigurasjon ---
BG_COLOR = "#f9f9f9"
HEADER_COLOR = "#76c8f9"
TEXT_COLOR = "#000000"

FONT_HEADER = ("Helvetica", 30, "bold")
FONT_SUBHEADER = ("Helvetica", 20, "bold")
FONT_TIME = ("Helvetica", 40)
FONT_SMALL = ("Helvetica", 16)
FONT_TINY = ("Helvetica", 12)

# --- Entur API ---
ENTUR_URL = "https://api.entur.io/journey-planner/v3/graphql"
ENTUR_HEADERS = {
    "Content-Type": "application/json",
    "ET-Client-Name": "infoskjerm-test"
}
ENTUR_QUERY = """
{
  quay(id: "NSR:Quay:74792") {
    estimatedCalls(timeRange: 7200, numberOfDepartures: 5) {
      expectedArrivalTime
      destinationDisplay {
        frontText
      }
      serviceJourney {
        line {
          name
        }
      }
    }
  }
}
"""


# --- GUI Setup ---
root = tk.Tk()
root.title("Info Skjerm")
root.geometry("600x800")
root.configure(bg=BG_COLOR)

# Hilsen
greeting_frame = tk.Frame(root, bg=BG_COLOR)
greeting_frame.pack(pady=10, anchor="w", padx=20)
tk.Label(greeting_frame, text="God morgen", font=FONT_HEADER, fg=HEADER_COLOR, bg=BG_COLOR).pack(anchor="w")
tk.Label(greeting_frame, text="mester", font=FONT_HEADER, fg=HEADER_COLOR, bg=BG_COLOR).pack(anchor="w")

# Tid og dato
time_frame = tk.Frame(root, bg=BG_COLOR)
time_frame.place(x=420, y=10)
time_label = tk.Label(time_frame, font=FONT_TIME, fg=HEADER_COLOR, bg=BG_COLOR)
time_label.pack(anchor="e")
date_label = tk.Label(time_frame, font=FONT_SMALL, fg=HEADER_COLOR, bg=BG_COLOR)
date_label.pack(anchor="e")

def update_time():
    now = datetime.now()
    time_label.config(text=now.strftime("%H:%M"))
    date_label.config(text=now.strftime("Tuesday %-d. %B"))
    root.after(1000, update_time)

# Eksamen
calendar_frame = tk.Frame(root, bg="white", bd=0, relief="solid")
calendar_frame.pack(pady=10, padx=20, fill="x")
tk.Label(calendar_frame, text="Exams", font=FONT_SMALL, bg="white", anchor="w").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Label(calendar_frame, text="15:00", font=FONT_SMALL, bg="white", anchor="e", fg=HEADER_COLOR).grid(row=0, column=1, sticky="e", padx=10)
tk.Label(calendar_frame, text="Exams", font=FONT_SMALL, bg="white", anchor="w").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(calendar_frame, text="17:00", font=FONT_SMALL, bg="white", anchor="e", fg=HEADER_COLOR).grid(row=1, column=1, sticky="e", padx=10)

# Vær (placeholder)
weather_frame = tk.Frame(root, bg=BG_COLOR)
weather_frame.place(x=480, y=210)
tk.Label(weather_frame, text="☀️", font=("Helvetica", 24), bg=BG_COLOR).pack()
tk.Label(weather_frame, text="6.7°", font=FONT_TINY, bg=BG_COLOR, fg=TEXT_COLOR).pack()
tk.Label(weather_frame, text="4 m/s", font=FONT_TINY, bg=BG_COLOR, fg=TEXT_COLOR).pack()

# Bussruter
bus_frame = tk.Frame(root, bg="white")
bus_frame.pack(pady=20, padx=20, fill="x")

# Globale lister for å beholde bilde-referanser
bus_images = []
route_images = []

def bus_row(parent, route_num, destination, wait):
    row = tk.Frame(parent, bg="white")
    row.pack(fill="x", pady=2)

    # Rutenummer som bilde
    try:
        route_img = Image.open(f"{route_num}.png").resize((70, 34))
        route_photo = ImageTk.PhotoImage(route_img)
        route_images.append(route_photo)
        tk.Label(row, image=route_photo, bg="white").pack(side="left", padx=5)
    except Exception as e:
        route_img = Image.open("12.png").resize((70, 34))
        route_photo = ImageTk.PhotoImage(route_img)
        route_images.append(route_photo)
        tk.Label(row, image=route_photo, bg="white").pack(side="left", padx=5)

    # Destinasjon
    tk.Label(row, text=destination, font=FONT_SMALL, bg="white").pack(side="left", padx=10)

    # Tid til ankomst
    tk.Label(row, text=wait, font=FONT_SMALL, fg=HEADER_COLOR, bg="white").pack(side="right", padx=10)

def update_bus_info():
    for widget in bus_frame.winfo_children():
        widget.destroy()

    try:
        response = requests.post(ENTUR_URL, json={'query': ENTUR_QUERY}, headers=ENTUR_HEADERS)
        data = response.json()
        now = datetime.now()
        for call in data["data"]["quay"]["estimatedCalls"]:
            arrival_time = datetime.fromisoformat(call["expectedArrivalTime"][:-6])
            diff = int((arrival_time - now).total_seconds() // 60)
            line = call["serviceJourney"]["line"]["name"]
            dest = call["destinationDisplay"]["frontText"]
            bus_row(bus_frame, line, dest, f"{diff} min")
    except Exception as e:
        bus_row(bus_frame, "??", "Ingen data", "N/A")
        print("Feil ved henting av bussdata:", e)

    root.after(60000, update_bus_info)  # Oppdater hvert minutt

# Start alt
update_time()
update_bus_info()

root.mainloop()
