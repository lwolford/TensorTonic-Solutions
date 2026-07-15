def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    hits = 0
    for i in range(len(recommendations)):
        common_items = list(set(recommendations[i][:k]) & set(ground_truth[i]))
        if len(common_items) > 0:
            hits += 1
    return hits / len(recommendations)
    # Write code here