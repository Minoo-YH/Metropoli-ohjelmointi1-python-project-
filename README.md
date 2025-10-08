# Flight Game

## Project Overview
Flight Game is a simulation of a flight booking system .

The main goal of the game is to allow users to travel to destinations, earn membership status based on distance traveled (KM), and eventually unlock offers and benefits such as free trips.

The game is built in Python and designed with a modular structure to make future enhancements easier.

---

## Project Goals
- Implement a functional flight booking simulation.
- Track user travel distance and membership levels (Silver, Gold, Diamond).
- Prepare for future improvements like payment integration and dynamic offers.

---


## Gameplay Instructions

### 1. Registration & Login  (Still in Progress — Operating in Test Environment)
- Register: Enter your name, email, and password.
- Login: Use credentials to log in. Required to retrieve your user ID and username.

### 2. Main Menu
After logging in, you'll see:
1. Choose Your Destination to Travel
2. View User Info
3. Logout
4. Delete User
5. Exit

### 3. Gameplay Details
Your profile displays:
- User ID
- Username
- KM traveled
- Battery level
- Membership status

### 4. Logout
Logs you out so another user can log in or register.

### 5. Delete User
Permanently deletes your account and all related data.

### 6. Exit
Closes the game.

---

## Database Solutions
- Built on a pre-existing school database with a custom added user table.
- The table structure and ER diagram will be provided later.
    
    FLIGHT_GAME/flight_game_users
---

## Future Development Ideas
- Payment System: Allow users to book trips without registering with extra payment, and give discounts for members.
- Modify airport table to split airports by city for more realistic simulation.
- Build a front-end using React.js and CSS for a graphical interface.

---

##  Code Structure
```
FLIGHT_GAME/
│
├── src/
│   ├── context/
│   │   ├── run.py
│   │   └── utils.py
│   │
│   ├── db/
│   │   ├── flight_game.py
│   │   └── flight_game.sql
│   │
│   ├── Queries/
│   │   ├── airports.py
│   │   ├── user.py
│   │   └── (other SQL queries)
│   │
│   └── main.py
│
├── .env
```

---

## Dependencies
- Python 3.x
- bcrypt
- math
- dotenv
- mysql-connector-python
- os

Install dependencies:
```bash
pip install bcrypt python-dotenv mysql-connector-python
```

---

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/Minoo-YH/Metropoli-ohjelmointi1-python-project-.git
```
2. Navigate to the project directory:
```bash
cd FLIGHT_GAME/src
```
3. Run the game:
```bash
python main.py
```

---

## License
This project is for academic purposes.
