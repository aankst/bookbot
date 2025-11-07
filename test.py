data = []

for ch in "abracadabra":
    # Check if we already have a dict for this char
    found = False
    for d in data:
        if d["char"] == ch:
            d["count"] += 1
            found = True
            break
    
    # If not found, create a new one
    if not found:
        data.append({"char": ch, "count": 1})

print(data)