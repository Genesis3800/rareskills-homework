p = 71

print("Problem 2")

print("First I want to check if these two calculations yield the same result: ")
print("Calculation 1:  (-1 * 18) mod 71 = (-1 mod 71) * (18 mod 71) = final_result")
print("Calculation 2:  (-1 * 18) mod 71 = -18 mod 71 = final_result")

print("Result of calculation 1:")
first_mini_1 = -1%71
first_mini_2 = 18%71
first_result_1_wrong = (first_mini_1 * first_mini_2)
first_result_1_correct = (first_result_1_wrong%71)

print("The result of calculation 1 is: ", first_result_1_wrong)
print("This comes out wrong cause the final result needs to be moduloed by 71")
print("The correct result is: ", first_result_1_correct)
print("which is essentially ~wrong_answer%71~")

print("-----------------------")

print("Result of calculation 2:")
final_result_2 = -18%71
print("The result of calculation 2 is: ", final_result_2)

print("-----------------------")



print("Now moving onto the actual meat of problem 2")
print("I need to calculate the congurent number for a=5/6, which is a fraction")
print("The key here is let a= x/y, then a = x*(multiplicative inverse of y mod p)")

print("So, a ≡ ((5 %71) * (multiplicative inverse of 6 mod 71) )%71")

print("Now I need to calculate the multiplicative inverse of 6 mod 71")
print("which is:")
first_num_denominator_inverse = (pow(6, -1, p))
print(first_num_denominator_inverse)

print("Now I can calculate the final result for the first number")
print("which is:")
first_num_result = ((5%p) * (first_num_denominator_inverse%p))%p
print(first_num_result)


print("Now I will directly print the equivalent values for b=11/12 and c =21/12")
print("b ≡ ((11 %71) * (multiplicative inverse of 12 mod 71) )%71")
second_num_denominator_inverse = (pow(12, -1, p))
second_num_result = ((11%p) * (second_num_denominator_inverse%p))%p
print(second_num_result)

print("c ≡ ((21 %71) * (multiplicative inverse of 12 mod 71) )%71")
third_num_denominator_inverse = (pow(12, -1, p))
third_num_result = ((21%p) * (third_num_denominator_inverse%p))%p
print(third_num_result)

print("Now I need to verify that a+b=c (in the finite field of 71)")

print("first way: a+b = 5/6 + 11/12 = 21/12 ")

print("second way: a+b = (60+66)%71 = 126%71 = 55")

# Code to verify that (first_num_result + second_num_result) % 71 = third_num_result

# Calculate the sum modulo 71
sum_result = (first_num_result + second_num_result) % p

# Check if the sum equals third_num_result
is_equal = sum_result == third_num_result

# Print the results
print("-----------------------")
print("Verification that (first_num_result + second_num_result) % 71 = third_num_result:")
print(f"first_num_result = {first_num_result}")
print(f"second_num_result = {second_num_result}")
print(f"Sum modulo 71 = {sum_result}")
print(f"third_num_result = {third_num_result}")
print(f"Are they equal? {is_equal}")

# Show the calculation
print(f"Calculation: ({first_num_result} + {second_num_result}) % 71 = {sum_result}")

if is_equal:
    print("✓ Verified: The sum of a and b equals c in the finite field of 71")
else:
    print("✗ Not verified: The sum of a and b does not equal c in the finite field of 71")
print("-----------------------")