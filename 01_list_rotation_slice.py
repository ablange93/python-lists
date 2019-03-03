# rotate list
# no time/space requirements
# return "rotated" version of input list

def rotate(my_list, num_rotations):
  
  # slice into 2x sections
  first_slice = my_list[-num_rotations:]
  second_slice = my_list[:-num_rotations]
  
  # merge into output list
  output_list = first_slice + second_slice 
  
  return output_list

print(rotate(['a', 'b', 'c', 'd', 'e'], 3))


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1), ['f', 'a', 'b', 'c', 'd', 'e'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1) == ['f', 'a', 'b', 'c', 'd', 'e']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2), ['e', 'f', 'a', 'b', 'c', 'd'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2) == ['e', 'f', 'a', 'b', 'c', 'd']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3), ['d', 'e', 'f', 'a', 'b', 'c'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3) == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4), 
['c', 'd', 'e', 'f', 'a', 'b'], rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4) == ['c', 'd', 'e', 'f', 'a', 'b']))
