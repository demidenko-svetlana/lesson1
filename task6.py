weather = {
    "city": "Moscow",
    "temperature": 20
}
print(weather["city"])
weather["temperature"] = weather["temperature"] - 5
#print(weather)
#print(weather.get("country"))
#print(weather.get("country","Russia")) # не меняется словарь,просто устанавливается дефолтно, но не добавляет
weather.update({
    "country":"Russia"
})
weather["district"] = "South"
weather["date"] = "27.05.19"
print(len(weather))