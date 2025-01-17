from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class RideShareApp:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.rides = []
        self.ride_history = []
        self.pending_rides = []

rideshare_app = RideShareApp()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        employee_id = request.form['employee_id']
        password = request.form['password']
        rideshare_app.users[email] = {
            'name': name,
            'phone': phone,
            'employee_id': employee_id,
            'password': password
        }
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email in rideshare_app.users and rideshare_app.users[email]['password'] == password:
            rideshare_app.current_user = rideshare_app.users[email]
            return redirect(url_for('dashboard'))
        else:
            return "Invalid email or password. Please try again."
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not rideshare_app.current_user:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=rideshare_app.current_user)

@app.route('/book_ride', methods=['GET', 'POST'])
def book_ride():
    if not rideshare_app.current_user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        pickup = request.form['pickup']
        dropoff = request.form['dropoff']
        time = request.form['time']
        match = {
            'driver_name': 'Jane Smith',
            'vehicle_name': 'Maruti Swift',
            'vehicle_number': 'TN01AK0001',
            'pickup_time': time,
            'eta': '10 minutes'
        }
        confirm = request.form['confirm']
        if confirm.lower() == 'yes':
            rideshare_app.pending_rides.append({
                'pickup': pickup,
                'dropoff': dropoff,
                'driver': match['driver_name'],
                'vehicle_name': match['vehicle_name'],
                'vehicle_number': match['vehicle_number'],
                'date': '2023-10-10',
                'status': 'Pending'
            })
            return "Carpool ride booked successfully! Your driver will confirm the ride soon."
    return render_template('book_ride.html')

@app.route('/create_ride', methods=['GET', 'POST'])
def create_ride():
    if not rideshare_app.current_user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        pickup = request.form['pickup']
        dropoff = request.form['dropoff']
        vehicle_name = request.form['vehicle_name']
        vehicle_number = request.form['vehicle_number']
        no_of_shares = request.form['no_of_shares']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        rideshare_app.rides.append({
            'pickup': pickup,
            'dropoff': dropoff,
            'vehicle_name': vehicle_name,
            'vehicle_number': vehicle_number,
            'no_of_shares': no_of_shares,
            'start_time': start_time,
            'end_time': end_time,
            'driver': rideshare_app.current_user['name'],
            'status': 'Available'
        })
        return "Carpool ride created successfully!"
    return render_template('create_ride.html')

@app.route('/ride_history')
def ride_history():
    if not rideshare_app.current_user:
        return redirect(url_for('login'))
    return render_template('ride_history.html', rides=rideshare_app.ride_history)

@app.route('/logout')
def logout():
    rideshare_app.current_user = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
