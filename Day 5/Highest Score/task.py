student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

def my_sum(nums):
    total = 0
    for num in nums:
        total += num
    return total

def my_min(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

def my_max(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

total_score = my_sum(student_scores)
smallest_num = my_min(student_scores)
largest_num = my_max(student_scores)

print(total_score)
print(f"Smallest score is: {smallest_num}")
print(f"Largest score is: {largest_num}")