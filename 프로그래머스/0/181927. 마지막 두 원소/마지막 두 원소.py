def solution(num_list):
    last_one = num_list[-1]
    last_sec = num_list[-2]
    new_element = 0
    if last_one > last_sec:
        new_element = last_one - last_sec
    else:
        new_element = last_one*2
    num_list.append(new_element)
    return num_list