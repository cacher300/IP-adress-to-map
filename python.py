import os
import requests
import folium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
ip_address = "104.196.224.97"  # Replace with the IP address you want to plot
api_key = "3769022f22f74e83d35156324ac1d541"  # Replace with your IPStack API key

# Call the IPStack API to retrieve the geographic location data for the IP address
response = requests.get(f"http://api.ipstack.com/{ip_address}?access_key={api_key}")
data = response.json()

# Extract the latitude and longitude coordinates from the data dictionary
lat = data["latitude"]
lon = data["longitude"]

# Create a Folium map centered on the IP address location
map = folium.Map(location=[lat, lon], zoom_start=6)

# Add a marker for the IP address location
folium.Marker(location=[lat, lon], popup=ip_address).add_to(map)

# Save the map as an HTML file
map.save("map.html")

# Configure the ChromeOptions to use a headless browser
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Use the headless browser to take a screenshot of the webpage
driver = webdriver.Chrome(options=chrome_options)
driver.get("file://" + os.getcwd() + "/map.html")  # Open the HTML file with the map
time.sleep(1)
driver.save_screenshot("screenshot.png")
driver.quit()
