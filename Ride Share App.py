class RideShareApp:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.rides = []
        self.ride_history = []
        self.pending_rides = []

    def register(self):
        print("\n--- User Registration ---")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        employee_id = input("Enter your employee ID: ")
        password = input("Enter a password: ")
        self.users[email] = {
            'name': name,
            'phone': phone,
            'employee_id': employee_id,
            'password': password
        }
        print("\nRegistration successful! Please login to continue.")

    def login(self):
        print("\n--- User Login ---")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email in self.users and self.users[email]['password'] == password:
            self.current_user = self.users[email]
            print(f"\nLogin successful! Welcome, {self.current_user['name']}!")
        else:
            print("\nInvalid email or password. Please try again.")

    def book_ride(self):
        print("\n--- Book a Carpool Ride ---")
        pickup = input("Enter your pickup location: ")
        dropoff = input("Enter your drop-off location: ")
        time = input("Enter your preferred time: ")
        print("\nSearching for available carpool matches...")
        # Simulate a match found
        match = {
            'driver_name': 'Jane Smith',
            'vehicle_name': 'Maruti Swift',
            'vehicle_number': 'TN01AK0001',
            'pickup_time': time,
            'eta': '10 minutes'
        }
        print(f"\nMatch found!\nDriver Name: {match['driver_name']}\nVehicle_number: {match['vehicle_number']}\nVehicle_name: {match['vehicle_name']}\nPickup Time: {match['pickup_time']}\nETA: {match['eta']}")
        confirm = input("\nConfirm booking? (yes/no): ")
        if confirm.lower() == 'yes':
            self.pending_rides.append({
                'pickup': pickup,
                'dropoff': dropoff,
                'driver': match['driver_name'],
                'vehicle_name': match['vehicle_name'],
                'vehicle_number': match['vehicle_number'],
                'date': '2023-10-10',
                'status': 'Pending'
            })
            print("\nCarpool ride booked successfully! Your driver will confirm the ride soon.")

    def create_ride(self):
        print("\n--- Create a Carpool Ride ---")
        pickup = input("Enter your pickup location:")
        dropoff = input("Enter your drop-off location:")
        vehicle_name = input("Vehicle Name:")
        vehicle_number = input("Vehicle Number:")
        no_of_shares = input("No of shares:")
        start_time = input("Enter ride start time:")
        end_time = input("Enter estimated ride end time:")
        self.rides.append({
            'pickup': pickup,
            'dropoff': dropoff,
            'vehicle_name': vehicle_name,
            'vehicle_number': vehicle_number,
            'no_of_shares': no_of_shares,
            'start_time': start_time,
            'end_time': end_time,
            'driver': self.current_user['name'],
            'status': 'Available'
        })
        print("\nCarpool ride created successfully!")

    def view_ride_history(self):
        print("\n--- Ride History ---")
        for ride in self.ride_history:
            print(f"Ride from {ride['pickup']} to {ride['dropoff']}\nDriver: {ride['driver']}\nvehicle_number: {ride['vehicle_number']}\nDate: {ride['date']}\nStatus: {ride['status']}\n")

    def accept_ride(self):
        print("\n--- Accept the Carpool Ride ---")
        if self.pending_rides:
            for idx, ride in enumerate(self.pending_rides):
                print(f"{idx + 1}. Ride from {ride['pickup']} to {ride['dropoff']}")
            choice = int(input("\nSelect a ride to accept (enter the number): "))
            selected_ride = self.pending_rides.pop(choice - 1)
            selected_ride['status'] = 'Completed'
            self.ride_history.append(selected_ride)
            print("\nCarpool ride accepted successfully!")
        else:
            print("\nNo pending rides to accept.")

    def logout(self):
        print("\nLogout successful. Thank you for using Hexaware RideShare Carpool!")
        self.current_user = None

    def main_menu(self):
        while True:
            if not self.current_user:
                print("\n==========================================")
                print("Welcome to Hexaware RideShare Carpool App")
                print("==========================================")
                print("\n1. Register\n2. Login\n3. Exit")
                option = input("\nPlease select an option: ")
                if option == '1':
                    self.register()
                elif option == '2':
                    self.login()
                elif option == '3':
                    break
                else:
                    print("\nInvalid option. Please try again.")
            else:
                print("\n==========================================")
                print("Hexaware RideShare Carpool Menu")
                print("==========================================")
                print("\n1. Book a Carpool Ride\n2. Create a Carpool Ride\n3. View Ride History\n4. Accept the Carpool Ride\n5. Logout")
                option = input("\nPlease select an option: ")
                if option == '1':
                    self.book_ride()
                elif option == '2':
                    self.create_ride()
                elif option == '3':
                    self.view_ride_history()
                elif option == '4':
                    self.accept_ride()
                elif option == '5':
                    self.logout()
                else:
                    print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    app = RideShareApp()
    app.main_menu()