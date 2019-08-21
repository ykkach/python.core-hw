# import pyowm

# owm = pyowm.OWM('203736c864231d379598ef7633bee76b')

# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Search for current weather in Lviv (Ukraine)
# observation = owm.weather_at_place('Lviv,UA')
# w=str(input('Enter your town: ', end=''))
# w = observation.get_weather()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>

# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)

from random import *

ranval = random.randint(0,100)
input_num=int(input('Input any number:'))
if input_num < 1 and input_num > 100:
    input_num=input('Error. Your number must be in range of 1 to 100! Please enter a number:')
else:
    while input_num != ranval:
        if input_num < ranval:
            print('Your number is less than ', ranval)
        print('Your number is bigger than ', ranval)
    else: print("You win the game")

