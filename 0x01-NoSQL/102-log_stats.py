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
    
    print('IPs:')
    ips = collection.aggregate([
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    count = 0
    for ip in ips:
        if count == 10:
            break
        print('\t{}: {}'.format(ip.get('_id'), ip.get('count')))
        count += 1
        

if __name__ == "__main__":
    log_stats()
