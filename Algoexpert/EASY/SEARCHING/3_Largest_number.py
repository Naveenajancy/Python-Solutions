def ThreeLargestNumber(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
               # print(f"I : J {array[i], array[j]}")
    return array[-3:]



#input = [10, 100, 1, 89, 4]
#input = [-25,-13,-1,0,100,3,6,21,1,4,5]
#input  = [-12, -100, -20, -1, -2]
#input = [10,11,11,10]
#print(f"{ThreeLargestNumber(input)}")
for i in range(1):
    print (i)