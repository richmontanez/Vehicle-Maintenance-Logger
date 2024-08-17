import time
import os
import pathlib


if not os.path.exists("logs"):
    os.mkdir("logs")

    with open("logs/vehicles.txt", "w") as new_text:
        new_text.writelines("")

while 1:
    with open("logs/vehicles.txt") as file:
        vehicles = file.readlines()

    vehicles_string = "".join(vehicles)
    garage = vehicles_string or "(garage is empty)\n"

    vehicle = input(f"Current Garage:\n {garage}"
                    f"Enter the name of the vehicle worked on or type 'x' to stop the program: ").strip()

    if vehicle == "x":
        break

    mileage = input("Mileage: ")
    work_done = input("Work done: ")

    mileage_time_date = time.strftime(f"{mileage}mi_Time_%H_%M_%S_Date_%m_%d_%Y")

    if (vehicle + "\n") in vehicles:

        filepath = "logs/{vehicle}/{mileage_time_date}.txt"
    else:
        with open("logs/vehicles.txt") as current_vehicles:
            current = current_vehicles.readlines()
        current.append(vehicle + "\n")
        with open("logs/vehicles.txt", "w") as new_vehicle_list:
            new_vehicle_list.writelines(current)

        os.mkdir(f"logs/{vehicle}")

        with open(f"logs/{vehicle}/{mileage_time_date}.txt", "w") as new_log:
            new_log.write(f"logs/{vehicle}/{mileage_time_date}.txt")

        filepath = f"logs/{vehicle}/{mileage_time_date}.txt"

    with open(filepath, "w") as f_write:
        f_write.writelines(f"Work done: {work_done}\n")