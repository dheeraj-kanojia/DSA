
################### Minimum waiting time ######################

def min_wat_tm(arr):
    arr = sorted(arr)
    total = 0
    n = len(arr)
    for i in range(0,n-1):
        total += arr[i] * (n-1-i)
    return total

print(min_wat_tm([3,2,1,2,6]))



##################### Class Photograph #######################


def class_photo(arr1, arr2, backrow_color):

    red = sorted(arr2)
    blue = sorted(arr1)


    for i in range(0 ,len(red)):
        red_val = red[i]
        blue_val = blue[i]
        if backrow_color == "Red":
            if red_val <= blue_val:
                return False
        else:
            if blue <= red_val:
                return False
    return True
