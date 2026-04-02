# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework in Python. In this assignment, you will practice defining routes, handling HTTP methods, working with JSON data, and organizing basic backend logic for a class enrollment system.

## 📝 Tasks

### 🛠️	Create the FastAPI Application

#### Description
Set up a FastAPI application that exposes a small API for class enrollment data. Create the application instance and define the basic routes needed to test that the server is running.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Include a root endpoint such as GET / that returns a welcome message.
- Include a GET endpoint to return all enrollment records.
- Return data in JSON format.


### 🛠️	Implement CRUD Endpoints

#### Description
Add endpoints to create, update, and delete enrollment records. Each record should include at least a student name, student ID, and class name.

#### Requirements
Completed program should:

- Implement a POST endpoint to create a new enrollment record.
- Implement a PUT endpoint to update an existing enrollment record by student ID.
- Implement a DELETE endpoint to remove an enrollment record by student ID.
- Return a clear error message when a requested record does not exist.
- Use an in-memory list or dictionary to store enrollment data.