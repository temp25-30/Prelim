words = []

print("Enter 3 Words")
for i in range(1,4):
    print(f"Word#{i}:")
    word = input()
    words.append(word)

words.sort()
print(f"\nThe last word is: {words[2]}")
