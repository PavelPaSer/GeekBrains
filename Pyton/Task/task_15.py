fib = [0, 1]

for i in range(10):
    fib.append(fib[-1] + fib[-2])

print(fib)

neg = [0, 1]

for n in range(10):
    neg.append(neg[-2] - neg[-1])
neg.reverse()

print(neg + fib[1:]) ## чтоб не было нуля начнем с первого элемета