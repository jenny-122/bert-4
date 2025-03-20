def find_unique_labels(filename):
    # Make an empty set
    unique_labels = set()
    
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        unique_labels.add(line.strip())
    
    return unique_labels

path = "extracted-spike-data/Spike7k_labels.txt"
unique_labels = find_unique_labels(path)
print(unique_labels)  # Added this to see the result
print(len(unique_labels))
