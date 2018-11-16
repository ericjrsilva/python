def build_bst(my_list):
  if len(my_list) == 0:
    return "No Child"
  
  middle_idx = len(my_list) // 2
  middle_value = my_list[middle_idx]
  
  print("Middle index: " + str(middle_idx))
  print("Middle value: " + str(middle_value))
  
  left_half_of_list = my_list[:middle_idx]
  right_half_of_list = my_list[middle_idx + 1:]
  
  tree_node = {
    "data": middle_value, 
    "left_child": build_bst(left_half_of_list),
    "right_child": build_bst(right_half_of_list)
  }
  
  return tree_node

sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)
