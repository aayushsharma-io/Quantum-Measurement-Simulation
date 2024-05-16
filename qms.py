import random

# Function to measure color
def measure_color(electron):
    # Returns 'B' for black and 'W' for white
    return electron

# Function to measure hardness
def measure_hardness(electron):
    # Randomly determine hardness for 'B' or 'W' electrons
    if electron in ['B', 'W']:
        return random.choice(['H', 'S'])
    else:
        return electron

# Function to demonstrate the measurement process
def demonstrate_measurement_process(electrons):
    results = []
    for electron in electrons:
        # Measure color first
        color = measure_color(electron)
        
        # Measure hardness
        hardness = measure_hardness(color)
        
        # Measure color again after hardness
        color_after_hardness = measure_color(color)
        
        results.append((color, hardness, color_after_hardness))
    
    return results

# Function to print results
def print_results(results):
    print("Color -> Hardness -> Color After Hardness")
    for result in results:
        print(f"{result[0]} -> {result[1]} -> {result[2]}")

# Sample input electrons
input_electrons = ['B', 'W', 'B', 'W']

# Perform the measurement process
results = demonstrate_measurement_process(input_electrons)

# Print the results
print_results(results)
