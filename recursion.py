def sum_nums(nums):
    if not nums:
        return 0
    else:
        return nums[0] + sum_nums(nums[1:])


def find_amount_of_elements(nums: list):
    if not nums:
        return 0
    else:
        return 1 + find_amount_of_elements(nums[1:])


def find_max_element(nums: list):
    if find_amount_of_elements(nums) == 1:
        return nums[0]
    else:
        return nums[0] if nums[0] > find_max_element(nums[1:]) else find_max_element(nums[1:])


print(sum_nums([3, 3, 4, 7, 9, 1]))
print(find_amount_of_elements([3, 6, 4, 9, 12, 5, 9]))
print(find_max_element([3, 6, 4, 9, 12, 5, 9]))