import tkinter as tk
import tkinter.messagebox as tmb
import get_data
import os

def dashboard():
    root = tk.Tk()
    root.title("Weather Dashboard")
    root.geometry("420x585")
    root.resizable(False, False)
    root.configure(bg="#e0f7fa")  # light blue background

    history = []

    def get_city():

        city = city_name.get()
        error_msg = f'❌ Error: [{city}] is not a city!'
        data = get_data.get_weather(city)

        if data is None:
            error_msg_label.config(text=error_msg)

        else:
            local_time = data['local time']
            weather = data['weather'].lower()
            show_weather_icon(weather)

            # Saving the weather of city in history list
            weather_history = f"{city.capitalize()}: {weather.upper()}" 
            history.append(weather_history)

            local_time_label.config(text=local_time)
            weather_detail_label.config(text=f'Weather today in {city.capitalize()} is {weather.upper()}')

            city_country_label.config(text=f"{data['city']}, {data['country']}")
            temp_label.config(text=f"{data['temperature']} °F")
            weather_label.config(text=f"{data['weather']}")
            max_temp_label.config(text=f"Max temp: {data['max temperature']}° F")
            min_temp_label.config(text=f"Min temp: {data['min temperature']}° F")
            humidity_label.config(text=f"Humidity: {data['humidity']} %")
            wind_speed_label.config(text=f"Wind speed: {data['wind speed'] * 3.6:.2f} km/h")
            wind_temp_label.config(text=f"Wind temp: {data['wind temp']}")
            pressure_label.config(text=f"Pressure: {data['pressure']} hPa")
            error_msg_label.config(text='')

        
    current_dir = os.getcwd()

    def save_history():
        with open('history.txt', 'a') as f:
            for i in history:
                f.write('\n')
                f.writelines(i)
        tmb.showinfo('History Saved', f'Weather history has been saved at {os.path.join(current_dir,'history.txt')}')

    def show_weather_icon(image):
        icon = tk.PhotoImage(file=f'icons/{image}.png')
        icon = icon.subsample(5, 5)
        weather_icon_label.config(image=icon)
        weather_icon_label.image = icon # To keep reference

    def about():

        about_project = '''
        Weather Dashboard is a simple desktop application buil
        with Python and Tkinter. It fetches real-time weather
        data using the OpenWeather API and displays key 
        information about current weather in a clean GUI.
        '''

        about_creator = '''
        Built by Izram as a hands-on project to strengthen Python
        skills, API handling, and GUI development with Tkinter.
        This project reflects a focus on clean structure, reusable
        logic, and learning by building real, functional applicatoins
        '''

        tmb.showinfo('About Project', about_project)
        tmb.showinfo('About Creator', about_creator)

    main_menu = tk.Menu(root)
    root.config(menu=main_menu)

    def sub_menu(main_text, sub_text, command):
        sub_menu = tk.Menu(main_menu, tearoff=0)
        sub_menu.add_command(label=sub_text, command=command)
        main_menu.add_cascade(label=main_text, menu=sub_menu)

    sub_menu('History', 'Save History', save_history)
    sub_menu('About', 'About Project and creator', about)

    # Header
    header = tk.Frame(root, bg="#0288d1")
    header.pack(pady=10, fill='x')

    tk.Label(header, text="Weather Dashboard", font=("Arial black", 24, "bold"), bg="#0288d1", fg="white").pack()
    city_country_label = tk.Label(header, text="", font=("Arial", 12), bg="#0288d1", fg="white")
    city_country_label.pack()

    # Search section
    search_frame = tk.Frame(root, bg="#b3e5fc")
    search_frame.pack(pady=15, fill='x')

    tk.Label(search_frame, text='CITY:', bg="#b3e5fc").pack(side='left')
    city_name = tk.Entry(search_frame, width=25)
    city_name.pack(side="left", padx=5)
    search_button = tk.Button(search_frame, text="Search", command=get_city, bg="#0288d1", fg="white")
    search_button.pack(side="left")

    # Main weather display
    main_weather = tk.Frame(root, bg="#81d4fa")
    main_weather.pack(pady=10, fill='x')

    temp_label = tk.Label(main_weather, text="_._", font=("Arial", 32, "bold"), bg="#81d4fa")
    temp_label.pack()
    weather_label = tk.Label(main_weather, text="__", font=("Arial", 14), bg="#81d4fa")
    weather_label.pack()

    weather_icon_label = tk.Label(main_weather, bg="#81d4fa", anchor='center', justify='center')
    weather_icon_label.pack(pady=5, fill='x') 

    weather_detail_label = tk.Label(main_weather, text='Weather Today')
    weather_detail_label.pack(pady=5, fill='x')

    # Local time 
    time_frame = tk.Frame(root, bg='#e0f7fa')
    time_frame.pack(fill='x')

    local_time_label = tk.Label(time_frame, text='Local Time: _', bg="#e0f7fa")
    local_time_label.pack()

    # Details section
    details = tk.Frame(root, bg="#b3e5fc")
    details.pack(pady=10, ipady=10, ipadx=10, fill='x')

    tk.Label(details, text='OTHER DETAILS', bg="#b3e5fc").pack()

    left = tk.Frame(details, bg="#b3e5fc")
    left.pack(side="left", padx=20)

    right = tk.Frame(details, bg="#b3e5fc")
    right.pack(side="right", padx=20)

    min_temp_label = tk.Label(left, text="Min Temp: _", bg="#b3e5fc")
    min_temp_label.pack(anchor="w")
    max_temp_label = tk.Label(left, text="Max Temp: _", bg="#b3e5fc")
    max_temp_label.pack(anchor="w")
    humidity_label = tk.Label(left, text="Humidity: _", bg="#b3e5fc")
    humidity_label.pack(anchor="w")

    wind_speed_label = tk.Label(right, text="Wind Speed: _", bg="#b3e5fc")
    wind_speed_label.pack(anchor="w")
    wind_temp_label = tk.Label(right, text='Wind Temp: _', bg="#b3e5fc")
    wind_temp_label.pack(anchor='w')
    pressure_label = tk.Label(right, text="Pressure: _", bg="#b3e5fc")
    pressure_label.pack(anchor="w")

    # Footer
    footer = tk.Frame(root, bg="#e0f7fa")
    footer.pack(fill='x')

    error_msg_label = tk.Label(footer, text="", bg="#e0f7fa")
    error_msg_label.pack()

    # Status bar
    status_frame = tk.Frame(root, bg="#0288d1")
    status_frame.pack(side='bottom', fill='x')

    tk.Label(status_frame, text='Created by Izram Khan', bg='#0288d1').pack(side='left')

    root.mainloop()
