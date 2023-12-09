def is_valid_bayesian_network(network_structure, tolerance=1e-5):
    for variable, data in network_structure.items():
        parents = data['parents']
        prob = data['prob']

        # Check if all parents exist in the network
        for parent in parents:
            if parent not in network_structure:
                return False

        # Check if conditional probabilities sum up to approximately 1
        if isinstance(prob, dict):
            prob_sum = sum(prob.values())
            if abs(1.0 - prob_sum) > tolerance:
                return False
        else:
            return False

    return True

input_data = {
    'Burglar': 0.001,
    'Earthquake': 0.002,
    'Alarm': {'parents': ['Burglar', 'Earthquake'], 'prob': {0: 0.999, 1: 0.001, 0: 0.998, 1: 0.002}},
    'JohnCalls': {'parents': ['Alarm'], 'prob': {0: 0.05, 1: 0.95}},
    'MaryCalls': {'parents': ['Alarm'], 'prob': {0: 0.01, 1: 0.99}}
}


# input_data = {
#     'Burglar': 0.001,
#     'Earthquake': 0.002,
#     'Alarm': {'parents': ['Burglar', 'Earthquake'], 'prob': {0: 0.999, 1: 0.001, 0: 0.998, 1: 0.002}},
#     'JohnCalls': {'parents': ['Alarm'], 'prob': {0: 0.10, 1: 0.95}},
#     'MaryCalls': {'parents': ['Alarm'], 'prob': {0: 0.01, 1: 0.99}}
# }

network_structure = {}

for variable, probability in input_data.items():
    if isinstance(probability, dict):
        parents = probability['parents']
        conditional_prob = probability['prob']
    else:
        parents = []
        conditional_prob = {0: probability, 1: 1 - probability}

    network_structure[variable] = {'parents': parents, 'prob': conditional_prob}

# Check the validity of the Bayesian network
if is_valid_bayesian_network(network_structure):
    print("The Bayesian network is valid.")
    # Print the Bayesian network structure in the desired format
    for variable, data in network_structure.items():
        parents = data['parents']
        prob = data['prob']

        prob_str = "{" + ", ".join([f"{k}: {v}" for k, v in prob.items()]) + "}"

        print(f"'{variable}': {{'parents': {parents}, 'prob': {prob_str}}},")
else:
    print("The Bayesian network is not valid.")
