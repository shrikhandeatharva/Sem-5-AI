network_structure = {
    'Flu': {'parents': [], 'prob': {0: 0.05, 1: 0.95}},
    'Cold': {'parents': [], 'prob': {0: 0.10, 1: 0.90}},
    'Cough': {'parents': ['Flu', 'Cold'], 'prob': {'Flu': 0.70, 'Cold': 0.40}},
    'Fever': {'parents': ['Flu', 'Cold'], 'prob': {'Flu': 0.80, 'Cold': 0.10}},
    'Headache': {'parents': ['Flu', 'Cold'], 'prob': {'Flu': 0.60, 'Cold': 0.20}},
    'Sneezing': {'parents': ['Flu', 'Cold'], 'prob': {'Flu': 0.30, 'Cold': 0.70}}
}

# Given query
query_variable = 'Flu'
evidence_variable = 'Cough'

# Calculate P(Cough)
# P(Cough) = P(Cough | Flu) * P(Flu) + P(Cough | Cold) * P(Cold)
p_cough = (
    network_structure[evidence_variable]['prob'][query_variable] * network_structure[query_variable]['prob'][1] +
    network_structure[evidence_variable]['prob'][query_variable] * network_structure[query_variable]['prob'][0]
)

# Calculate P(Flu | Cough) using Bayes' theorem
# P(Flu | Cough) = (P(Cough | Flu) * P(Flu)) / P(Cough)
p_flu_given_cough = (
    network_structure[evidence_variable]['prob'][query_variable] * network_structure[query_variable]['prob'][1]
) / p_cough

print(f'P({query_variable} | {evidence_variable}) = {p_flu_given_cough:.2f}')
