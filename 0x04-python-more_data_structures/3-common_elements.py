#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_element = []
    for items in set_1:
        for item in set_2:
            if items == item:
                common_element.append(item)
    return common_element
