'''
# TaskFlow API

TaskFlow is a Django-based API for managing tasks, featuring user authentication and secure access control. It provides endpoints for creating, retrieving, updating, and deleting tasks, ensuring that users can only access their own tasks. The project is built with Django Rest Framework (DRF) and adheres to RESTful design principles.

## Features

- **Task Management**: Users can create, view, update, and delete their tasks.
- **User Authentication**: Includes login, logout, and registration functionality using Django's built-in authentication system.
- **Secure Access**: Tasks are scoped to individual users.

## Technical Requirements

### 1. Database
- Uses Django ORM to interact with the database.
- Models for `Task` and `User`.
- Each user has access to their own tasks only.

### 2. Authentication
- Implements Django’s built-in authentication system.

### 3. API Design
- Built with Django Rest Framework (DRF).
- Follows RESTful design principles with appropriate HTTP methods (GET, POST, PUT, DELETE).
- Includes error handling and proper HTTP status codes.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- A virtual environment (recommended)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/blessingebele/TaskFlow.git
   cd TaskFlow
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

Access the API at `BlessingEbele.pythonanywhere.com/`.

## API Endpoints

### Authentication
  Basic Authentication

### Tasks
- `GET /api/tasks/` – List all tasks for the authenticated user.
- `POST /api/tasks/` – Create a new task.
- `GET /api/tasks/<id>/` – Retrieve a single task.
- `PUT /api/tasks/<id>/` – Update a task.
- `DELETE /api/tasks/<id>/` – Delete a task.

## Deployment
 - PythonAnywhere
### Local Development
- Use the built-in Django development server.

### Production
- Deploy on hosting platforms like [PythonAnywhere](https://www.pythonanywhere.com/).

#### Steps for Deployment on PythonAnywhere
1. Upload your project files or clone the repository.
2. Set up a virtual environment and install dependencies.
3. Configure the WSGI file and set up static files.
4. Migrate the database and test the application.

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the BlessingEbele.pythonanywhere.com (LICENSE) file for details.

## Acknowledgments

- Django Rest Framework documentation.
- PythonAnywhere for hosting.
- Open-source libraries used in this project.
