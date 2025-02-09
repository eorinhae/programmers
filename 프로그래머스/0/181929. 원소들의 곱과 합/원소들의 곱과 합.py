def solution(num_list):
    multiply = 1
    for i in num_list:
        multiply *= i
    if multiply < (sum(num_list))**2:
        return 1
    else:
        return 0