def solution(my_string, overwrite_string, s):
    m = my_string[:s]
    o = overwrite_string
    answer = m + o + my_string[s+len(o):]
    return answer