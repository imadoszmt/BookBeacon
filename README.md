# BookBeacon

BookBeacon is a web application designed to help book enthusiasts find rare and hard-to-locate books. Our platform serves as a bridge between readers and elusive literature, making the search for uncommon books easier and more efficient.

## Introduction

BookBeacon aims to solve the challenge of finding rare books by providing a centralized platform where users can search for uncommon titles and request assistance in locating books that are not in our database.

This project is part of the ALX Foundation Phase portfolio for the Full Stack Software Engineering program.

**Note:** This project is currently in development and not yet deployed.

- **Author LinkedIn**: [Imad Zalmat](https://www.linkedin.com/in/imad-zalmat-aa2940a9/)

## Features

Currently implemented:
- User authentication
- Book catalog browsing
- Search functionality for rare books

Features in development:
- Request system for books not in the catalog
- Notification system for when requested books are found

## Technical Stack

- Python 3
- Django web framework
- HTML/CSS
- JavaScript
- Bootstrap

## Installation

To set up BookBeacon locally, follow these steps:

1. Ensure you have Python 3 installed on your system.

2. Clone the repository:
   ```
   git clone https://github.com/imadoszmt/BookBeacon.git
   ```

3. Navigate to the project directory:
   ```
   cd bookbeacon
   ```

4. Create a virtual environment:
   ```
   python3 -m venv venv
   ```

5. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

6. Install Django:
   ```
   pip install django
   ```

7. Set up the database:
   ```
   python manage.py migrate
   ```

8. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

9. Run the development server:
   ```
   python manage.py runserver
   ```

The application should now be running at `http://localhost:8000`.

## Usage

After installation, you can use BookBeacon as follows:

1. Register for an account or log in if you already have one.
2. Use the search functionality to look for rare books in our catalog.
3. If a book is not found, you will be able to fill out a form to request assistance in locating the book (feature in development).
4. (Future feature) Receive notifications when requested books are found.

Please note that some features mentioned may not be fully implemented yet as the project is still in development.

## Contributing

We welcome contributions to BookBeacon! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## Related Projects

- [BookFinder](https://www.bookfinder.com/): A search engine for new and used books.
- [AbeBooks](https://www.abebooks.com/): An e-commerce platform for new, used, and rare books.
- [LibraryThing](https://www.librarything.com/): A cataloging and social networking site for book lovers.

## Project Status

This project is a prototype developed as part of the ALX Foundation Phase of the Full Stack Software Engineering program. It is not licensed for distribution or use beyond educational purposes.

