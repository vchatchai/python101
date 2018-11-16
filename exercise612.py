

# filename = input("please fill the file name:")
filename = 'usernames.txt'
with open(filename, 'r') as  file : 
    for line in file : 
        words = [line.split()] 
        words.insert(0, words[0].pop(0))
        print(words)

