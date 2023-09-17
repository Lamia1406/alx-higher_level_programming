#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    weight = 0
    for i in my_list:
        average += i[0] * i[1]
        weight += i[1]
    average /= weight
    return average
