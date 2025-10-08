\# ✈️ Flight Game – Python \& MariaDB Project



\## 🎯 Overview

\*\*Flight Game\*\* is a full-stack educational project built with \*\*Python\*\*, \*\*MariaDB\*\*, and soon \*\*HTML/JS frontend\*\*.  

It simulates a flight management game where users can register, log in, explore flights, and move between airports using real data.



This project was developed as part of the \*\*Metropolia University – Programming 1 (Python)\*\* course.



---



\## 🌐 Features

\- 🧍 \*\*User System:\*\* Secure register, login, and delete (with bcrypt hashing)

\- ✈️ \*\*Flights:\*\* List and add new scheduled flights

\- 🌍 \*\*Game Logic:\*\* Track player location, CO₂ usage, and goals

\- 🧩 \*\*Database:\*\* Real airport, country, and game tables from MariaDB

\- 💾 \*\*.env Support:\*\* Safe database credentials handling

\- 🐍 \*\*Modular \& Clean Code Structure\*\*



---



\## 🧱 Project Structure

/PythonProject1/

│

├── src/

│ ├── main.py # Main game menu

│ ├── db/

│ │ └── connection.py # Handles MariaDB connection

│ ├── models/

│ │ ├── user\_model.py

│ │ ├── flight\_model.py

│ │ ├── goal\_model.py

│ │ └── goal\_reached\_model.py

│ ├── services/

│ │ ├── user\_service.py

│ │ ├── flight\_service.py

│ │ └── game\_service.py

│ └── utils/

│ └── logger.py # Simple info/error logging

│

├── .env # Environment variables (DB credentials)

├── requirements.txt # All dependencies

└── README.md # Project documentation





---



\## ⚙️ Setup \& Run Locally



\### 1️⃣ Clone the repository

```bash

git clone https://github.com/Minoo-YH/Metropoli-ohjelmointi1-python-project-.git

cd Metropoli-ohjelmointi1-python-project-

git checkout Minoo-flightgame


reate & activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Create .env file

Inside your project folder, create a .env file with:

DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=flight_game

5️⃣ Verify MariaDB connection
& "C:\Program Files\MariaDB 12.0\bin\mysql.exe" -u root -p
USE flight_game;
SHOW TABLES;

6️⃣ Run the project
python -m src.main

🧠 Technologies Used

Python 3.10+

MariaDB 12

bcrypt — password hashing

python-dotenv — manage .env config

mysql-connector-python — database driver

🚀 Future Improvements

Add web frontend (HTML + JavaScript)

Visualize flight routes on a map

Fetch live weather & flight data via APIs

Extend sustainability scoring (CO₂ tracking)

👩‍💻 Author

Minoo YH
📍 GitHub Profile

🎓 Metropolia University of Applied Sciences

🪪 License

This project was created for educational purposes under Metropolia University’s Programming 1 course.
You are free to use and modify it with credit








