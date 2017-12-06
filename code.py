from flask import Flask, request, Response
import redis
import json

from command_management import CommandManager

wii = CommandManager(redis.Redis())

app = Flask(__name__)


@app.route('/')
def current_inventory():
    return json.dumps({})


@app.route('/post', methods=['POST'])
def postMessage():
    message = request.form['msg']
    piname = request.form['name']
    wii.new_message(message, piname)
    return json.dumps(message)

@app.route('/msg_history')
def getHistory():
    if len(request.args) != 0:
        message = "Invalid search"

        return Response('["msg": "{}"]'.format(message), status=400)

    messages = []
    for message in wii.get_command_list():
        piname = wii.get_pi_name(message).decode("utf-8")
        message = message.decode("utf-8")
        messages.append({message:piname})

    return json.dumps(messages)


#translate back = for messages in wii.get_command_list():
                    #message = message.decode("utf-8")

if __name__ == '__main__':
    app.run(debug=True)