#!/usr/bin/env python3
'''task
'''


def list_all(mongo_collection):
    '''Lists all documents
    '''
    return [doc for doc in mongo_collection.find()]
