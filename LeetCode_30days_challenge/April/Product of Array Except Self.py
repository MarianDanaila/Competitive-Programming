def productExceptSelf(nums):
    output = []
    output.append(1)
    for i in range(1, len(nums)):
        output.append(nums[i-1]*output[i-1])
    print(output)
    r = 1
    for i in range(len(nums)-2, -1, -1):
        r *= nums[i+1]
        output[i] *= r
    return output
print(productExceptSelf([1,2,3,4]))