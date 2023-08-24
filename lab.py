class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team_name):
        team_matches = []
        for match in self.matches:
            if team_name in [match.team1, match.team2]:
                team_matches.append(match)
        return team_matches

    def search_by_location(self, location_name):
        location_matches = []
        for match in self.matches:
            if match.location == location_name:
                location_matches.append(match)
        return location_matches

    def search_by_timing(self, timing_name):
        timing_matches = []
        for match in self.matches:
            if match.timing == timing_name:
                timing_matches.append(match)
        return timing_matches

def main():
    flight_table = FlightTable()

    flight_table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    flight_table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    flight_table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    flight_table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    flight_table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    flight_table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Aryan Singh E22CSEU0457")
            team_name = input("Enter the team name: ")
            team_matches = flight_table.search_by_team(team_name)
            for match in team_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, Timing: {match.timing}")
            break
        elif choice == 2:
            print("Aryan Singh E22CSSEU0457")
            location_name = input("Enter the location: ")
            location_matches = flight_table.search_by_location(location_name)
            for match in location_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, Timing: {match.timing}")
            break
        elif choice == 3:
            print("Aryan Singh E22CSEU0457")
            timing_name = input("Enter the timing: ")
            timing_matches = flight_table.search_by_timing(timing_name)
            for match in timing_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, Timing: {match.timing}")
                break
        elif choice == 4:
            print("Aryan Singh E22CSEU0457")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
