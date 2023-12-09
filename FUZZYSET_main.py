def fuzzy_set_union(A, B):
    result = {}
    for key in A.keys():
        result[key] = round(max(A[key], B.get(key, 0)), 2)
    for key in B.keys():
        if key not in result:
            result[key] = round(B[key], 2)
    return result

def fuzzy_set_intersection(A, B):
    result = {}
    for key in A.keys():
        if key in B:
            result[key] = round(min(A[key], B[key]), 2)
    return result

def fuzzy_set_complement(A):
    result = {}
    for key in A.keys():
        result[key] = round(1 - A[key], 2)
    return result

def fuzzy_set_sum(A, B):
    result = {}
    for key in A.keys():
        result[key] = round(A[key] + B.get(key, 0), 2)
    for key in B.keys():
        if key not in result:
            result[key] = round(B[key], 2)
    return result

def fuzzy_set_difference(A, B):
    result = {}
    for key in A.keys():
        result[key] = round(A[key] - B.get(key, 0), 2)
    for key in B.keys():
        if key not in result:
            result[key] = round(-B[key], 2)
    return result

def fuzzy_set_product(A, B):
    result = {}
    for key in A.keys():
        result[key] = round(A[key] * B.get(key, 1), 2)
    for key in B.keys():
        if key not in result:
            result[key] = round(0, 2)
    return result

def fuzzy_set_power(A, n):
    result = {}
    for key in A.keys():
        result[key] = round(A[key] ** n, 2)
    return result

def fuzzy_set_cartesian_product(A, B):
    result = {}
    for key1 in A.keys():
        for key2 in B.keys():
            result[key1 + key2] = round(A[key1] * B[key2], 2)
    return result

def fuzzy_set_disjunctive_sum(A, B):
    result = {}
    for key in A.keys():
        result[key] = round(max(A[key], B[key]), 2)
    for key in B.keys():
        if key not in result:
            result[key] = round(B[key], 2)
    return result

# Example fuzzy sets
A = {'A': 0.3, 'B': 0.5, 'C': 0.8}
B = {'A': 0.7, 'B': 0.4, 'C': 0.2}

# Perform various fuzzy set operations and label them
print("Union (A ∪ B):", fuzzy_set_union(A, B))
print("Intersection (A ∩ B):", fuzzy_set_intersection(A, B))
print("Complement of A:", fuzzy_set_complement(A))
print("Complement of B:", fuzzy_set_complement(B))
print("Sum (A + B):", fuzzy_set_sum(A, B))
print("Difference (A - B):", fuzzy_set_difference(A, B))
print("Product (A * B):", fuzzy_set_product(A, B))
print("Power (A^2):", fuzzy_set_power(A, 2))
print("Cartesian Product (A x B):", fuzzy_set_cartesian_product(A, B))
print("Disjunctive Sum (A ∨ B):", fuzzy_set_disjunctive_sum(A, B))
