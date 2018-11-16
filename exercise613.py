

# filename = input("please fill the file name:")
filename = 'usernames.txt'
usernames = []
with open(filename, 'r') as  file : 
    for line in file : 
        words = [line.split()] 
        words.insert(0, words[0].pop(0))
        usernames.append(words)


result = []

for username in usernames:
    if len(username[1]) == 0  :
        result.append(username[0])
        
print(usernames)
print(result)
