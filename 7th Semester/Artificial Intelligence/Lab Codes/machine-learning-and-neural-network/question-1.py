import numpy as np
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = np.zeros(input_size + 1)  # Including bias term

    # Step 1: Define the activation function (Step function)
    def activation(self, x):
        return 1 if x >= 0 else 0

    # Step 2: Train the Perceptron
    def train(self, X, y):
        for _ in range(self.epochs):
            for i in range(len(X)):
                # Input with bias term
                inputs = np.append(X[i], 1)
                prediction = self.activation(np.dot(inputs, self.weights))
                # Update weights using the perceptron learning rule
                self.weights += self.learning_rate * (y[i] - prediction) * inputs

    # Step 3: Make predictions
    def predict(self, X):
        predictions = []
        for i in range(len(X)):
            inputs = np.append(X[i], 1)
            prediction = self.activation(np.dot(inputs, self.weights))
            predictions.append(prediction)
        return predictions

# Step 4: Define input and output for AND and OR gates
# AND Gate
X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input
y_and = np.array([0, 0, 0, 1])  # Output

# OR Gate
X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input
y_or = np.array([0, 1, 1, 1])  # Output

# Step 5: Create perceptron models for AND and OR gates
perceptron_and = Perceptron(input_size=2)
perceptron_or = Perceptron(input_size=2)

# Train the models
perceptron_and.train(X_and, y_and)
perceptron_or.train(X_or, y_or)

# Step 6: Test the models
print("Testing AND Gate:")
predictions_and = perceptron_and.predict(X_and)
print(f"Predictions: {predictions_and}")
print(f"Expected: {y_and}\n")

print("Testing OR Gate:")
predictions_or = perceptron_or.predict(X_or)
print(f"Predictions: {predictions_or}")
print(f"Expected: {y_or}")