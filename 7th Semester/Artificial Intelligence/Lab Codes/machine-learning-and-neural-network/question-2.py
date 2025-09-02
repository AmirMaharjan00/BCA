import numpy as np
# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Sigmoid derivative function
def sigmoid_derivative(x):
    return x * (1 - x)

# Neural Network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        # Initialize weights with random values
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Random weights and biases
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        
        self.bias_hidden = np.random.rand(self.hidden_size)
        self.bias_output = np.random.rand(self.output_size)

    def forward(self, X):
        # Forward propagation through the network
        self.hidden_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = sigmoid(self.hidden_input)
        
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        self.final_output = sigmoid(self.final_input)
        
        return self.final_output

    def backward(self, X, y, output):
        # Backpropagation
        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)
        
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)
        
        # Update weights and biases
        self.weights_hidden_output += self.hidden_output.T.dot(output_delta)
        self.weights_input_hidden += X.T.dot(hidden_delta)
        
        self.bias_output += np.sum(output_delta, axis=0)
        self.bias_hidden += np.sum(hidden_delta, axis=0)

    def train(self, X, y, epochs):
        for epoch in range(epochs):
            # Perform forward pass
            output = self.forward(X)
            
            # Perform backward pass (backpropagation)
            self.backward(X, y, output)
            
            # Optionally, print error at intervals (for tracking learning)
            if epoch % 1000 == 0:
                error = np.mean(np.square(y - output))  # Mean Squared Error
                print(f'Epoch {epoch}, Error: {error}')

    def predict(self, X):
        return self.forward(X)

# Define the XOR problem (training data)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input
y = np.array([[0], [1], [1], [0]])  # Output

# Create a neural network with 2 input neurons, 4 hidden neurons, and 1 output neuron
nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1)

# Train the neural network
nn.train(X, y, epochs=10000)

# Test the neural network after training
print("\nTesting after training:")
print(nn.predict(X))