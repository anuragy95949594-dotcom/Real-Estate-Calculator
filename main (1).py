# REAL ESTATE CALCULATOR
# College project using basic Python topics and File Handling

RECORD_FILE = "property_records.txt"

GST_RATE = 5
STAMP_DUTY_RATE = 5
REGISTRATION_FEE = 30000


def calculate_property_cost():
    print("\n===== CALCULATE PROPERTY COST =====")

    rate = float(input("Enter rate per sq. ft. (Rs.): "))
    area = float(input("Enter property area in sq. ft.: "))

    if rate <= 0 or area <= 0:
        print("Rate and area must be greater than zero.")
        return

    base_price = rate * area
    gst = base_price * GST_RATE / 100
    stamp_duty = base_price * STAMP_DUTY_RATE / 100
    registration = REGISTRATION_FEE
    total_cost = base_price + gst + stamp_duty + registration

    property_details = {
        "Rate per sq. ft.": rate,
        "Property Area (sq. ft.)": area,
        "Base Price (Rs.)": base_price,
        "GST (5%) (Rs.)": gst,
        "Stamp Duty (5%) (Rs.)": stamp_duty,
        "Registration Fee (Rs.)": registration,
        "Total Cost (Rs.)": total_cost
    }

    

    save_choice = input("Save this calculation? (y/n): ").lower()

    if save_choice == "y":
        file = open(RECORD_FILE, "a")
        file.write("\n========== PROPERTY RECORD ==========\n")
        for item, amount in property_details.items():
            file.write(item + ": " + str(amount) + "\n")
        file.write("=====================================\n")
        file.close()
        print("Record saved successfully in", RECORD_FILE)
    else:
        print("Record was not saved.")


def view_saved_records():
    print("\n===== SAVED PROPERTY RECORDS =====")
    file = open(RECORD_FILE, "r")
    records = file.read()
    file.close()

    if records == "":
        print("No records found.")
    else:
        print(records)


def main():
    while True:
        print("\n========== REAL ESTATE CALCULATOR ==========")
        print("1. Calculate Property Cost")
        print("2. View Saved Property Records")
        print("3. Exit")
        print("============================================")

        menu_choice = input("Enter your choice (1-3): ")

        if menu_choice == "1":
            calculate_property_cost()
        elif menu_choice == "2":
            view_saved_records()
        elif menu_choice == "3":
            print("Thank you for using Real Estate Calculator!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()
