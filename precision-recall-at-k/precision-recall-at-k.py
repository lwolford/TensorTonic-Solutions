def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    top_k_intersect = list(set(top_k) & set(relevant))

    precision_at_k = len(top_k_intersect) / k
    recall_at_k = len(top_k_intersect) / len(relevant)

    return [precision_at_k, recall_at_k]