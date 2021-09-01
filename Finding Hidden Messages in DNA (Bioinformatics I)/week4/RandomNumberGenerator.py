import random


def binary_search(needle, nums):
    left, right = 0, len(nums) - 1
    pos = right

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > needle:
            pos = mid
            right = mid - 1
        else:
            left = mid + 1

    return pos


def get_random_number(probabilities):
    total = sum(probabilities)
    normalized = [prob / total for prob in probabilities]

    run_sum = 0
    # cum_sum = [(run_sum := run_sum + prob) for prob in probabilities]
    cum_sum = []
    for prob in normalized:
        run_sum += prob
        cum_sum.append(run_sum)

    needle = random.random()
    return binary_search(needle, cum_sum)


if __name__ == "__main__":
    from collections import defaultdict

    probabilities = [0.25, 0.25, 0.1, 0.4]
    counts = defaultdict(int)
    for _ in range(100):
        counts[get_random_number(probabilities)] += 1
    print(counts)
