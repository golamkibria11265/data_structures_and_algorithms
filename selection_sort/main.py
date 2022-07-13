number_of_list = [10,5,2,8,7,888,6]

for i in range(len(number_of_list)):
    index_min = i
    for j in range(i+1, len(number_of_list)):
        if(number_of_list[j] < number_of_list[index_min]):
            index_min = j
    number_of_list[i], number_of_list[index_min] = number_of_list[index_min] , number_of_list[i]

print(number_of_list)
