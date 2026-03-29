#  Title:   features.py
#  Desc:    Superficial bitch class
#  Author:  Angela Louise Trainor
#  Date:    03/28/2026

def extract_features(user, post):
    """
    This is where you put the info on what crap you want the machine to pick up.
    
     AKA:  Convert user + post into model-ready features.

     Replace this with real ML feature pipelines later.
     Hook external APIs here (user embeddings, NLP models, etc.)
    """

    return {
        "user_interest_match": 1 if post.topic in user.interests else 0,
        "engagement": post.likes + post.replies + post.reposts,
    }


def predict_engagement(features):
    """
    Fake prediction model (placeholder)  <- I need to add in stuff...

     Replace with(so many options!!):
    - REST API call to ML service
    - Local PyTorch / TensorFlow model
    """

    base = features["engagement"] / 100

    return {
        "like": min(1, base * 0.8),
        "reply": min(1, base * 0.6),
        "repost": min(1, base * 0.7),
        "dwell": min(1, base * 0.9)
    }
