#!/usr/bin/env python3

""" Cache implementation with Redis"""

import redis
import uuid
from typing import Union


UnionOfTypes = Union[str, int, float, bytes]


class Cache:
    """" class to manage a cache """
    def __init__(self):
        """"
        Initialize the Cache object and flush the Redis database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: UnionOfTypes) -> str:
        """
        Store the input data in Redis using a random key.
        """
        self._key = str(uuid.uuid4())
        self._redis.set(self._key, data)
        return self._key
