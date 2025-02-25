def find_longest_subarray(A, N, K):
    MaxLen = 0
    Len = 0
    for i in range(N):
        if K % A[i] == 0:
            Len += 1
            MaxLen = max(MaxLen, Len)
        else:
            Len = 0
    return MaxLen