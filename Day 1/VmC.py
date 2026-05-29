# CombinedResults.py

# Read VM1 accuracy
with open("vm1_result.txt", "r") as f:
    vm1_accuracy = float(f.read().strip())

# Read VM2 accuracy
with open("vm2_result.txt", "r") as f:
    vm2_accuracy = float(f.read().strip())

# Combine results
combined_accuracy = (vm1_accuracy + vm2_accuracy) / 2

# Display final result
print("\n=================================")
print(" CLOUD DISTRIBUTED MNIST RESULT ")
print("=================================")

print("VM1 Accuracy      :", vm1_accuracy)
print("VM2 Accuracy      :", vm2_accuracy)
print("Combined Accuracy :", combined_accuracy)

print("=================================")
print("VM1 trained first 30,000 MNIST images")
print("VM2 trained remaining 30,000 MNIST images")
print("Coordinator combined both VM results")
print("=================================")