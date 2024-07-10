#!/usr/bin/env python3
"""
Pymongo operations and functions
"""
from pymongo import MongoClient


def log_stats():
    """
    Nginx logs stored
    """

    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    col = db.nginx

    total_logs = col.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    count_method = {method: col.count_documents({"method": method})
                    for method in methods}

    check_status = col.count_documents(
        {"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {count_method[method]}")
    print(f"{check_status} status check")


if __name__ == "__main__":
    log_stats()
