def calculate_cooling_load(area, occupants, building_type, outdoor_temp, indoor_temp):
    # Cooling Load based on building type
    if building_type.lower() == 'residential':
        cooling_load = 100 * occupants
    elif building_type.lower() == 'commercial':
        cooling_load = 150 * occupants
    else:
        print("Invalid building type entered.")
        return None
    
    # Heat transfer due to conduction
    U = 30  # Overall heat transfer coefficient (W/m²°C)
    Q_conduction = U * area * (outdoor_temp - indoor_temp)
    
    # Sensible Cooling Load
    sensible_cooling_load = Q_conduction + cooling_load
    return sensible_cooling_load

# Input from the user
area = float(input("Enter the area of the building (in square meters): "))
occupants = int(input("Enter the number of occupants in the building: "))
building_type = input("Enter the type of building (residential, commercial, etc.): ")
outdoor_temp = float(input("Enter the outdoor temperature (in Celsius): "))
indoor_temp = float(input("Enter the indoor desired temperature (in Celsius): "))

# Calculate and display the sensible cooling load
sensible_cooling_load = calculate_cooling_load(area, occupants, building_type, outdoor_temp, indoor_temp)
if sensible_cooling_load is not None:
    print("Sensible Cooling Load:", sensible_cooling_load, "Watts")
