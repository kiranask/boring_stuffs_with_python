from  collections import deque


test_list = [1,2,3,4,5,6,7,8]

# Rotate left by 3

test_list = test_list[3:]+ test_list[:3]
print(test_list)

# Rotate right by 3

test_list = [1,2,3,4,5,6,7,8]
test_list = test_list[-3:] + test_list[:-3 ]
print("list" ,test_list)
test_queue = deque(test_list)
test_queue.rotate(-3)
print("Queue rotate",test_queue )
test_queue = deque(test_list)
test_queue.rotate(3)
print('queue right ',test_queue)


# Python program to right rotate a list by n

# Returns the rotated list
