#!/usr/bin/env python3

"""
List all documents in the given MongoDB collection.

:param mongo_collection: The PyMongo collection object.
:return: A list of all documents in the collection.
"""

def list_all(mongo_collection):
    """ List all documents in the given MongoDB collection. """
    cursor = mongo_collection.find()
    return [doc for doc in cursor]
