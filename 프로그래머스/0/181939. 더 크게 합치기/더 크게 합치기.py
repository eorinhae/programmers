def solution(a, b):
    ab = str(a)+str(b)
    ba = str(b)+str(a)
    int_ab = int(ab)
    int_ba = int(ba)
    if int_ab >= int_ba:
        answer = int_ab
    elif int_ab < int_ba:
        answer = int_ba
    return answer