from bs4 import BeautifulSoup

try:
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    table = soup.find("table")
    if table is None:
        raise ValueError("Jadval topilmadi!")

    rows = table.find("tbody").find_all("tr")

    weather_data = []

    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 3:
            continue

        day = cols[0].text.strip()
        temp_text = cols[1].text.strip().replace("°C", "")
        
        try:
            temp = int(temp_text)
        except ValueError:
            print(f"Xato: {day} kunining harorat ma'lumotini o‘qib bo‘lmadi: '{temp_text}'")
            continue

        condition = cols[2].text.strip()
        weather_data.append((day, temp, condition))

    for day, temp, condition in weather_data:
        print(f"{day}: {temp}°C, {condition}")

    if weather_data:
        max_temp = max(weather_data, key=lambda x: x[1])
        print(f"\nEng issiq kun: {max_temp[0]} ({max_temp[1]}°C)")

        sunny_days = [day for day, temp, condition in weather_data if condition == "Sunny"]
        print(f"Quyoshli kunlar: {', '.join(sunny_days) if sunny_days else 'Yo‘q'}")

        avg_temp = sum(temp for _, temp, _ in weather_data) / len(weather_data)
        print(f"O'rtacha harorat: {avg_temp:.2f}°C")
    else:
        print("Ma'lumotlar mavjud emas.")

except FileNotFoundError:
    print("Xato: 'weather.html' fayli topilmadi!")
except Exception as e:
    print(f"Kutilmagan xato: {e}")
