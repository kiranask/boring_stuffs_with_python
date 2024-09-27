list=(my name is kiran "Kiran")
echo ${list[0]}
echo {list[1]}
echo all the values in array ${list[*]}
# To get the length of the array
echo to get length of the array ${#list[*]}
# slicing in bash
echo to get two values ${list[*]:2}