

def linear_search(array,number_to_search):
    length = len(array)
    mid = (length)//2
    if(number_to_search == array[mid]):
        print(array[mid],'is found')
    elif(number_to_search < array[mid]):
        linear_search(array[0:mid],number_to_search)
    elif(number_to_search > array[mid]):
        linear_search(array[mid:length],number_to_search)


linear_search([1,2,3,4,5,6,70,8,9],70)
