# find rotation point 
# No time/space requirements
# return index of "rotation point" element

def rotation_point(rotated_list):
  
  # find rotation point
  minIndexValue = 0
  
  # iterate through,
  for i in range(len(rotated_list)-1):
    if rotated_list[i+1] < rotated_list[minIndexValue]:
      minIndexValue = i+1
    
  # return lowest value's index
  return minIndexValue

#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))

