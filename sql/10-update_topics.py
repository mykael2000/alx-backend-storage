#!/usr/bin/env python3
'''task
'''


def update_topics(mongo_collection, name, topics):
    '''Changes all topics of a collection
    '''
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
