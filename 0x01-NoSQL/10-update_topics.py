#!/usr/bin/env python3
"""
Pymongo operations and functions
"""


def update_topics(mongo_collection, name, topics):
    '''update doc'''
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
        )
