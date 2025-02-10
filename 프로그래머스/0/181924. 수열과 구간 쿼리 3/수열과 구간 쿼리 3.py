def solution(arr, queries):
    for k in range(len(queries)):
        i = queries[k][0]
        j = queries[k][1]
        arr[i], arr[j] = arr[j], arr[i]
    return arr