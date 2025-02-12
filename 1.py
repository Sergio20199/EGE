s = open('24_demo.txt').read()

count = 0
max_count = 0
for i in range(len(s)):
    if s[i] == 'X':
        count += 1
        if s[i] == 'Y':
            count += 1
            if s[i] == 'Z':
                count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print(max_count)
        
