#encode:UTF-8
def lis(arr):
    arr.reverse()
    n = len(arr)
    m = [0]*n
    for x in range(n-2,-1,-1):
        for y in range(n-1,x,-1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result
 
# arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]

    return finalstr

def sublisttest(arr):
    finalstr=[]
    temp=[]
    start=0
    for i in range(0,len(arr)):
        # print(start)

        if arr[i]>arr[i-1]:
            temp=arr[start:i]
            # print(temp)
            if len(temp)>len(finalstr):
                finalstr=temp[:]
            start=i

        if i==len(arr)-1:
            temp=arr[start:]
            # print(temp)
            if len(temp)>len(finalstr):
                finalstr=temp[:]

    return finalstr

name=input('input:')
print(name.split(" "))
data = map(float, name)
print(list(data))
content='74295176543287654321'
print(sublisttest(content))
# strlist=list(content)
# arr=[]
# for i in strlist:
#     arr.append(int(i))
# # arr.reverse()

# print(lis(arr))