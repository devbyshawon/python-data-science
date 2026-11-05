# Sample medical labels
labels = [
    "Pneumonia",
    "Edema",
    "Cardiomegaly",
    "Pneumonia",
    "Edema",
    "Pneumonia",
    "Cardiomegaly",
    "Edema",
    "Pneumonia",
    "Edema"
]


# Create a function
def count_diseases(labels):
    counts = {}

    # Loop through all labels
    for label in labels:
        if label not in counts:
            counts[label] = 0

        counts[label] += 1

    return counts


# Call the function
results = count_diseases(labels)

# Display the output
print("Medical Label Counts")
print("--------------------")

for disease, count in results.items():
    print(f"{disease}: {count}")

print(f"\nTotal labels: {len(labels)}")
