class LRTFareSystem:
    fares = {
        'Baclaran': {'Monumento': 16, 'Roosevelt': 20},
        'Monumento': {'Baclaran': 16, 'Roosevelt': 14},
        'Roosevelt': {'Baclaran': 20, 'Monumento': 14}
    }
    distances = {
        'Baclaran': {'Monumento': 12, 'Roosevelt': 19},
        'Monumento': {'Baclaran': 12, 'Roosevelt': 7},
        'Roosevelt': {'Baclaran': 19, 'Monumento': 7}
    }

    def calculate_fare(self, start_station, end_station):
        if start_station in self.fares and end_station in self.fares[start_station]:
            return self.fares[start_station][end_station]
        else:
            return None

    def calculate_distance(self, start_station, end_station):
        if start_station in self.distances and end_station in self.distances[start_station]:
            return self.distances[start_station][end_station]
        else:
            return None


def main():
    lrt = LRTFareSystem()

    start_station = input("Enter initial location: ")
    end_station = input("Enter destination: ")

    fare = lrt.calculate_fare(start_station, end_station)
    distance = lrt.calculate_distance(start_station, end_station)

    if fare is not None and distance is not None:
        print(f"Total distance traveled: {distance} Km")
        print(f"Total due fare: Php {fare}")
    else:
        print("Invalid input. Please check the station names and try again.")


if __name__ == "__main__":
    main()
