word_list = [x.strip() for x in open("words.txt", "r").readlines()]
for i in [word for word in word_list if word == word[::-1]]: print i