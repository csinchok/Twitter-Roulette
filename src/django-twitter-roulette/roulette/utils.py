def calculate_luck(my_bullet_score, avg_bullet_score, total_votes):
    if (abs(avg_bullet_score - my_bullet_score) < (0.1 * total_votes)):
        # you're run-of-the-mill; but in an odd twist of fate (actually, poor
        # mathematics), this is the least-likely modifier to receive
        return 1.0
    if (my_bullet_score < avg_bullet_score):
        # you're below average; may Darwin have mercy on your soul
        return 1.5
    elif (my_bullet_score > avg_bullet_score):
        # you're above average; you parents must be proud
        return 0.5
    else:
        # should never get here
        return 1.0

