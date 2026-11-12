
import csv

# Open the audit CSV file
with open("audit.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    total_rows = 0
    agreement_count = 0

    for row in reader:
        total_rows += 1

        if row["agree"].strip().lower() == "true":
            agreement_count += 1

# Calculate agreement percentage
percentage = (agreement_count / total_rows) * 100

print("Total rows:", total_rows)
print("Agreements:", agreement_count)
print("Disagreements:", total_rows - agreement_count)
print("Agreement percentage:", percentage)
