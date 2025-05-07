import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Funksjon for å hente værdata
def fetch_weather():
    latitude = 63.4305
    longitude = 10.3951

    url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}"
    headers = {
        "User-Agent": "MyWeatherApp/1.0 your_email@example.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        current_weather = data["properties"]["timeseries"][0]
        details = current_weather["data"]["instant"]["details"]

        temperature = details.get("air_temperature")
        wind_speed = details.get("wind_speed")

        next_hours = current_weather["data"].get("next_1_hours")
        if next_hours:
            symbol = next_hours["summary"]["symbol_code"]
        else:
            symbol = "Ingen værbeskrivelse tilgjengelig"

        return temperature, wind_speed, symbol

    else:
        return None, None, f"Feil: {response.status_code}"


# Lag Tkinter-vindu
root = tk.Tk()
root.title("Været i Trondheim")

# Hent værdata
temperature, wind_speed, symbol = fetch_weather()

# Lag labels
label_temp = ttk.Label(root, text=f"Temperatur: {temperature}°C")
label_temp.pack(pady=5)

label_wind = ttk.Label(root, text=f"Vindstyrke: {wind_speed} m/s")
label_wind.pack(pady=5)

label_symbol = ttk.Label(root, text=f"Værbeskrivelse: {symbol}")
label_symbol.pack(pady=5)

# Last inn og vis bildet
print(symbol)

try:
    image = Image.open(symbol + ".png")
    image = image.resize((150, 150))  # Tilpass størrelsen hvis ønskelig
    photo = ImageTk.PhotoImage(image)

    label_image = ttk.Label(root, image=photo)
    label_image.image = photo  # Viktig: behold en referanse!
    label_image.pack(pady=10)

except FileNotFoundError:
    error_label = ttk.Label(root, text="Fant ikke bildet 'sun.png'")
    error_label.pack(pady=10)

root.mainloop()