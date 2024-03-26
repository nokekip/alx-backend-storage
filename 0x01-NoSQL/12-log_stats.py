#!/usr/bin/env python3

""" provides stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient


def log_stats():
    """ Prints the log stats in nginx collection """
    con = MongoClient('mongodb://localhost:27017')
    collection = con.logs.nginx

    print(f"{collection.count_documents({})} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for req in methods:
        print('\tmethod {}: {}'.format(req,
              collection.count_documents({'method': req})))

    print('{} status check'.format(collection.count_documents(
          {'method': 'GET', 'path': '/status'})))


if __name__ == "__main__":
    log_stats()
