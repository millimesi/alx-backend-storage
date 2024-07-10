#!/usr/bin/env python3
"""
Pymongo operations and functions
"""


def insert_school(mongo_collection, **kwargs):
    '''Inserts doc to the collection'''
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
