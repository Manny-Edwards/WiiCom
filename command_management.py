import redis
import threading



class CommandManager:

    def __init__(self, commands):
        self.r = redis.Redis()
        self.lock = threading.RLock()


    def new_message(self, message, piname):
        with self.lock:
            key = message
            self.r.set(key, piname)

    def get_pi_name(self, message):
            return self.r.get(message)

    def delete_all(self):
        self.r.flushall()

    def get_command_list(self):
        return self.r.keys()

