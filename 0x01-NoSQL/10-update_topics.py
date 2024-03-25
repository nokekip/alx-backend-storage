#!/usr/bin/env python3

"""
Change all topics of a school document based on the school name.

:param mongo_collection: The PyMongo collection object.
:param name: The name of the school to update.
:param topics: The list of topics to set for the school.
"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of a school document based on the school name.
    """
    mongo_collection.update_many(
        {"name": name}, {"$set": {"topics": topics}}
        )
