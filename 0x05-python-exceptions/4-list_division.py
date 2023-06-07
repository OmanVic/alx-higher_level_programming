#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for item in range(list_length):
        try:
            new_list.append(my_list_1[item] / my_list_2[item])
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            if item > min((len(my_list_1) - 1), (len(my_list_2)-1)):
                new_list.append(0)
                print("out of range")
        finally:
            if item > max((len(my_list_1) - 1), (len(my_list_2)-1)) or item == max(range(list_length)):
                return new_list
