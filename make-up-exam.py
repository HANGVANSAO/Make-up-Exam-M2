# def indexOfA(text):
#     countIndexA = 0
#     for i in range(len(text)):
#         if text[i] == "A":
#             countIndexA += 1
#     return countIndexA
# def indexOfB(text):
#     countIndexB = 0
#     for i in range(len(text)):
#         if text[i] == "B":
#             countIndexB += 1
#     return countIndexB
# def indexOfC(text):
#     countIndexC = 0
#     for i in range(len(text)):
#         if text[i] == "C":
#             countIndexC += 1
#     return countIndexC

# text = input()
# result = 0
# if indexOfA(text) == 4:
#     result += 40
# elif indexOfA(text) == 2 and indexOfB(text) == 2:
#     result += 20
# elif indexOfC(text) >= 1:
#     result += 10
# print(result)

# # #2
# # def sumXIndex(string):
# #     sum = 0
# #     for i in range(len(string)):
# #         if string[i] == "X":
# #             sum += i
# #     return sum

# # word = input()
# # sum= sumXIndex(word)
# # print(sum)







# 3
def getNumberOfFirstIndex(text,char):
    numberFirstIndex= 0
    firstIndex = True
    for i in range(len(text)):
        if text[i] == char and firstIndex:
            numberFirstIndex += i
            firstIndex = False
    return numberFirstIndex

text = input()
result = "NOT GOOD"
if getNumberOfFirstIndex(text,"X") < getNumberOfFirstIndex(text,"Y"):
    result = "GOOD"
print(result)