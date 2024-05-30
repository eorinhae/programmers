def solution(a, d, included):
    sum = 0
    for i in range(len(included)):
        if included[i] == True:
            sum += a+i*d
    answer = sum
    return answer