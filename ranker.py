#  Title:   ranker.py
#  Desc:    This is the judgy bitch of this shitty ass program
#           it judges the content so you don't have to.
#  Author:  Angela Louise Trainor
#  Date:    03/28/2026

from config import WEIGHTS, BOOSTS
from features import extract_features, predict_engagement
from utils import recency_boost, virality_boost, is_recent


class FeedRanker:

    def __init__(self):
        pass

    def score_post(self, user, post):
        features = extract_features(user, post)
        preds = predict_engagement(features)

        base_score = (
            WEIGHTS["like"] * preds["like"] +
            WEIGHTS["reply"] * preds["reply"] +
            WEIGHTS["repost"] * preds["repost"] +
            WEIGHTS["dwell"] * preds["dwell"]
        )

        score = base_score                   # Add boosts
        score += recency_boost(post)         # Recency
        score *= (1 + virality_boost(post))  # Virality

        if post.author_id in user.following: # Close friend boost
            score += BOOSTS["close_friend"]

        if is_recent(post):                  # Real-time injection
            score += BOOSTS["recent_post"]

        return score

    def rank(self, user, posts):
        scored = [(post, self.score_post(user, post)) for post in posts]
        ranked = sorted(scored, key=lambda x: x[1], reverse=True)

        return [p[0] for p in ranked]
