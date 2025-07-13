import os
import datetime

def get_last_meter_reading(file_path):
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found. Creating the file.")
        with open(file_path, 'w') as file:
            file.write("0,")  # Set default value for the last meter reading and date
        return 0, None  # Return default value

    try:
        with open(file_path, 'r') as file:
            data = file.readline().strip().split(',')
            if len(data) == 2:
                last_reading = float(data[0])  # Read the last meter reading
                last_date = datetime.datetime.strptime(data[1], '%Y-%m-%d').date()  # Read the date part
                return last_reading, last_date
            else:
                print("Error: Incorrect format in file. Resetting file.")
                with open(file_path, 'w') as reset_file:
                    reset_file.write("0,")
                return 0, None
    except ValueError:
        print("Error: Unable to parse last meter reading or date from file.")
        return None, None
    except Exception as e:
        print(f"Error: Unable to read file '{file_path}': {e}")
        return None, None

def write_new_meter_reading(file_path, new_reading):
    try:
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')  # Get current date
        with open(file_path, 'w') as file:
            file.write(f"{new_reading},{current_date}")  # Write both reading and date
    except Exception as e:
        print(f"Error: Unable to write new meter reading to file: {e}")

def calculate_electricity_bill(usage, rate_per_kWh):
    return usage * rate_per_kWh

def write_summary_to_record_file(last_date, new_reading, last_reading, renter_usage, total_bill, total_usage, rate_per_kWh, total_bill_in_rupees):
    try:
        with open("record.txt", "a") as file:
            file.write(f"============================================================\n\n")
            # Write the summary to the file
            file.write(f"Date of Last Meter Reading: {last_date.strftime('%Y-%m-%d')}\n")
            file.write(f"Current Date: {datetime.datetime.now().strftime('%Y-%m-%d')}\n\n")
            file.write(f"New unit: {new_reading}kWh\n")
            file.write(f"Old unit: {last_reading}kWh\n")
            file.write(f"Renter's unit: {renter_usage}kWh\n\n")
            file.write(f"Total bill: {total_bill}rupees\n")
            file.write(f"Total unit: {total_usage}kWh\n\n")
            file.write(f"Cost of 1 unit: {total_bill} / {total_usage} = {rate_per_kWh} rupees\n\n")
            file.write(f"Cost of Renters unit: {renter_usage} * {rate_per_kWh} = {total_bill_in_rupees}rupees\n")
    except Exception as e:
        print(f"Error: Unable to write summary to file: {e}")

def main():
    file_path = "meter_reading.txt"

    # Get the last meter reading and its corresponding date from the file
    last_reading, last_date = get_last_meter_reading(file_path)
    if last_reading is None or last_date is None:
        return

    print("Last Meter Reading Summary")
    print("==========================")
    print(f"Last Meter Reading: {last_reading} kWh")
    print(f"Date: {last_date.strftime('%Y-%m-%d')}")  # Print the date without time part
    print()

    # Prompt the user for the new meter reading
    try:
        new_reading = float(input("Enter the new meter reading: "))
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
        return

    # Write the new meter reading and current date to the file
    write_new_meter_reading(file_path, new_reading)

    try:
        total_usage = float(input("Total electricity usage in kWh(Billed units): "))
        total_bill = float(input("Total electricity bill in rupees(Amount): "))
        
        rate_per_kWh = total_bill / total_usage
        
        renter_usage = new_reading - last_reading
        
        total_bill_in_rupees = calculate_electricity_bill(renter_usage, rate_per_kWh) 
        
        # Write the summary to the record file
        write_summary_to_record_file(last_date, new_reading, last_reading, renter_usage, total_bill, total_usage, rate_per_kWh, total_bill_in_rupees)
                
        print("\nElectricity Bill Summary")
        print("========================")
        print(f"Renters Electricity Usage: {renter_usage} kWh")
        print(f"Rate per kWh: {rate_per_kWh:.2f} rupees")
        print(f"Renters Total Bill: {total_bill_in_rupees:.2f} rupees")
        
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":  
    main()
#okgit
#third commit?
#final commit?
git 