f = open("")
max_count_G = 0
a = f.read()
s = ""
for string in a.split():
    cur_count_G = string.count("Q")
    if cur_count_G > max_count_G:
        max_count_G = cur_count_G
        s = string

syms = {}
for i in s:
    syms[i] = syms.get(i, 0) + 1

max_count = min(syms.values())
spisok_syms = []

for key, value in syms.items():
    if value == max_count:
        spisok_syms.append(key)
print(sorted(spisok_syms))
print(a.count(sorted(spisok_syms)[0]))
