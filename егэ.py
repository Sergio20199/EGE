B0, B1 = 1, 9999
C0, C1 = 3648, 6287

def f(x, A0, A1, y):
    return ((B0 <= x <= B1) ==(C0 <= x <= C1)) or (A0 <= x <= A1) or (x >4200) or (y > 500)

min_len_A = float('inf')
limit = 10000

for A0 in range(1, limit):
    for A1 in range(A0 + 1, limit):
        if all(f(x, A0, A1, y) for x in range(1, limit) for y in range(1, limit)):
            min_len_A = min(min_len_A, A1 - A0)

print(min_len_A)