#!/usr/bin/env python3
'''task
'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a new document
    '''
    output = mongo_collection.insert_one(kwargs)
    return output.inserted_id
