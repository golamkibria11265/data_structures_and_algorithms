test_list = [4,5,[7,8,10,[99,77,[88]]],100]
def recursion(test_list):
    if(88 in [test_list]):
        print("found")
    elif(((type(test_list) is type([])))):
        for x in test_list:
            recursion(x)
recursion(test_list)
