# Bubble Sorting Algorithm in Python


def bubbleSort(data):
    for element in range(len(data)):
        for eachData in range(1, len(data) - element):
            if data[eachData - 1] > data[eachData]:
                data[eachData - 1], data[eachData] = data[eachData], data[eachData - 1]



# lst = [5,7,9,32,3,5,1,6]
# print(lst)
# bubbleSort(lst)
# print(lst)