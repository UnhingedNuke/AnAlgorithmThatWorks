#  Title:   candidate_generator.py
#  Desc:    Coming to call you about your cars extended warranty
#            you need to replace the imaginary ppl with ppl this one
#            choses to shine in the sun of the cyberworld n stuff...
#
#                    TOUCH. GRASS. PLEAAASSEEEE.
#
#  Author:  Angela Louise Trainor
#  Date:    03/28/2026

def generate_candidates(user, all_posts):
    """
    Pull candidate posts for ranking... chosen one.

    Replace this bullshit with:
    - Database queries (PostgreSQL, MongoDB)              <- much fancy
    - Graph API calls                                     <- meca fancy
    - External feed APIs (Bluesky AT Protocol, etc.)      <- too much shit
    """

    candidates = []

    for post in all_posts:
        if post.author_id in user.following:                # Include followed users
            candidates.append(post)

        elif post.likes + post.replies + post.reposts > 50: # Include trending posts (simple logic for now)
            candidates.append(post)

    return candidates
