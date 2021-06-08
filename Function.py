my_list=[-2,1,2,-10,22,-10]

def list_max(my_list):
    result = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > result:
            result = my_list[i]

    #print(result)
    return result

l1=[-2,1,2,-10,22,-10]
list_max(l1)
