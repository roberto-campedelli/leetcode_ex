#1 - Two Sum
def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [i, d[target - n]]
        d[n] = i

if __name__ == "__main__":
    nums = [10,2,3,4,5,12,43]
    target = 15
    print(twoSum(nums, target))
    