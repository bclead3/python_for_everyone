overall_words = []
handle = open('romeo.txt')
for line in handle:
    words = line.split()
    for word in words:
        if word not in overall_words:
            overall_words.append(word)

overall_words.sort()
print(overall_words)