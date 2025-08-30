n = int(input("Enter a number "))
def myfunction1(n):
    if n<=0:
        return
    for i in range(n+1):
        print("Codingal")
    myfunction1(n/2)
    myfunction1(n/3)
myfunction1(n)
print("Time complexity is O(n)")
print("space complexity is O(log n)")
print("Recurrence relation is T(n)=T(n/2)+T(n/3)+O(n)")

print()
def myfunction2(n):
    if n<=1:
        return
    print("Codingal")
    myfunction2(n-1)
myfunction2(n)
print("Time complexity is O(n)")
print("space complexity is O(n)")
print("Recurrence relation is T(n)=T(n-1)+O(1)")
