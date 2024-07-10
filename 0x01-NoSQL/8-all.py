#!/usr/bin/env python3
"""
Pymongo operations and functions
"""


def list_all(mongo_collection):
    ''' Lists all docs in mongo collectiom'''
    docs = mongo_collection.find()
    return list(docs)
