import galois

# Define the finite field GF(71)
GF = galois.GF(71)

# Define the polynomials using their coefficients
# Format: [constant term, x term, x² term]
p_coeffs = GF([52, 24, 61])  # 52x² + 24x + 61
q_coeffs = GF([40, 40, 58])  # 40x² + 40x + 58

# Create polynomial objects
x = galois.Poly([0, 1], field=GF)  # Represents x
p = galois.Poly([52, 24, 61], field=GF)  # 52x² + 24x + 61
q = galois.Poly([40, 40, 58], field=GF)  # 40x² + 40x + 58
# Addition: p(x) + q(x)
sum_poly = p + q
print("p(x) + q(x) =", sum_poly)

# Multiplication: p(x) * q(x)
prod_poly = p * q
print("p(x) * q(x) =", prod_poly)

# Find roots of p(x)
p_roots = p.roots()
print("Roots of p(x):", p_roots)

# Find roots of q(x)
q_roots = q.roots()
print("Roots of q(x):", q_roots)

# Find roots of p(x)q(x)
pq_roots = prod_poly.roots()
print("Roots of p(x)q(x):", pq_roots)