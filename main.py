import time
import os

with open("logs/vehicles.txt") as file:
    vehicles = file.readlines()
with open("logs/vehicles.txt") as file:
    vehicles_text = file.read().split()

vehicle = input(f"Which vehicle did you work on: {vehicles_text} or other?\n")
mileage = input("Mileage: ")
work_done = input("Work done: ")

mileage_time_date = time.strftime(f"{mileage}mi_Time_%H_%M_%S_Date_%m_%d_%Y")

if (vehicle + "\n") in vehicles:

    filepath = f"logs/{vehicle}/{mileage_time_date}.txt"
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
with open(filepath) as log:
    print(log.read())


 
