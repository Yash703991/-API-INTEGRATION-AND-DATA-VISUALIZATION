import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# API Key and base URL
API_KEY = '9d444d98c3306535a5426db9f5e08cda'
BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'

# City and parameters
city = 'Nagpur'
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric',  # Get temperature in Celsius
    'cnt': 10  # Number of data points (3-hour intervals)
}

# Fetch data from the API
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    
    # Extract relevant information
    dates = []
    temperatures = []
    humidity = []

    for entry in data['list']:
        date = datetime.datetime.fromtimestamp(entry['dt'])
        dates.append(date)
        temperatures.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])

    # Plot temperature and humidity
    sns.set(style='whitegrid')
    
    # Temperature Plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=dates, y=temperatures, marker='o', label='Temperature (°C)', color='orange')
    plt.title(f'Temperature Trend in {city}')
    plt.xlabel('Date/Time')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Humidity Plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=dates, y=humidity, marker='o', label='Humidity (%)', color='blue')
    plt.title(f'Humidity Trend in {city}')
    plt.xlabel('Date/Time')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print(f"Error: {response.status_code} - {response.json()['message']}")


