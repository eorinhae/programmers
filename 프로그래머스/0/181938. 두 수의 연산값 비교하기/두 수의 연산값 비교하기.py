def solution(a, b):
    answer = 0
    compare = 2*a*b
    ab = str(a)+str(b)
    int_ab = int(ab)
    if int_ab >= compare:
        answer = int_ab
    elif int_ab < compare:
        answer = compare
    return answer