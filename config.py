#  Title:   config.py
#  Desc:    Lil bit of smexy matrixy stuff going on around here...
#  Author:  Angela Louise Trainor
#  Date:    03/28/2026

WEIGHTS = {                # Core ranking weights
    "like": 0.25,
    "reply": 0.35,
    "repost": 0.25,
    "dwell": 0.15
}

BOOSTS = {                  # Boost values
    "close_friend": 0.3,
    "recent_post": 0.2,
    "niche": 0.5            <- Weights posts and alligns you with ppl interested in those things too.
    "positivity": 0.4       <- If makes ppl happy, or weighed as positive, goes up.
    "news": 0.6             <- If relevant to news cycle, include in algo
    "locale": 0.1           <- If in region, such as fun activities, include.
}
