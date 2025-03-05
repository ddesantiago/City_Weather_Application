
"""
This is a simple script to demonsrate: 
- working with APIs, handling JSON files, HTTP communication 
- demonstrate basic GUI development
- basic python code for a functioning application
"""
import tkinter as tk
import requests #this library allows to communicate with HTTP

def get_weather():
    city = city_entry.get()
# Replace with API Key
    API_KEY = "421439bd7db1e13aa56d9ce8c8ce140b"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    """Fetches weather details for the given city."""
# Replace with API Key
    params = {"q": city, "appid": "421439bd7db1e13aa56d9ce8c8ce140b", "units": "metric"} #params are best structured in dictionaries
    
    try:
        response = requests.get(BASE_URL, params=params) #this is where the API is used
        data = response.json()

        if response.status_code == 200: #200 is the status code for success in HTTP
        
            temp = data["main"]["temp"]
            weather_desc = data["weather"][0]["description"].capitalize()
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

       #update labels with weather info
            weather_label.config(text=f"Weather: {weather_desc}")
            temp_label.config(text=f"Temperature:{temp}°C")
            humidity_label.config(text=f"Wind Speed: {humidity} %")
            wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
    
        else:
            weather_label.config(text="City not found. Please check the name and try again.")
    except Exception as e:
        weather_label.config(text="Error fetching data.")

#Create the main tkinter window
root = tk.Tk() #this is the main window where everything is placed 
root.title("Weather App")
root.geometry("350x250") # sets the window size

#Creates widgets (labels, entry, button)
tk.Label(root, text="Enter City Name:").pack(pady=25) #.pack is method to call for spacing
city_entry = tk.Entry(root)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial",12))
weather_label.pack()

temp_label = tk.Label(root, text="", font=("Arial",12))
temp_label.pack()

humidity_label = tk.Label(root, text="", font=("Arial",12))
humidity_label.pack()

wind_label = tk.Label(root, text="", font=("Arial",12))
wind_label.pack()

#Start tkinter event loop (this keeps the window running otherwise would simply close once all code is executed)
root.mainloop()


    