def custom_len(input_list):
    """custom_len(input_list) imitates len(input_list)"""
    i = 0 #doesn't have to start at zero. 
    for item in input_list:
    	print input_list[i]
    	i += 1 # This function is the counter
    return i 

input_list = [9,8,7,6,5,4,3,2,1]

custom_len(input_list)
