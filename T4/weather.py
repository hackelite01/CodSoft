import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap
import time


# functions


def get_weather(city):
    try:
        API_KEY = "bc295a4bc8727b69c6df749ba9cc88be"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        res = requests.get(url)

        if res.status_code == 404:
            messagebox.showerror("Error", "City not found")
            return None

        # get weather information
        weather = res.json()
        icon_id = weather['weather'][0]['icon']
        temperature = weather['main']['temp'] - 273.15
        description = weather['weather'][0]['description']
        city = weather['name']
        country = weather['sys']['country']
        min_temp = int(weather['main']['temp_min'] - 273.15)
        max_temp = int(weather['main']['temp_max'] - 273.15)
        pressure = str(weather['main']['pressure'])
        humidity = str(weather['main']['humidity'])
        wind = str(weather['wind']['speed'])
        sunrise = time.strftime("%I:%M:%S", time.gmtime(
            weather['sys']['sunrise'] - 21600))
        sunset = time.strftime("%I:%M:%S", time.gmtime(
            weather['sys']['sunset']-21600))

        # icon for weather
        icon_url = f" https://openweathermap.org/img/wn/{icon_id}@2x.png"
        return (max_temp, min_temp, pressure, humidity, wind, sunrise, sunset, icon_url, temperature, description, city, country)
    except:
        messagebox.showerror(
            "Error", "There was a problem retrieving that information")


def search():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name")
        return
    result = get_weather(city)
    if result is None:
        return
    max_temp, min_temp, pressure, humidity, wind, sunrise, sunset, icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city},{country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    img = image.resize((130, 130))
    icon = ImageTk.PhotoImage(img)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"Temperature: {temperature:.2f}°C")
    description_label.configure(text=f"Description: {description}")
    min_label.configure(text=f"Minimum Temperature: {min_temp}°C")
    max_label.configure(text=f"Maximum Temperature: {max_temp}°C")
    pressure_label.configure(text=f"Pressure: {pressure}")
    humidity_label.configure(text=f"Humidity: {humidity}%")
    wind_label.configure(text=f"Wind: {wind}km/h")
    sunrise_label.config(text=f"Sunrise: {sunrise}")
    sunset_label.configure(text=f"Sunset: {sunset}")


window = ttkbootstrap.Window(themename="morph")
window.title("Quiz App")
window.geometry("500x650")
# window.resizable(0, 0)

heading = tk.Label(window, text="Weather App", font="Arial,30,bold")
heading.pack(pady=20, padx=130)


# Search textfield
city_entry = ttkbootstrap.Entry(window, font="helvetica,18")
city_entry.pack(pady=10)

# Button
search_btn = ttkbootstrap.Button(
    window, text="Search", command=search, bootstyle="warning")
search_btn.pack(pady=10)

# label
location_label = tk.Label(window, font="helvetica,25")
location_label.pack(pady=15)

icon_label = tk.Label(window)
icon_label.pack()

temperature_label = tk.Label(window, font="helvetica,20")
temperature_label.pack()

description_label = tk.Label(window, font="helvetica,20")
description_label.pack()

min_label = tk.Label(window, font="helvetica,20")
min_label.pack()

max_label = tk.Label(window, font="helvetica,20")
max_label.pack()

pressure_label = tk.Label(window, font="helvetica,20")
pressure_label.pack()

humidity_label = tk.Label(window, font="helvetica,20")
humidity_label.pack()

wind_label = tk.Label(window, font="helvetica,20")
wind_label.pack()

sunrise_label = tk.Label(window, font="helvetica,20")
sunrise_label.pack()

sunset_label = tk.Label(window, font="helvetica,20")
sunset_label.pack()


window.mainloop()
