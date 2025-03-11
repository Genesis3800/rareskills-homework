p = 71

print("Problem 5")

print("My approach in this one is simple, just brute force it")

print("p = 71")
print("a = 12")
solutions = []

for i in range(0, p):
    if (i*i) % p == 12:
        solutions.append(i)

print(solutions)
