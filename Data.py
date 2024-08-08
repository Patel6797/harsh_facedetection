import csv

# Define the data for individuals
people_data = [
    {"First Name": "Harsh", "Last Name": "Kathiriya", "Address": "1 Fayer Court, Henbury Way, Watford, WD197EL", "SSN": "123-45-6789", "DOB": "06/07/1997"},
    {"First Name": "Keerti", "Last Name": "Kathiriya", "Address": "15 Sleaford Green, Watford, England, WD19-7EB", "SSN": "NA", "DOB": "12/05/1997"},
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