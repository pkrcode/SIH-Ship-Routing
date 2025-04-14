import pygame
import requests
import os
from dotenv import load_dotenv

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
TEXT_COLOR = WHITE
BACKGROUND_COLOR = (30, 30, 30)
BORDER_COLOR = (128, 128, 128)
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)

# Fonts
def load_custom_font(size):
    return pygame.font.Font(None, size)  # Use a custom font path if desired.

# Load API Key
load_dotenv()
API_KEY = os.getenv("api_key")

# Function to fetch weather data
def get_weather_data(latitude, longitude):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": f"{data['main']['temp']}°C",
            "feels_like": f"{data['main']['feels_like']}°C",
            "humidity": f"{data['main']['humidity']}%",
            "wind_speed": f"{data['wind']['speed']} m/s",
            "description": data['weather'][0]['description'].capitalize().split()[0]
        }
    else:
        return {"error": "Unable to fetch weather data"}

# Function to display weather for the first location (departure)
def weather(screen, latitude, longitude):
    # Fetch weather data
    weather_data = get_weather_data(latitude, longitude)

    # Set up font and positioning
    weather_font = load_custom_font(24)
    label_font = load_custom_font(32)
    x_position = SCREEN_WIDTH * 3 // 4 + 80  # Shift right by 240 pixels
    y_position = SCREEN_HEIGHT * 3 // 4 + 15 # Adjust Y position for quadrant

    # Box properties
    box_width, box_height = 240, 180
    
    #text to display
    departure_label = label_font.render("Pref. Ship:", True, BLACK)
    screen.blit(departure_label, (700, 310))
    
    departure_label = label_font.render("Parameters:", True, BLACK)
    screen.blit(departure_label, (680, 380))
    
    departure_label = label_font.render("Ship dim:", True, BLACK)
    screen.blit(departure_label, (680, 450))

    # Draw "Departure" label
    departure_label = label_font.render("Departure", True, BLACK)
    screen.blit(departure_label, (760, 510))

    # Draw the weather box with a grey border
    pygame.draw.rect(screen, BORDER_COLOR, (700 - 2, 550 - 2, box_width + 4, box_height + 4), border_radius=10)
    pygame.draw.rect(screen, BACKGROUND_COLOR, (700, 550, box_width, box_height), border_radius=10)

    # Render weather data
    if "error" not in weather_data:
        weather_text = [
            f"Temperature: {weather_data['temperature']}",
            f"Feels Like: {weather_data['feels_like']}",
            f"Humidity: {weather_data['humidity']}",
            f"Wind Speed: {weather_data['wind_speed']}",
            f"Description: {weather_data['description'].split()[0]}"
        ]
    else:
        weather_text = [weather_data["error"]]

    # Display weather information
    for i, text in enumerate(weather_text):
        label = weather_font.render(text, True, TEXT_COLOR)
        screen.blit(label, (700 + 10, 550 + 20 + (i * 30)))  # Adjust line spacing

# Function to display weather for the second location (destination)
def weatherTwo(screen, latitude, longitude):
    # Fetch weather data
    weather_data = get_weather_data(latitude, longitude)

    # Set up font and positioning
    weather_font = load_custom_font(24)
    label_font = load_custom_font(32)
    x_position = 970  # Shift right by 240 pixels
    y_position = 550  # Adjust Y position for quadrant

    # Box properties
    box_width, box_height = 240, 180

    # Draw "Destination" label
    destination_label = label_font.render("Destination", True, BLACK)
    screen.blit(destination_label, (x_position + (box_width // 2 - destination_label.get_width() // 2), y_position - 40))

    # Draw the weather box with a grey border
    pygame.draw.rect(screen, BORDER_COLOR, (x_position - 2, y_position - 2, box_width + 4, box_height + 4), border_radius=10)
    pygame.draw.rect(screen, BACKGROUND_COLOR, (x_position, y_position, box_width, box_height), border_radius=10)

    # Render weather data
    if "error" not in weather_data:
        weather_text = [
            f"Temperature: {weather_data['temperature']}",
            f"Feels Like: {weather_data['feels_like']}",
            f"Humidity: {weather_data['humidity']}",
            f"Wind Speed: {weather_data['wind_speed']}",
            f"Description: {weather_data['description']}"
        ]
    else:
        weather_text = [weather_data["error"]]

    # Display weather information
    for i, text in enumerate(weather_text):
        label = weather_font.render(text, True, TEXT_COLOR)
        screen.blit(label, (x_position + 10, y_position + 20 + (i * 30)))  # Adjust line spacing
 