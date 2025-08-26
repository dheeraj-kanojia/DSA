
################### Minimum waiting time ######################

def min_wat_tm(arr):
    arr = sorted(arr)
    total = 0
    n = len(arr)
    for i in range(0,n-1):
        total += arr[i] * (n-1-i)
    return total

# print(min_wat_tm([3,2,1,2,6]))
#

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


################# Tandem Bicycle #################


def tandem(arr1, aar2):

    red = sorted(arr1)
    blue = sorted(aar2, reverse= True)

    for i in range(0, len(red)):
        red_val = red[i]
        blue_val = blue[i]
        max_val = max(red_val,blue_val)
        red[i] = max_val
    return sum(red)



# tandem([5, 5, 3, 9, 2],[3, 6, 7, 2, 1])


########################### Optimal Freelancing #####################

def optimal_freelance(optimal_val):
    assigned_date = [False] * 7
    total_pay = 0
    sorted_payment = sorted(optimal_val, key=lambda x: (-x['payment']))
    for i in sorted_payment:
        days = i["deadline"]
        payment = i["payment"]
        latest_day = min(days,7)
        for day in range(latest_day,0,-1):
            if assigned_date[day - 1] != "Taken":
                assigned_date[day - 1] = "Taken"
                total_pay += payment
                break
    return total_pay


print(optimal_freelance([
    {"deadline": 1, "payment": 1},
    {"deadline": 2, "payment": 2},
    {"deadline": 2, "payment": 2},
    {"deadline": 7, "payment": 1},
    {"deadline": 4, "payment": 5},
    {"deadline":3, "payment": 4},

]))