items = []
while True:
    word = input("Word: ")
    
    if word not in items:
        items.append(word)
    else:
        print(f"You typed in {len(items)} different words")
        break