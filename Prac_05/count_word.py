COUNT_WORD = {}
text = str(input("please insert a text: "))
word_list = text.split(" ")

print(word_list)
for word in word_list:
    count = word_list.count(word)
    COUNT_WORD[word] = count


for key, value in sorted(COUNT_WORD.items()):
    print("{}: {}".format(key, value))