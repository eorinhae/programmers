def solution(ineq, eq, n, m):
    answer = 0
    if eq == "!":
        if ineq == ">":
            if n>m:
                answer = 1
            else:
                answer = 0
        elif ineq == "<":
            if n<m:
                answer = 1
            else:
                answer = 0
    elif eq == "=":
        if ineq == ">":
            if n>=m:
                answer = 1
            else:
                answer = 0
        elif ineq == "<":
            if n<=m:
                answer = 1
            else:
                answer = 0
    return answer