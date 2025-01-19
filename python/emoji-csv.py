import csv

# Input and output file paths
emoji_file_path = "emojis.txt"
output_csv_path = "emojis_master.csv"

# Default values
default_type = "emoji"
default_system = "general"
default_label_prefix = "Emoji"

# Read emojis from the file
with open(emoji_file_path, "r", encoding="utf-8") as file:
    emojis = file.read().split()  # Split by whitespace

# Write to CSV
with open(output_csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    # Write header
    writer.writerow(["Symbol", "Type", "System", "Label"])
    # Write each emoji with default values
    for i, emoji in enumerate(emojis, start=1):
        writer.writerow([emoji, default_type, default_system, f"{default_label_prefix} {i}"])

print(f"Spreadsheet created: {output_csv_path}")
