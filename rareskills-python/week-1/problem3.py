p = 71

print("Problem 3")

print("I need to calculate elements congurent to a = 2/3, b=1/2, c=1/3")
print("I will be skipping over the calculation for this part in this problem")

print("Element congurent to a = 2/3 is")
congurent_a = ((2%p) * (pow(3, -1, p)%p))%p
print(congurent_a)

print("-----------------------")

print("Element congurent to b = 1/2 is")
congurent_b = ((1%p) * (pow(2, -1, p)%p))%p
print(congurent_b)

print("-----------------------")

print("Element congurent to c = 1/3 is")
congurent_c = ((1%p) * (pow(3, -1, p)%p))%p
print(congurent_c)

print("-----------------------")

print("Now I need to verify that a*b=c (in the finite field of 71)")

print("first way: a*b = (2/3) * (1/2) = 2/6 = 1/3 = c")

print("second way: a*b = (48 * 36) % 71")
print("Let us check if this is equal to c")

print("a*b = ", (48 * 36) % 71)
print("c = ", congurent_c)

print("-----------------------")

print("Ta ta da mofos!!!!!")




