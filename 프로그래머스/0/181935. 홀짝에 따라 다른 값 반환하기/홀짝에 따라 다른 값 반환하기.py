def solution(n):
    answer = 0
    find = []
    if n%2!=0:
        for i in range(1,n+1):
            find.append(i)
        for j in find[:n+1:2]:
            answer += j
    elif n%2==0:
        for i in range(2,n+1):
            find.append(i)
        for j in find[:n+1:2]:
            answer += j*j
    return answer