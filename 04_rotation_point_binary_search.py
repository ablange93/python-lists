# find rotation point 
# O(logN) time requirement
# return index of "rotation point" element

def rotation_point(rotated_list):
  
  # set high & low values
  low = 0
  high = len(rotated_list) - 1

	# start while loop
  while low <= high:
    
    # set mid values
    mid = (low + high) // 2
    mid_next = (mid + 1) % len(rotated_list)
    mid_previous = (mid - 1) % len(rotated_list)
    
    # evaluate mid against mid_next & mid_previous
    if rotated_list[mid] < rotated_list[mid_next] and rotated_list[mid] < rotated_list[mid_previous]:
      return mid
    # check if second half after mid is sorted,
    elif rotated_list[mid] < rotated_list[high]:
      # if it is, everything from mid to high is sorted, so set the new high to -1 before mid, then recursivley re-calculate & evalute the new mid
      high = mid - 1
    else:
      # otherwise everything from mid to low is sorted, so set the new low to +1 after mid, the recursivley re-calculate & evalute the new mid
      low = mid + 1

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))
