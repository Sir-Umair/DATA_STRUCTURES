# l=[i for i in range(4)]
# print(l)
# marks=[]
# l = int(input("ENTER THE NUMBER OF LENGHT: "))
# for i in range(l):
#     K=int(input("ENTER MARKS: "))
#     marks.append(K)
# print(marks)

L=[3,4,5,6,7,8,9,12,1,13,45,67,88]
print(L[0:9:3])
L.sort()
L.reverse()
print(L.count(3))
L.pop(7)
L.insert(12,8)
print(L)