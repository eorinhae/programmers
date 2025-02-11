def solution(arr, queries):
    for query in queries:
        s = query[0]
        e = query[1]
        k = query[2]
    
        for i in range(len(arr)):
            if (i >= s and
                i <= e and
                i % k == 0
            ):
                arr[i] +=1
        
    return arr