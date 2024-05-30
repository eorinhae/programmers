def solution(code):
    mode = 0
    idx = 0
    ret = ""
    for i in code:
        if i == '1': #code 문자가 1일 때 mode 바꾸기
            if mode == 0: 
                mode = 1
            elif mode == 1:
                mode = 0
        if mode == 0: #mode 값에 따라 ret 추가하기
            if code[idx] != '1' and idx%2==0:
                ret += code[idx]
        elif mode == 1:
            if code[idx] != '1' and idx%2!=0:
                ret += code[idx]
        idx += 1
    answer = ret
    if ret == "":
        answer = "EMPTY"
    return answer