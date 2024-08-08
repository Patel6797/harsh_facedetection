import csv

# Define the data for individuals
people_data = [
    {"First Name": "Harsh", "Last Name": "Kathiriya", "Address": "200 Vine Street, Waynesboro, VA-22980", "SSN": "123-45-6789"},
    {"First Name": "Keerti", "Last Name": "Kathiriya", "Address": "15 Sleaford Green, Watford, England, WD19-7EB", "SSN": "NA"},
    {"First Name": "Jhanvi", "Last Name": "Ghadia", "Address": "200 vine street, waynesboro, VA-22980", "SSN": "987-65-4321"},
    {"First Name": "Daksh", "Last Name": "Ghadia", "Address": "200 vine street, waynesboro, VA-22980", "SSN": "987-65-4321"},
    {"First Name": "Ajay", "Last Name": "Madhani", "Address": "9 bele-grene dr Fishershville, VA-22980", "SSN": "987-65-4321"},
    {"First Name": "Jay", "Last Name": "Madhani", "Address": "52 sunset blvd, Staunton, VA-22401", "SSN": "987-65-4321"},
    {"First Name": "Sohil", "Last Name": "Vekaria", "Address": "9 bel-grene dr, Fishershville, VA-22980", "SSN": "987-65-4321"},
    {"First Name": "Rinkal", "Last Name": "Madhani", "Address": "9 bel-grene dr, Fishershville, VA-22980", "SSN": "987-65-4321"},
    {"First Name": "Gita", "Last Name": "Madhani", "Address": "52 sunset blvd, Staunton, VA-22401", "SSN": "987-65-4321"},
    {"First Name": "Om", "Last Name": "Madhani", "Address": "9 bel-grene dr, Fishershville, VA-24401", "SSN": "987-65-4321"},
    {"First Name": "Shree", "Last Name": "Madhani", "Address": "9 bel-grene dr, Fishershville, VA-22401", "SSN": "987-65-4321"},
    {"First Name": "Mahi", "Last Name": "Madhani", "Address": "52 Sunset blvd, Staunton VA-22401", "SSN": "987-65-4321"},
    {"First Name": "Jay", "Last Name": "Sharma", "Address": "1320 Portrepublic rd, Harrisonburg, VA-24401", "SSN": "NA"},
    {"First Name": "Tanmay", "Last Name": "Chaudhari", "Address": "9 bel-grene dr, Fishershville, VA-22401", "SSN": "987-65-4321"}
   # Add more people as needed
]

# Specify the CSV file name
csv_file = "person_info.csv"

# Write the data to the CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["First Name", "Last Name", "Address", "SSN"])
    writer.writeheader()
    writer.writerows(people_data)
print("CSV file created successfully.")