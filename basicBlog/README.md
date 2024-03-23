Flask Blog Application by Osiro Asunde

This is a simple Flask blog application where users can log in, input blog entries, and view them.

Installation

	1.	Clone the repository to your local machine:

git clone https://github.com/yourusername/flask-blog.git


	2.	Install the required dependencies by running:

pip install -r requirements.txt



Usage

	1.	Set up environment variables:
	•	Create a .env file in the root directory of the project.
	•	Add your secret key for the Flask app:

Blogadminpassword=your_secret_key_here


	2.	Run the Flask application:

python app.py


	3.	Access the application in your web browser at http://localhost:81.
	4.	Log in with the predefined username and password:
	•	Username: Osiro
	•	Password: [your_secret_key_here]
	5.	Input your blog entries by filling out the form on the input page.
	6.	View all blog entries on the display page.

File Structure

	•	app.py: Main Flask application file containing routes and logic.
	•	templates/: Directory containing HTML templates for the application.
	•	static/: Directory for static assets such as images.

Dependencies

	•	Flask: Web framework for Python.
	•	Python-dotenv: Library for managing environment variables.

Notes

	•	Make sure to keep your secret key secure and never expose it publicly.

Let me know if there’s anything else you’d like to add or modify!
