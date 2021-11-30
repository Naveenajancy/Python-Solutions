def log2n(n):
    
    if n>1:
        out = log2n(n/2)
        print(f"recusrion {out}")
        return out + 1
        #print(f"final output{1+out}")
    else:
        return 0

number = 32
print(f"{log2n(number)}")
