# 🌤️ Weather App Documentation

This documentation for my Weather Application, which utilizes the WeatherAPI to fetch meteorological data and uses Qt for the user interface.

## Overview & Functionality

This application is a practical desktop project designed to test API integration, JSON data parsing, image asset caching, and GUI creation using Qt. 

*   **Core Feature:** The user inputs a specific location. Upon submission, the app dynamically extracts the location name, country, and current local time.
*   **Forecast Display:** The application displays the current weather data for today plus a 6-day forward forecast (7 days total). 
*   **Data Optimization:** Because the API's full forecast payload is massive (containing hourly data), the application parses and displays only the essential daily summary: maximum, minimum, and average temperatures, alongside the general weather condition status and corresponding visual icons.

---

## API Architecture

While WeatherAPI offers multiple endpoints (such as `/current.json`, `/search.json`, `/history.json`, and `/alerts.json`), this specific application exclusively implements the **Forecast** method to gather all its required real-time and future data in a single request.

### Implemented API Method
*   **Endpoint:** `/forecast.json`
*   **Purpose:** Used to retrieve both the current local metadata and the upcoming 7-day weather outlook.

### Request Parameters
*   `key` *(Required)*: Your unique WeatherAPI developer key.
*   `q` *(Required)*: The query location parameter, passed dynamically based on the user's city choice (e.g., `q={local}`).
*   `days` *(Optional)*: Set to `7` to fetch today's weather and the 6 subsequent days.
*   `aqi` *(Optional)*: Air Quality Index flag. Set to `no` to keep data payloads light.
*   `alerts` *(Optional)*: Weather alerts flag. Set to `no` since severe alerts are not required for this implementation.

#### Dynamic Request Example:
```python
f"https://api.weatherapi.com/v1/forecast.json?key={api_key}&q={local}&days=7&aqi=no&alerts=no"
```

## Image Asset Management (Icons Cache)

To display weather conditions visually without degrading application performance, the project includes a dedicated component called `icons_manager`.

*   **The Problem:** Each weather state comes with an icon URL from the API. Making a network request to download the image file every single time the UI refreshes would flood the network and slow down the interface.
*   **The Solution (`icons_manager`):**
    *   It extracts the icon asset link from the API's JSON response.
    *   It checks if the image file already exists in a local directory.
    *   **Cache Miss:** If the image is not local, it sends a single HTTP request, downloads the raw binary content of the icon, and saves it locally.
    *   **Cache Hit:** If the image already exists locally, it skips the network entirely.
    *   Finally, it loads the local image file and renders it smoothly inside the Qt application layout.

---

## User Interface (Qt)

The graphical user interface was initially designed visually using **Qt Designer** and subsequently customized through code adjustments.

### Key UI Workflows
*   **Location Lookup:** Handles user selection (e.g., `local = "aveiro"`) and updates the query parameters.
*   **JSON Data Extraction:** Parses the nested JSON response to extract string values for the location name, country, and local time, as well as array data for the 7 forecast days.
*   **Visual Layout:** Organizes text data and pairs them with their locally-cached weather icons across the dashboard.
