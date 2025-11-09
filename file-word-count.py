# Program to find the most frequent words in a text file

# Step 1: Ask user for the file name
filename = input("Enter file name: ") #e.g. sample.txt

# Step 2: Open and read the file
with open(filename, 'r') as file:
    text = file.read()

# Step 3: Convert text to lowercase and split into words
words = text.lower().split()
print(words)
# Step 4: Count frequency of each word
word_count = {}
for word in words:
    word = word.strip(".,!?;:\"'()[]{}")  # remove punctuation
    if word:
        word_count[word] = word_count.get(word, 0) + 1


# Step 5: Find the word(s) with the maximum frequency
max_freq = max(word_count.values())
most_frequent = []
for word, count in word_count.items():
    if count == max_freq:
        most_frequent.append(word)

# Step 6: Display the result
print("\nMost frequent word(s):")
for word in most_frequent:
    print(f"{word} : {word_count[word]} times")
