p = 71

print("Honestly, I don't understand the point of this problem :p")
print("Problem 7")

print("I need to find a polynomial of degree 1 that passes through  (10, 15), (23, 29).")
print("Since these are two points, the polynomial will be of degree 1 and be the equation for a line (y = mx + c).")

slope = (29 - 15) / (23 - 10)

print("No, the slope, m =", slope)

y_intercept = 15 - 10 * slope
print("Therefore, c = 15 - 10 * m =", "which is equal to:", y_intercept)
print("--------------------------------")
print("Therefore, the polynomial is y =", slope, "x +", y_intercept)

print("--------------------------------")
print("Now, I need to find out f(10) and f(23)")

print("f(10) =", slope * 10 + y_intercept)
print("f(23) =", slope * 23 + y_intercept)

















