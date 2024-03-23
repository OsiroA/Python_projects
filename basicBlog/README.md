Flask Blog Application by Osiro Asunde

This Flask blog application allows users to log in, input blog entries, and view them. It serves as a simple platform for users to share their thoughts, ideas, and experiences through blog posts.

Purpose

The purpose of this project is to provide a user-friendly interface for creating and managing blog entries. It simplifies the process of blogging by offering a straightforward input form and an organized display of blog entries.

Technologies and Libraries Used

	•	Flask: Web framework for Python that provides tools, libraries, and patterns to build web applications.
	•	Python-dotenv: Library for managing environment variables.
	•	HTML/CSS: Used for creating the structure and styling of the web pages.
	•	Git: Version control system for tracking changes in the project.

Installation

	1.	Clone the repository to your local machine:

git clone https://github.com/OsiroA/Python_projects.git


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
	•	Password: [your_secret_key_here] - attach your email to a commit in a pull request to get this
	5.	Input your blog entries by filling out the form on the input page.
	6.	View all blog entries on the display page.

File Structure

	•	app.py: Main Flask application file containing routes and logic.
	•	templates/: Directory containing HTML templates for the application.
	•	static/: Directory for static assets such as images.

Code Repository

The code repository for this project is available at [Github](https://github.com/OsiroA/Python_projects/tree/main/basicBlog)

Challenges Faced

One challenge faced during the project was implementing user authentication and authorization. This was overcome by utilizing Flask’s built-in features for handling user sessions and creating a secure login system.
