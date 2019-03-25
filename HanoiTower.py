from time import time
def bin_fibonacci(n):
    print(f"Calculating F({n})")
    if n <= 1:
        return 1
    else:
        return bin_fibonacci(n-1) + bin_fibonacci(n-2)

def lin_fibonacci(k):
    if k <= 1:
        # returns (F1, 0) or (F0, 0)
        return (1, 0)
    else:
        (i, j) = lin_fibonacci(k-1)
        # returns (Fk, Fk-1)
        return (i+j, i)

def is_sorted(list):
    if len(list) == 1:
        return True
    else:
        return (list[0] < list[1]) and is_sorted(list[1:])

def santa_delivers_presents_recursively(houses):
    print(f"Delivering presents to {houses[0]}'s home")
    if len(houses) > 1:
        santa_delivers_presents_recursively(houses[1:])

def generate_binary(num):
    if num == 1:
        return ['0', '1']
    else:
        return [k + '0' for k in generate_binary(num-1)] + [k + '1' for k in generate_binary(num-1)]

a_list = generate_binary(4)

print(a_list)