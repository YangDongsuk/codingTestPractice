a = input()
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
num_sum = 0
words = []
for i in a:
    if i in num_list:
        num_sum += int(i)
    else:
        words.append(i)

words.sort()
word2 = ""
for i in words:
    word2 += i


print(word2+str(num_sum))
