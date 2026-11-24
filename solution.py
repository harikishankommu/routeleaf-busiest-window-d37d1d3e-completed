def busiest_window(deliveries: list[int], k: int) -> int:
    """Return the largest total number of deliveries over any k consecutive days.

    deliveries is a list of daily delivery counts in date order, and k is the
    window length. Bounds: 1 <= k <= len(deliveries) <= 10^5 and
    0 <= deliveries[i] <= 10^4.
    """

    current_sum = 0
    for i in range(k):
        current_sum += deliveries[i]

    max_sum = current_sum
    for i in range(k , len(deliveries)):
        current_sum += deliveries[i] - deliveries[i-k]
        max_sum = max(max_sum,current_sum)

    return max_sum
