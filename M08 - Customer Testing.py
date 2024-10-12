# Define the merge_customers function first
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


geralds_customers_test1 = [
    (4891, "Smith", "South Bend", 1500),
    (4978, "Miller", "Bloomington", 9800),
    (5144, "Johnson", "Terre Haute", 3500),
    (8949, "Garcia", "Fort Wayne", 2500),
    (9841, "Brown", "Gary", 3000)
]

geraldines_customers_test1 = [
    (1598, "Jones", "Jeffersonville", 1500),
    (2578, "Smith", "Evansville", 2500),
    (6548, "Robertson", "Indianapolis", 1000),
    (9853, "Erickson", "Clarksville", 1750),
    (9856, "Jacobs", "Columbus", 1900)
]

# Expected Output: Merged and sorted list of customers by customer ID.
merged_list_test1 = merge_customers(geralds_customers_test1, geraldines_customers_test1)
print("Test Case 1: General Merge")
for customer in merged_list_test1:
    print(customer)
geralds_customers_test2 = [
    (4891, "Smith", "South Bend", 1500),
    (2578, "Smith", "Bloomington", 2500),
    (5144, "Johnson", "Terre Haute", 3500)
]

geraldines_customers_test2 = [
    (2578, "Smith", "Evansville", 2500),
    (6548, "Robertson", "Indianapolis", 1000),
    (9853, "Erickson", "Clarksville", 1750)
]

# Expected Output: Merged list should contain only one "2578 Smith" record.
merged_list_test2 = merge_customers(geralds_customers_test2, geraldines_customers_test2)
print("Test Case 2: Duplicate Customer IDs")
for customer in merged_list_test2:
    print(customer)

geralds_customers_test3 = []  # Empty Gerald's file

geraldines_customers_test3 = [
    (1598, "Jones", "Jeffersonville", 1500),
    (2578, "Smith", "Evansville", 2500),
    (9856, "Jacobs", "Columbus", 1900)
]

# Expected Output: Merged list should contain only records from Geraldine's file.
merged_list_test3 = merge_customers(geralds_customers_test3, geraldines_customers_test3)
print("Test Case 3: One File is Empty")
for customer in merged_list_test3:
    print(customer)

geralds_customers_test4 = [
    (4891, "Smith", "South Bend", 1500),
    (4978, "Miller", "Bloomington", 9800)
]

geraldines_customers_test4 = [
    (1598, "Jones", "Jeffersonville", 1500),
    (2578, "Smith", "Evansville", 2500),
    (6548, "Robertson", "Indianapolis", 1000),
    (9853, "Erickson", "Clarksville", 1750)
]

# Expected Output: Merged list should contain all records from both lists, sorted.
merged_list_test4 = merge_customers(geralds_customers_test4, geraldines_customers_test4)
print("Test Case 4: Different File Sizes")
for customer in merged_list_test4:
    print(customer)
