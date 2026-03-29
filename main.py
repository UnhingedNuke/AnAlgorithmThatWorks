#  Title:   Main
#  Desc:    This is literally the main class of this object oriented nonsense
#  Author:  Angela Louise Trainor
#  Date:    03/28/2026

from models import User, Post
from datetime import datetime, timedelta
from candidate_generator import generate_candidates
from ranker import FeedRanker

''' 
HOW 2 INTEGRATE
  Replace this section with:
 - API request handler (FastAPI / Flask) <- Need to look at stack overflow
 - User auth system          <- also stack
 - Database queries          <- all these need defaulto versions of each /w plugins from stack... maybe chat or grok... idk yet.
 - External API calls (Bluesky, etc.)
 '''

user = User(   # This is my sad little test user
    id="u1",
    following=["u2", "u3"],
    interests=["ai", "tech"]
)

posts = [    # Tester posts are here in this weird array thingy
    Post("p1", "u2", "AI is crazy", datetime.utcnow() - timedelta(minutes=2), 10, 5, 3, "ai"),
    Post("p2", "u4", "Random meme", datetime.utcnow() - timedelta(hours=5), 100, 20, 50, "fun"),
    Post("p3", "u3", "New tech release", datetime.utcnow() - timedelta(minutes=10), 5, 2, 1, "tech"),
    Post("p4", "u5", "Politics post", datetime.utcnow() - timedelta(hours=1), 200, 80, 100, "news"),
]    

# FEED PIPELINE
candidates = generate_candidates(user, posts)    # Step 1: Candidate generation

ranker = FeedRanker()                            # Step 2: Ranking
feed = ranker.rank(user, candidates)

for post in feed:                                # Step 3: Output
    print(f"{post.id}: {post.content}")
