# Define customer records as a list of tuples (ID, Last Name, City, Property Size)
geralds_customers = [
    (4891, "Smith", "South Bend", 1500),
    (4978, "Miller", "Bloomington", 9800),
    (5144, "Johnson", "Terre Haute", 3500),
    (8949, "Garcia", "Fort Wayne", 2500),
    (9841, "Brown", "Gary", 3000)
]

geraldines_customers = [
    (1598, "Jones", "Jeffersonville", 1500),
    (2578, "Smith", "Evansville", 2500),
    (6548, "Robertson", "Indianapolis", 1000),
    (9853, "Erickson", "Clarksville", 1750),
    (9856, "Jacobs", "Columbus", 1900)
]

# Function to merge two sorted lists without duplicates
def merge_customers(geralds, geraldines):
    merged_customers = []
    i, j = 0, 0

    while i < len(geralds) and j < len(geraldines):
        if geralds[i][0] < geraldines[j][0]:
            merged_customers.append(geralds[i])
            i += 1
        elif geralds[i][0] > geraldines[j][0]:
            merged_customers.append(geraldines[j])
            j += 1
        else:
            # If IDs are the same, add only one (avoid duplicates)
            merged_customers.append(geralds[i])
            i += 1
            j += 1

    # Add remaining records if any
    while i < len(geralds):
        merged_customers.append(geralds[i])
        i += 1

    while j < len(geraldines):
        merged_customers.append(geraldines[j])
        j += 1

    return merged_customers

# Merge the two customer lists
merged_list = merge_customers(geralds_customers, geraldines_customers)

# Display the merged list
for customer in merged_list:
    print(customer)
