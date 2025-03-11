p = 71

print("Problem 4")

print("Consider a 2x2 Matrix A = [[a,b],[c,d]]")
print("The determinant of A is ad-bc")
print("The inverse of the matrix is given by:")
print("1/(determinant) * [[d,-b],[-c,a]]")

print("-----------------------")

print("Now, the given matrix is A = [[1,1],[1,4]]")
print("The determinant of A is 1*4-1*1 = 3")
print("The inverse of A is given by:")
print("1/3 * [[4,-1],[-1,1]]")

print("-----------------------")

print("This is the same as multiplying by inverse 3 modulo 71 ")
inverse_multiple = pow(3, -1, 71)
print("which is equal to:", inverse_multiple)

print("Therefore, the inverse of A is:")
print(inverse_multiple * 4, inverse_multiple * -1, inverse_multiple * -1, inverse_multiple * 1)

print("-----------------------")

print("These numbers are all huge af because they have not been moduloed by 71")
print("So, the correct inverse of A is:")
print((inverse_multiple * 4 )% 71, (inverse_multiple * -1 )% 71, (inverse_multiple * -1 )% 71, (inverse_multiple * 1 )% 71)

print("-----------------------")

print("Now I need to multiply A by it's inverse to check if our result is correct")
print("A*A^-1 = [[1,1],[1,4]]*[[25,47],[47,24]]")
print("A*A^-1 = [[1*25+1*47,1*47+1*24],[1*25+4*47,1*47+4*24]]")

print("The calculated numbers of the matrix are:")
print((1*25+1*47)%71, (1*47+1*24)%71, (1*25+4*47)%71, (1*47+4*24)%71)

print("-----------------------")



