import sqlite3
import hashlib
from datetime import datetime
def get_hash(passwd):
    return hashlib.sha512(passwd.encode('utf-8')).hexdigest()


def get_current_time():
    return datetime.now()
