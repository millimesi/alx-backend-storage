#!/usr/bin/env python3
"""Chaching using redis"""
import redis
import uuid
from functools import wraps
from typing import Union, Optional, Callable


def replay(method: Callable):
    """
    show history
    """

    kinputs = f"{method.__qualname__}:inputs"
    koutputs = f"{method.__qualname__}:outputs"

    inputs = self._redis.lrange(kinputs, 0, -1)
    outputs = self._redis.lrange(koutputs, 0, -1)

    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for input_data, output_data in zip(inputs, outputs):

        input_str = input_data.decode('utf-8')
        output_str = output_data.decode('utf-8')

        print(f"{method.__qualname__}(*{input_str}) -> {output_str}")


def call_history(method: Callable) -> Callable:
    """
    store
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        kinputs = f"{method.__qualname__}:inputs"
        koutputs = f"{method.__qualname__}:outputs"
        self._redis.rpush(kinputs, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(koutputs, output)
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    counter methods
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = f"{method.__qualname__}"
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Initialize the Redis client and store it as a private variable
        Also flush the Redis database
        """
        self._redis = redis.Redis(host='localhost', port=6379, db=0)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, int, float, bytes]) -> str:
        """
        stores the data
        """
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, int, float, bytes]:
        """
        get data from Redis
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        get string from Redis
        """
        return self.get(key, fn=lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        get int from Redis.
        """
        return self.get(key, fn=int)
