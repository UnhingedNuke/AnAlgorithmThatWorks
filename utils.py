#  Title:   utils.py
#  Desc:    Time Sensitive Much? What the hell?!?
#  Author:  Angela Louise Trainor
#  Date:    03/28/2026

from datetime import datetime
import math

def recency_boost(post):
    hours_old = (datetime.utcnow() - post.timestamp).total_seconds() / 3600
    return max(0, 1 - hours_old / 48)

def virality_boost(post):
    return math.log(1 + post.reposts + (2 * post.replies))

def is_recent(post):
    minutes_old = (datetime.utcnow() - post.timestamp).total_seconds() / 60
    return minutes_old < 5
