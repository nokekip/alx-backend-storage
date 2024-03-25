#!/usr/bin/env python3

"""
Insert a new document into the given MongoDB collection based on kwargs.

:param mongo_collection: The PyMongo collection object.
:param kwargs: Keyword arguments representing fields and values for the new document.
:return: The _id of the newly inserted document.
"""

def insert_school(mongo_collection, **kwargs):
    """ Insert a new document into the given MongoDB collection based on kwargs. """
    new_school = mongo_collection.insert_one(kwargs)
    return new_school.inserted_id
