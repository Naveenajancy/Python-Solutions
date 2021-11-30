def isValidateSubsequence(array, sequence):
    seqidx = 0
    for value in array:
        if seqidx == len(sequence):
            break
        if sequence[seqidx] == value:
            seqidx += 1
    print(f"seqidx {seqidx} len(sequence) {len(sequence)}")
    return seqidx == len(sequence)





#print(isValidateSubsequence([5,1,22,25,6,-1,8,10], [1,6,-1,10]))

print(isValidateSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[5, 1, -1, 10]))

print(isValidateSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[4, 5, 1, 22, 25, 6, -1, 8, 10]))


#print(isValidateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 6, -1, 8, 10]))

print(isValidateSubsequence([1, 1, 1, 1, 1], [1, 1, 1]))