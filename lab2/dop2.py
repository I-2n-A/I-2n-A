n = int(input())

def get_n_count(n):
    count = 0
    while n:
        count += 1
        n = n // 10
    return count

def get_n(max_n):
    for x in range(1, max_n + 1):
        square = x * x
        length_of_x = get_n_count(x)
        num_divider = 10 ** length_of_x
        num = square % num_divider
        if num == x:
            yield num
for x in get_n(n):
    print(x, "*", x, "=", x * x)