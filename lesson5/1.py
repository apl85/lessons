def num_gen(num):
    for i in range(1, num + 1, 2):
        yield i



number = num_gen(7)

print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))







