file = open('ExampleIFile.txt', 'r')
Ofile = open('ExampleOFile.txt', 'w')

words = []
loremCount = 0
ipsumCount = 0

for line in file:

    word = line.split()
    for i in range(len(word)):

        if (word[i].upper() == 'Lorem'.upper()):
            loremCount += 1

        if (word[i].upper() == 'ipsum'.upper()):
            ipsumCount += 1

        words.append(word)
    word = []

print(len(words))

sortedWords = str(words.sort())

for char in sortedWords:
    Ofile.write(sortedWords)

print("Number of Lorem's:", loremCount)
print("Number of Ipsum's:", ipsumCount)
