def is_jolly_jump(nums):
  diff=[]
  for i in range(len(nums)-1):
    diff.append(abs(nums[i]-nums[i+1]))
    
  ans = 1
  for j in range(1,len(nums)):
    if j not in diff:
      ans = 0
  if ans == 0:
    return False
  else:
    return True

nums = [1,4,2,3]
print(is_jolly_jump(nums))