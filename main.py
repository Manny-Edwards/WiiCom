from translate import *
from command_management import *
wii = CommandManager(redis.Redis())

word = trans_to_eng()
r = requests.post('http://192.168.1.142:5000/post', data={'msg':word})


message = ''
for messages in wii.get_command_list():
        message = messages
trans_to_code(list(message.upper()))
