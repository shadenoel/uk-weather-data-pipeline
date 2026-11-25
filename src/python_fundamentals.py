# # # Exercise 1 - Variables and data types

# city = "London"
# temperature = 12.5
# humidity = 82
# wind_speed = 15.3
# is_raining = False
# observation_timestamp = '2026-11-25 15:00:00'

# print(city)
# print(type(city))
# print(temperature)
# print(type(temperature))
# print(humidity)
# print(type(humidity))
# print(wind_speed)
# print(type(wind_speed))
# print(is_raining)
# print(type(is_raining))
# print(observation_timestamp)
# print(type(observation_timestamp))

# # Exercise 2 - Lists

# cities = ["London", "Manchester", "Birmingham", "Edinburgh", "Cardiff"]
# temperatures = [12.5, 9.2, 10.8, 7.4, 11.3]

# print(cities)
# print(temperatures)
# print(type(cities))
# print(type(temperatures))
# print(cities[0])
# print(cities[-1])
# print(temperatures[2])
# print(len(cities))

# cities.append("Bristol")
# temperatures.append(11.8)
# print(cities)
# print(temperatures)
# print(cities.index("Manchester"))

# print(max(temperatures))
# print(min(temperatures))
# print(sum(temperatures))
# print(sum(temperatures)/len(temperatures))

# Exercise 3 - Dictionaries

# weather = {
#     "city": "London",
#     "temperature": 12.5,
#     "humidity": 82,
#     "wind_speed": 15.3,
#     "is_raining": False,
#     "observation_timestamp": '2026-11-25 15:00:00'
# }
# print(weather)
# print(type(weather))
# print(weather["city"])
# print(weather.get("temperature"))

# weather["temperature"] = 13.2
# weather["country"] = "United Kingdom"
# print(weather.keys())
# print(weather.values())
# print(weather.items())
# print(len(weather.items()))
# print("humidity" in weather)
# print(weather.get("pressure"))
# print(weather)

weather_observations = [
    {
        "city": "London",
        "temperature": 12.5,
        "humidity": 82
    },
    {
        "city": "Manchester",
        "temperature": 9.2,
        "humidity": 88
    },
    {
        "city": "Birmingham",
        "temperature": 10.8,
        "humidity": 79
    }
]
print(weather_observations[1]["humidity"])

# Exercise 4 - Loops and conditional logic

for observation in weather_observations:
    print(observation["city"])

for observation in weather_observations:
    print(observation["temperature"])

for observation in weather_observations:
    if observation["temperature"] > 10:
        print(observation["city"])

for observation in weather_observations:
    if observation["humidity"] > 80:
        print(observation["city"])

for observation in weather_observations:
    if observation["temperature"] < 10:
        print(f"{observation['city']} is cold")
    else:
        print(f"{observation['city']} is warm")

weather_observations[0]["temperature_category"] = "warm"
weather_observations[1]["temperature_category"] = "cold"
weather_observations[2]["temperature_category"] = "warm"

print(weather_observations)

test_observations = [{
    "city": "London",
    "temperature": 12.5,
    "humidity": 82
},
{
    "city": "Manchester",
    "temperature": None,
    "humidity": 88
},
{
    "city": "Birmingham",
    "temperature": 10.8,
    "humidity": 79
}
]

for observation in test_observations:
    if observation["temperature"] is None:
        print(f"Warning: Missing temperature for {observation['city']}")