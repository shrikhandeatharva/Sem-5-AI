def fuzzy_set_union(A, B):
    result = {}
    for key in A.keys():
        result[key] = max(A[key], B.get(key, 0))
    for key in B.keys():
        if key not in result:
            result[key] = B[key]
    return result

def fuzzy_set_intersection(A, B):
    result = {}
    for key in A.keys():
        if key in B:
            result[key] = min(A[key], B[key])
    return result

def fuzzy_set_complement(A):
    result = {}
    for key in A.keys():
        result[key] = 1 - A[key]
    return result

# Example fuzzy sets
# A = {'A': 0.3, 'B': 0.5, 'C': 0.8}
# B = {'B': 0.7, 'C': 0.4, 'D': 0.2}
A = {'A': 0.3, 'B': 0.5, 'C': 0.8}
B = {'A': 0.7, 'B': 0.4, 'C': 0.2}

# Union of A and B
union_result = fuzzy_set_union(A, B)
print("Union :", union_result)

# Intersection of A and B
intersection_result = fuzzy_set_intersection(A, B)
print("Intersection :", intersection_result)

# Complement of A
complement_result = fuzzy_set_complement(A)
print("Complement of A :", complement_result)

# Complement of B
complement_result = fuzzy_set_complement(B)
print("Complement of B :", complement_result)
