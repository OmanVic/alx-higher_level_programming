#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_of_items = 0
    second_sum = 0
    def sum(a, b):
        return a * b
    for item in my_list:
        sum_of_items += sum(*item)
        second_sum += item[1]
    avg = sum_of_items / second_sum
    return avg
