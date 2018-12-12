from functools import reduce

### Using division
def multiply(arr):
    newArr=[]
    product = 1
    for num in arr:
        product = product * num
    for num in arr:
        newArr.append(int(product/num))
    return newArr

print(multiply([1,2,3,4,5]))

### Not using division
def multiply_without_division(arr):
    arrCopy=arr[:]
    newArr=[]
    for num in arr:
        arrCopy.remove(num)
        newArr.append(reduce(lambda a, b : a*b, arrCopy))
        arrCopy=arr[:]
    return newArr

print(multiply_without_division([1,2,3,4,5]))