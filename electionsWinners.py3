def electionsWinners(votes, k):
    highest = max(votes)
    if k == 0:
        counter = votes.count(highest)
        if counter == 1:
            return 1
        return 0
    return len([vote for vote in votes if vote + k > highest])
===============================
def electionsWinners(votes, k):
    highest = max(votes)
    return int(votes.count(highest) == 1) if k == 0 else len([vote for vote in votes if vote + k > highest])
