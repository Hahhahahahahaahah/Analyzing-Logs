import os

logs_files = os.listdir("./logs")

all_warnings = 0
all_info = 0
all_errors= 0
for file in logs_files:
    errors = 0
    warning = 0
    info = 0
    print(f"Report for{file}")
    with open(f"./logs/{file}","r") as logfile:
        for line in logfile:
            if "ERROR" in line:
                errors += 1
            elif "WARNING" in line:
                warning += 1
            elif "INFO" in line:
                info += 1

    print(f"Errors: {errors}")
    print(f"Warnings: {warning}")
    print(f"Info: {info}")
    print()
    all_errors += errors
    all_warnings += warning
    all_info += info
print("----------------------")
print("Final Report")
print(f"Total Errors: {all_errors}")
print(f"Total Warning: {all_warnings}")
print(f"Total Errors: {all_info}")