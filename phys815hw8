import numpy as np
import matplotlib.pyplot as plt

# Define the true value of the parameter
true_p = 0.7

# Define the number of experiments to simulate for each true value
num_experiments = 100

# Define the sample size for each experiment
sample_size = 10

# Define the function to generate random data based on the true parameter
def generate_data(p, n):
    return np.random.binomial(n, p)

# Define the function to calculate the observable based on the generated data
def calculate_observable(data):
    return np.mean(data)

# Initialize arrays to store the true and measured parameter values
true_p_array = np.linspace(0, 1, 21)
measured_p_array = np.zeros_like(true_p_array)

# Loop over the true parameter values and simulate experiments
for i, true_p in enumerate(true_p_array):
    measured_p_values = np.zeros(num_experiments)
    for j in range(num_experiments):
        data = generate_data(true_p, sample_size)
        measured_p_values[j] = calculate_observable(data)
    measured_p_array[i] = np.mean(measured_p_values)

# Plot
plt.plot(true_p_array, measured_p_array, 'o')
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('True Parameter Value')
plt.ylabel('Measured Parameter Value')
plt.show()
