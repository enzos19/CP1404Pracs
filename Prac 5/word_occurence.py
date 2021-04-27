text = input("Please type the text: ")
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
    for word in words:
        print("{} : {}".format(word, word_count[word]))