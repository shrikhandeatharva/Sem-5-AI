# Activation function: predicts the class based on weights, input, and bias
def activation(weights, input_vector, bias):
    weighted_sum = sum(w * v for w, v in zip(weights, input_vector)) + bias
    return 1 if weighted_sum > 0 else -1

# Training function: adjusts weights and bias to learn from the data
def train_perceptron(weights, bias, data, learning_rate=0.1, epochs=10):
    for _ in range(epochs):
        for dp in data:
            # Make a prediction using the current weights and bias
            prediction = activation(weights, dp[:4], bias)
            # Calculate the loss (the difference between the actual and predicted class)
            loss = dp[4] - prediction
            # Update the weights and bias based on the loss
            for i in range(4):
                weights[i] += learning_rate * loss * dp[i]
            bias += learning_rate * loss
    return weights, bias

# Main function
def main():
    # Read and process the data from "iris.csv"
    with open("iris.csv", "r") as f:
        data = f.readlines()
        data = [d.replace("Iris-setosa", "-1").replace("Iris-versicolor", "1") for d in data]
        data = [d.strip().split(",") for d in data]
        data = [[float(v) for v in d] for d in data]

    # Initialize weights and bias
    weights = [0, 0, 0, 0]
    bias = 0

    # Split data into training and test sets
    test_set = data[45:50] + data[95:100]
    training_set = data[:45] + data[50:95]

    # Train the perceptron
    weights, bias = train_perceptron(weights, bias, training_set)

    # Print the trained weights
    print(f"Trained Weights: {weights}")

    print(f"Bias: {bias}")

    # Test the perceptron on the test set
    print("Test Set:")
    for dp in test_set:
        prediction = activation(weights, dp[:4], bias)
        print(f"Predicted: {prediction} | Actual: {dp[4]}")

    # Visualize the data and decision boundary using Matplotlib
    import matplotlib.pyplot as plt
    plt.scatter([d[1] for d in data[:50]], [d[2] for d in data[:50]], color="red", label="Iris-setosa")
    plt.scatter([d[1] for d in data[50:100]], [d[2] for d in data[50:100]], color="blue", label="Iris-versicolor")
    plt.xlabel("Sepal Width")
    plt.ylabel("Petal Length")

    # Calculate the decision boundary and plot it
    slope = -weights[1] / weights[2]
    y_intercept = -bias / weights[2]
    x_values = [2, 5]
    y_values = [slope * x + y_intercept for x in x_values]
    plt.plot(x_values, y_values, label='Decision Boundary', color='black')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
