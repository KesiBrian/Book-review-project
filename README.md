BOOK REVIEW PROJECT

Welcome to the Book Review Project! This full-stack web application allows users to sign up, log in, read reviews, and post their own reviews for books. Users can also rate books and explore others' opinions. The app is built with a Flask API backend and a React frontend.

FEATURES
.User Authentication: Sign up, log in, and manage user sessions.
.Review System: Users can read, post, and rate book reviews.
.CRUD Operations: Full Create, Read, Update, Delete functionality for books and reviews.
.Profile Management: View and update user profile details.
.Responsive Design: The app is fully responsive, making it accessible on various devices.

TECH STACK
Backend

.Flask: Python-based web framework for the backend.
.Flask-RESTful: To handle API routes.
.Flask-SQLAlchemy: ORM to interact with the database.
.Flask-Migrate: For handling database migrations.
.Flask-CORS: For enabling Cross-Origin Resource Sharing between frontend and backend.
.JWT Authentication: For secure user sign-up and login.

Frontend
.React: Frontend framework for building dynamic user interfaces.
.React Router: For client-side routing to navigate between pages.
.Formik: For building forms and handling validation.
.CSS/SCSS: For styling the application with a modern and clean look.

Setup
Prerequisites
.Python 3.8+
.Node.js 14+
.pipenv (For managing Python dependencies)
.npm (For managing Node dependencies)

Backend Setup
1.Clone the repository:

bash
Copy
git clone https://github.com/your-username/book-review-project.git
cd book-review-project/server

2.Install the backend dependencies:
bash
Copy
pipenv install
pipenv shell

3.Run the Flask app:
bash
Copy
python app.py

4.The backend should now be running on http://localhost:5555.

Frontend Setup
1.Navigate to the client directory:
bash
Copy
cd ../client

2.Install the frontend dependencies:
bash
Copy
npm install

3.Run the React app:
bash
Copy
npm start

4.The frontend should now be running on http://localhost:3000.

Database Setup
1.Initialize the database by running the following commands:
bash
Copy
cd server
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

2.Seed the database with some initial data:
bash
Copy
python seed.py

3.Your database should now be populated with some initial books and reviews!

Usage
1.Sign Up: Create an account using the "Sign Up" form.
2.Log In: Use the "Log In" form to authenticate and access your profile.
3.View Books & Reviews: Browse through books and read the reviews posted by others.
4.Post a Review: Write and submit your own review for a book.
5.Rate a Book: Rate a book on a scale of 1-5 stars.
