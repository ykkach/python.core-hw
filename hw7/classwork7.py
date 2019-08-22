import pyowm

owm = pyowm.OWM('203736c864231d379598ef7633bee76b')

c=input("Write your city:")
observation = owm.weather_at_place(c)
w = observation.get_weather()

temp = w.get_temperature('celsius')['temp'] # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
wind = w.get_wind()['speed'] # {'speed': 4.6, 'deg': 330}
hum = w.get_humidity() # 87

print('For now in', c ,'is', w.get_detailed_status() ) 
print("The temperature in", c ,"is" , temp , "degrees Celsius.")
print(" The speed of wind is", wind , "meters per second.")
print(" The percentage of humidity in the air is" , hum , "% .")

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)

################

# import random

# ranval = random.randint(0,100)
# input_num=int(input('Input any number:'))
# if input_num in range(0,100):
#     while input_num != ranval:
#         if input_num < ranval:
#             print('Your number is less than ')
#         print('Your number is greater than ')
#         input_num=int(input('Input another number'))
#     else: print("You win the game")
# input_num=input('Error. Your number must be in range of 1 to 100! Please enter a number:')

############

from math import *
def crc():
    r = float(input("Input radius: "))
    print("Square={}".format(PI * r**2))