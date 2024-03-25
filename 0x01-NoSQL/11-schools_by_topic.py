#!/usr/bin/env python3

"""
Find all schools that cover the specified topic.

:param mongo_collection: The PyMongo collection object.
:param topic: The topic to search for.
:return: A list of schools covering the specified topic.
"""


def schools_by_topic(mongo_collection, topic):
    """ Find all schools that cover the specified topic. """
    cursor = mongo_collection.find({"topics": topic})
    return [doc for doc in cursor]
