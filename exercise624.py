values = [int(v) for v in input("Please fill number:").split()]

result = [v for  v in values if v < 0]

print(len(result))