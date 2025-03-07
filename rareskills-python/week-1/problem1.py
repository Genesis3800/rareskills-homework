
print("Problem 1")

# The finite field is set to 71
# The set of possible values therefore is 0, 1, 2, ..., 70
p = 71

print("This gives the modulo of 5 mod 71")
print(5 % p)

print("-----------------------")

print("This gives the number congurent to -5")
print(-5 % p)

print("-----------------------")

print("This gives the number congurent to 5")
print(5 % p)

print("-----------------------")

print("This gives the multiplicative inverse of 5 mod 71")
# Multiplicative inverse here means that 5×3=15≡1(mod7)
# Note to self: Look into Fermat's Little Theorem: a^(p-2) ≡ a^(-1) (modp)
print(pow(5, -1, p))

print("-----------------------")

print("This gives the multiplicative inverse of -1 mod 71")
print(pow(-1, -1, p))

print("-----------------------")

print("This gives the multiplicative inverse of -4 mod 71")
print(pow(-4, -1, p))

print("-----------------------")

print("This gives the multiplicative inverse of -160 mod 71")
print(pow(-160, -1, p))

print("-----------------------")

print("This gives the multiplicative inverse of 500 mod 71")
print(pow(500, -1, p))

print("-----------------------")


