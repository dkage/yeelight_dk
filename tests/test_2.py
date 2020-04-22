from classes.LightBulb import LightBulb
from tests3 import test

new_light = LightBulb()

a = test()

print('here')
print(a)
new_light.fill_data_from_discover(a)
new_light.tcp_connect()
new_light.send_command()
