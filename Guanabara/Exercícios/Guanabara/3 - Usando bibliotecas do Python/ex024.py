city = input('write the city where you from: ').strip()
if city.lower().split()[0].find("santo") >= 0:
    print("Your city start with 'Santo' word")
else:
    print("Your city doesn't start with 'Santo' word")
