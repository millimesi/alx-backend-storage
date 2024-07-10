#!/usr/bin/env python3
"""
Pymongo operations and functions
"""


def schools_by_topic(mongo_collection, topic):
    """Read docs by filter"""
    return list(mongo_collection.find({"topics": topic}))
