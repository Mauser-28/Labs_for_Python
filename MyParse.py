import requests 

def get_weather (cityName: str, api: str):
    variationLimit:int = 4 #int(input("enter limit of variations "))

    geoParams = {
        "q": cityName,
        "limit": variationLimit,
        "appid": api 
    }

    try:
        geoDataCall = requests.get("http://api.openweathermap.org/geo/1.0/direct", params=geoParams, timeout=(3,8))
        geoData = geoDataCall.json()
        print("\nнайдена информация о следующих городах:\n")
        for i in range(min(len(geoData), variationLimit)):
            item = geoData[i]
            name = item.get("name", "N/A")
            country = item.get("country", "N/A")
            state = item.get("state", "N/A")
            
            local_names = item.get("local_names", {})
            ru_name = local_names.get("ru", "N/A")

            print(f"{i + 1}.", 
                  f"{name} ({ru_name})", 
                  f"Страна: {country}", 
                  f"Область(штат): {state}", 
                  sep = "\n", 
                  end = "\n\n")

        print("\nНа данный момент выбор пользователю предосталяться не будет, потому на данный момент выбирается наиболее вероятный вариант\n")

        weatherParams = {
            "units": "metric",
            "lat": geoData[0]["lat"],
            "lon": geoData[0]["lon"],
            "appid": api
        }
        weatherDataCall = requests.get("https://api.openweathermap.org/data/2.5/weather", params=weatherParams)
        weatherData = weatherDataCall.json()
        
        city_name = weatherData.get('name', 'N/A')
        sys_data = weatherData.get('sys', {})
        country = sys_data.get('country', 'N/A')
        
        main_data = weatherData.get('main', {})
        temp = main_data.get('temp', 'N/A')
        feels_like = main_data.get('feels_like', 'N/A')
        humidity = main_data.get('humidity', 'N/A')
        pressure = main_data.get('pressure', 'N/A')
        
        wind_data = weatherData.get('wind', {})
        wind_speed = wind_data.get('speed', 'N/A')
        
        weather_list = weatherData.get('weather', [{}])
        description = weather_list[0].get('description', 'N/A') if weather_list else 'N/A'

        print(f"Погода в городе: {city_name} ({country})", 
              f"Состояние:   {description}", 
              f"Температура: {temp}°C (ощущается как {feels_like}°C)", 
              f"Влажность:   {humidity}%", 
              f"Давление:    {pressure} гПа", 
              f"Ветер:       {wind_speed} м/с",
              sep = "\n",
              end = "\n\n")


    except requests.exceptions.Timeout:
        print("После подключения сервер долго не отвечал. Попробуйте сделать запрос позже.")
    except requests.exceptions.ConnectionError:
        print("Не удалось подключиться к серверу.")



if __name__ == "__main__":
    print("\nparser for site openweathermap.org\n")
    get_weather(input("Введите название города "), input("Введите api-ключ ")) #d4f0ee5a4b6fc13984be0d3bee874de8

    