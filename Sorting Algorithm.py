def sort_function(data):

    length = len(data)

    for item in range(length):
        for i in range(0, length-item-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                print(f"Unsorted: {data}")
    
    print(f"sorted: {data}")
    

num = [5,4,3,2,1]
print(f"unsorted: {num}")
sort_function(num)