🧩 Flask REST API – User Management
This project demonstrates a simple RESTful API built using Flask that performs basic CRUD (Create, Read, Update, Delete) operations on an in-memory users dictionary.

📌 Features
GET /users/<user_id> – Get details of a specific user
POST /users – Create a new user
PUT /users/<user_id> – Update an existing user's details
DELETE /users/<user_id> – Delete a user


🛠️ Technologies Used
Python 3
Flask 2.3.3
requests
jsonify

🚀 Getting Started

1. Clone the Repository
git clone https://github.com/your-username/flask-user-api.git

2. Install Dependencies
pip install requests
pip insatll jsonify

4. Run the Flask App
python app.py
The API will run at: http://127.0.0.1:5000/


📬 API Endpoints

GET	/users/<user_id>	Fetch user by ID

POST	/users	Add a new user

PUT	/users/<user_id>	Update user details

DELETE	/users/<user_id>	Delete a user
