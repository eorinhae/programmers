def solution(l, r):
    answer = [-1]
    if (l > 555555 or r < 5):
        return answer
    
    #0과 5로만 이루어진 정수 리스트 만들기
    zeroFive = [] #0과 5로만 이루어진 정수 리스트
    for i in range(64): #0~63
        bin = format(i,'b') #이진 변환
        bin = bin.replace('1', '5') #'0'을 '5'로 바꿈
        zeroFive.append(int(bin)) #문자열을 정수로 바꾸고 리스트에 추가
    
    #l, r 범위 구하기
    l_digit = len(str(l)) #자릿수 구하기
    r_digit = len(str(r))
    if r_digit == 7:
        endIn = 63 #zeroFive 리스트의 마지막 원소 인덱스
    else:
        endIn = 2**(r_digit) - 1 #같은 자릿수 원소 중 마지막 원소 인덱스
    startIn = 2**(l_digit-1) #같은 자릿수 원소 중 첫번째 원소 인덱스
    
    #l 이상이면서 가장 가까운 인덱스 찾기
    for item in zeroFive[startIn:]:
        if l <= item:
            startIn = zeroFive.index(item)
            break
            
    #r 이하이면서 가장 가까운 인덱스 찾기
    for item in zeroFive[endIn:0:-1]: #endIn부터 1번까지 역순으로 순회
        if r >= item:
            endIn = zeroFive.index(item)
            break
    #리턴
    if startIn <= endIn:
         answer = zeroFive[startIn:endIn+1]
    
    return answer