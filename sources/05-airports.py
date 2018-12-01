airports = {
    "ORY": "Orly",
    "LAX": "Los Angeles",
}

print("Where are you going?")
a = input().upper()
if a in airports:
    print(airports[a])
else:
    print(a, "not found")
