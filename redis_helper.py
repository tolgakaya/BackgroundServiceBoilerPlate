import json
import os
import redis
from dotenv import load_dotenv

class RedisHelper:
    def __init__(self):
        load_dotenv()
        self.host = os.getenv('REDIS_HOST')
        self.port = os.getenv('REDIS_PORT', 6379)
        self.db = os.getenv('REDIS_DB', 0)
        self.connection = None

    def open_connection(self):
        self.connection = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    def close_connection(self):
        if self.connection:
            del self.connection
        self.connection = None

    def write_to_list(self, list_name, data):
        if not self.connection:
            raise Exception("No connection available.")
        if isinstance(data, (list, tuple)):
            self.connection.rpush(list_name, *data)
        else:
            self.connection.rpush(list_name, data)

    def write_custom_type(self, key, custom_data, ttl=None):
        if not self.connection:
            raise Exception("No connection available.")
        self.connection.set(key, json.dumps(custom_data))
        if ttl:
            self.connection.expire(key, ttl)

    def read_from_redis(self, key):
        if not self.connection:
            raise Exception("No connection available.")
        data = self.connection.get(key)
        if data:
            return json.loads(data)
        return None

    def set_ttl(self, key, ttl):
        if not self.connection:
            raise Exception("No connection available.")
        self.connection.expire(key, ttl)
