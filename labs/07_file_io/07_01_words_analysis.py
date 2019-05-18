'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
word_list = []
word_count = 0
longest_word_list = []
shortest_word_list = []
fout = open('words.txt', 'r')
fread = fout.readlines()
for line in fread:
    line = line.rstrip()
    word_count += 1
    word_list.append(line)
fout.close()

longest_word = max(word_list, key=lambda b : len(b))
shortest_word = min(word_list, key = lambda b : len(b))
for word in word_list:
    if len(word) == len(shortest_word):
        shortest_word_list.append(word)
    if len(word) == len(longest_word):
        longest_word_list.append(word)
print(f"Total words are {word_count}")
print(longest_word_list)
print(shortest_word_list)
#print(word_list)
