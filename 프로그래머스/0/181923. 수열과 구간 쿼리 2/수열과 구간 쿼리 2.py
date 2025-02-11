def solution(arr, queries):
    answer = []
    
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
        greater_than_k = []        
        sliced_arr = arr[s:e+1]
        
        for i in sliced_arr:
            if i > k:
                greater_than_k.append(i)
                
        if not greater_than_k:
            answer.append(-1)
        else:
            answer.append(min(greater_than_k))
            
    return answer