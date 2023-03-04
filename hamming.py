# import random
# import time

# def onlyOne(input):
#     output = []
#     for x in input:
#         if x[1] == 1: output.append(x[0])
#     return output

# times = int(input())
# startList = []
# tiiis = 0

# for x in range(times):
#     startList.append(list((x, random.randint(0, 1))))
# print(str(startList)
# #   .replace(", [", ",\n [")
#     )

# onesList = onlyOne(startList)

# print(str(onesList)
# #   .replace(", [", ",\n [")
#     )

# error = onesList[0]
# for x in onesList:
#     if x == onesList[0]: pass
#     error = x ^ error
# print(error)

# errorsBin = list(str(bin(error).split("b")[1]))
# print(errorsBin)
# print(len(errorsBin))

# for x in errorsBin:
#     print(str(tiiis + 1))
#     print("before " + str(errorsBin))
#     errorsBin.pop(0)
#     print(x)
#     if x == "1": 
#         index = "0b1"
#         for i in range(len(errorsBin)):
#             index = index + "0"
#         print(index)
#         print(int(index, 2))
#         startList[int(index, 2)][1] = int(not startList[int(index, 2)][1])
#     time.sleep(1)
#     print("after " + str(errorsBin))

# print(str(startList)
# #   .replace(", [", ",\n [")
#     )

# onesList = onlyOne(startList)

# print(str(onesList)
# #   .replace(", [", ",\n [")
#     )

# error = onesList[0]
# for x in onesList:
#     if x == onesList[0]: pass
#     error = x ^ error
# print(error)

# errorsBin = list(str(bin(error).split("b")[1]))
# print(errorsBin)
