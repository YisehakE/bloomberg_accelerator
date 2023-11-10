
def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """

    start, end, curr_sum = 0
    min_len = float("inf")

    while end < len(nums):
        curr_sum += nums[end]
        end += 1

        while start < end and curr_sum >= target:
            min_len = min(min_len, end - start)

            curr_sum -= nums[start]
            start += 1
    return 0 if min_len == float("inf") else min_len


''' TEST CASES '''