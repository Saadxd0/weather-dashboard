import tkinter as tk
from tkinter import messagebox
from weather_api import get_weather_data

def show_weather():
    city = city_entry.get()
    data = get_weather_data(city)

    if data:
        city_label.config(text=f"Weather in {city}")
        temp_label.config(text=f"Temperature: {data['main']['temp']}°C")
        humid_label.config(text=f"Humidity: {data['main']['humidity']}%")
        wind_label.config(text=f"Wind Speed: {data['wind']['speed']} m/s")
        condition_label.config(text=f"Condition: {data['weather'][0]['description'].title()}")
    else:
        messagebox.showerror("Error", "City not found or API issue!")

# GUI
root = tk.Tk()
root.title("Weather Dashboard")
root.geometry("300x250")

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=10)

tk.Button(root, text="Get Weather", command=show_weather).pack()

city_label = tk.Label(root, text="", font=("Arial", 14))
city_label.pack(pady=5)

temp_label = tk.Label(root, text="")
humid_label = tk.Label(root, text="")
wind_label = tk.Label(root, text="")
condition_label = tk.Label(root, text="")

temp_label.pack()
humid_label.pack()
wind_label.pack()
condition_label.pack()

root.mainloop()
