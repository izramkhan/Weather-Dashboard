# 🌤️ Weather Dashboard (Python + Tkinter)

A clean, desktop-based weather dashboard built with Python and Tkinter that displays real-time weather data and local time using the OpenWeather API.

---

## 📌 Features

* Search weather by city name
* Real-time weather data from **OpenWeather API**
* Displays:

  * Current temperature
  * Minimum & maximum temperature
  * Weather condition
  * Humidity
  * Wind speed
  * Pressure
  * Local time of the city
* Weather icons based on conditions
* Weather search history (can be saved to a file)
* Simple, clean, and user-friendly GUI
* Error handling for invalid city names

---

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI)
* Requests (API handling)
* OpenWeather API

---

## 📂 Project Structure

```
weather-dashboard/
│
├── main.py              # Entry point
├── dashboard.py         # GUI logic
├── get_data.py          # API & data processing
├── history.txt          # Saved weather history (generated)
├── icons/               # Weather icons (PNG files)
│   ├── clear.png
│   ├── clouds.png
│   ├── rain.png
│   ├── haze.png
│   └── ...
└── README.md
```

⚠️ **Important:**
The `icons/` folder **must be included**.
If the image files are missing, the program will crash when loading weather icons.

---

## 🖼️ Weather Icons

Weather icons are loaded dynamically based on the weather condition returned by the API.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/izramkhan/Weather-Dashboard.git
cd Weather-Dashboard
```

### 2. Install dependencies

```bash
pip install requests
```

### 3. Add your OpenWeather API key

Open `get_data.py` and replace:

```python
api_key = "YOUR_API_KEY_HERE"
```

Get a free API key from:
[https://openweathermap.org/api](https://openweathermap.org/api)

---

### 4. Run the application

```bash
python main.py
```

---

## 📖 About the Project

This project was built as a hands-on exercise to strengthen:

* Python fundamentals
* API integration
* GUI development with Tkinter
* Clean project structure and separation of logic

The focus is on **clarity, functionality, and learning by building**, not overengineering.

---

## 👤 Author

**Izram Khan**
Student & Python Learner

---

## 📄 License

This project is open-source and available under the **MIT License**.
