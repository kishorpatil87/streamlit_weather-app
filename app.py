import streamlit as st
import requests

# Base URL for Weatherstack API
BASE_URL = "http://api.weatherstack.com/current"
API_KEY = "ddb71af2b28f997e73e4f1c9f616f2c6"  # Replace with your Weatherstack API key

# Function to fetch weather data
def get_weather(city):
    params = {
        "access_key": API_KEY,
        "query": city
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

# Streamlit App
st.set_page_config(page_title="Weather Information App", layout="centered")
st.title("Weather Information App")
st.markdown("Enter a city name to get the current weather information.")

# Input from user
city = st.text_input("Enter the city name:")

if st.button("Get Weather"):
    if city.strip() == "":
        st.error("Please enter a valid city name.")
    else:
        data = get_weather(city)
        
        # Check if response contains weather data
        if "current" in data:
            current = data["current"]
            location = data.get("location", {}).get("name", city)

            # Display weather details
            st.success(f"Weather Information for {location}:")
            st.write(f"**Temperature:** {current['temperature']}°C")
            st.write(f"**Weather Description:** {', '.join(current['weather_descriptions'])}")
            st.write(f"**Humidity:** {current['humidity']}%")
            st.write(f"**Wind Speed:** {current['wind_speed']} km/h")
        else:
            # Handle error messages from the API
            error_info = data.get("error", {}).get("info", "Unknown error occurred.")
            st.error(f"Error: {error_info}")
