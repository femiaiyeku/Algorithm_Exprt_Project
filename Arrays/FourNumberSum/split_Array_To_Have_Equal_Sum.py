def ArrayChallenge(arr):
  """
  Takes the array of integers stored in arr which will always contain an even amount of integers
  and determines how they can be split into two even sets of integers each so that both sets add up to the same number,
  if this is impossible return -1. If its possible to split the array into two sets , then return a string representation of the first set followed by the second set
  with each integer separated by a comma and both sets sorted in ascending order. The set that goes first is the set with smallest first integer.
  For example if arr is [16, 22, 35, 8, 20, 1, 21, 11] , then your program should output 1, 11,20, 35, 8, 16, 21, 22
  """

  n = len(arr)
  if n % 2 != 0:
    return -1

  sum_all = sum(arr)
  target_sum = sum_all // 2

  def helper(arr, target_sum, start, end):
    if start == end:
      if sum(arr) == target_sum:
        return arr
      else:
        return []

    arr_left = helper(arr[start + 1:], target_sum, start + 1, end)
    if arr_left:
      return arr_left + [arr[start]]

    arr_right = helper(arr[start:end - 1], target_sum, start, end - 1)
    if arr_right:
      return [arr[end - 1]] + arr_right

    return []

    arr = sorted(arr)
    arr_left = helper(arr, target_sum, 0, n // 2)
    if arr_left:
        arr_right = [x for x in arr if x not in arr_left]
        return ','.join([str(x) for x in arr_left]) + ',' + ','.join([str(x) for x in arr_right])
    else:
        return -1
    