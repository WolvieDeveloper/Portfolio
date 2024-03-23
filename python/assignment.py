def calculate_lrt_fare():
    print("\nWelcome to LRT Fare Calculator\n")
    
    stations = ["Roosevelt", "Balintawak", "Yamaha Monument", "5th Avenue", "R. Papa", "Abad Santos", "Blumentritt", "Tayuman", "Bambang", "Doroteo Jose", "Carriedo", "Central Terminal", "United Nations", "Pedro Gil", "Quirino", "Vieto Cruz", "Gil Puyat", "Libertad", "EDSA", "Baclaran"]
    station_distances = [469, 818, 601, 850, 683, 640, 627, 956, 565, 567, 527, 501, 536, 733, 493, 756, 892, 1816, 1573]

    # Display stations
    print("Stations:\n")
    for i, station in enumerate(stations):
        print(f"{i+1}. {station}")
    
    while True:
        try:
            start_station = int(input("\nEnter Current Station Number: "))
            destination_station = int(input("Enter Destination Station Number: "))
            if start_station < 1 or start_station > len(stations) or destination_station < 1 or destination_station > len(stations):
                raise ValueError("Invalid station number. Please enter a number within range.")
            break
        except ValueError as ve:
            print(ve)
    
    start_index = start_station - 1
    dest_index = destination_station - 1
    total_distance = abs(station_distances[start_index] - station_distances[dest_index]) / 1000
    total_fare = 13.21 + max(total_distance - 1, 0) * 1.23

    print("\nCurrent Station: ", stations[start_index])
    print("Destination: ", stations[dest_index])
    print("Total Distance (Km): ", total_distance, " Km")
    print("Total Fare: Php", total_fare)


if __name__ == "__main__":
    calculate_lrt_fare()
