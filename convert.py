import csv

# Data to populate the CSV
items = [
    { "symbol": "A", "type": "text", "system": "Alphabet", "label": "A", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "B", "type": "text", "system": "Alphabet", "label": "B", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "C", "type": "text", "system": "Alphabet", "label": "C", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "D", "type": "text", "system": "Alphabet", "label": "D", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "E", "type": "text", "system": "Alphabet", "label": "E", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "F", "type": "text", "system": "Alphabet", "label": "F", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "G", "type": "text", "system": "Alphabet", "label": "G", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "H", "type": "text", "system": "Alphabet", "label": "H", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "I", "type": "text", "system": "Alphabet", "label": "I", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "J", "type": "text", "system": "Alphabet", "label": "J", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "K", "type": "text", "system": "Alphabet", "label": "K", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "L", "type": "text", "system": "Alphabet", "label": "L", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "M", "type": "text", "system": "Alphabet", "label": "M", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "N", "type": "text", "system": "Alphabet", "label": "N", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "O", "type": "text", "system": "Alphabet", "label": "O", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "P", "type": "text", "system": "Alphabet", "label": "P", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "Q", "type": "text", "system": "Alphabet", "label": "Q", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "R", "type": "text", "system": "Alphabet", "label": "R", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "S", "type": "text", "system": "Alphabet", "label": "S", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "T", "type": "text", "system": "Alphabet", "label": "T", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "U", "type": "text", "system": "Alphabet", "label": "U", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "V", "type": "text", "system": "Alphabet", "label": "V", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "W", "type": "text", "system": "Alphabet", "label": "W", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "X", "type": "text", "system": "Alphabet", "label": "X", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "Y", "type": "text", "system": "Alphabet", "label": "Y", "tags": ["letter", "SLP", "OT"] },
    { "symbol": "Z", "type": "text", "system": "Alphabet", "label": "Z", "tags": ["letter", "SLP", "OT"] },
    {"symbol": "./images/more.png", "type": "image", "system": "Proloquo2Go", "label": "More", "tags": ["symbols", "OT", "SLP"]},
    {"symbol": "./images/all-done.png", "type": "image", "system": "Proloquo2Go", "label": "All Done", "tags": ["symbols", "OT", "SLP"]}
]

# Filepath for the CSV file
csv_file_path = "symbols_master.csv"

# Write to CSV
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Symbol", "Type", "System", "Label", "Tags"])
    # Write rows
    for item in items:
        writer.writerow([
            item["symbol"],
            item["type"],
            item["system"],
            item["label"],
            ", ".join(item["tags"])  # Join tags into a single string
        ])

csv_file_path
