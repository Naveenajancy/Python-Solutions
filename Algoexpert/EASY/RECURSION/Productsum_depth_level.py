#O(n) time number of elements including subarray elements
#O(d) where d is the depth level of subarray of special array

def productSum(array, multiplier=1):
    #multiplier = 1
    sum = 0
    for element in array:
        if type(element) is list:
            print(f"element is list {element} ")
            sum += productSum(element, multiplier+1)
            print(f"list sum {sum}")
        else:
            sum += element
            print(f" int : {element} sum {sum} int multiplier {multiplier}" )

    print(f"I am returning  {sum}*{multiplier}={sum * multiplier}")
    return sum * multiplier

            #print(f"depth dict {depth_dict}")

        #print(f"element {element} and type {type(element)}")

#inp = [1,2,[5, -1],6, 7, [12,[13,[10]]]]
inp = [[[[5]]]]

output = productSum(inp, multiplier=1)
print(f"output {output}")
