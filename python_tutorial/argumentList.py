def concat(*args, sep="/"):
    return sep.join(args)

print(concat("earth", "mars", "venus"))



print(*list(range(5,10)))