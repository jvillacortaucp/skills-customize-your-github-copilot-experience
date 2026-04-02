from fastapi import FastAPI, HTTPException


app = FastAPI()

enrollments = [
    {"student_id": "S001", "student_name": "Alice", "class_name": "Biology"},
    {"student_id": "S002", "student_name": "Ben", "class_name": "Computer Science"},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the class enrollment API"}


@app.get("/enrollments")
def get_enrollments():
    return enrollments


@app.post("/enrollments")
def create_enrollment(enrollment: dict):
    enrollments.append(enrollment)
    return enrollment


@app.put("/enrollments/{student_id}")
def update_enrollment(student_id: str, updated_enrollment: dict):
    for index, enrollment in enumerate(enrollments):
        if enrollment["student_id"] == student_id:
            enrollments[index] = updated_enrollment
            return updated_enrollment
    raise HTTPException(status_code=404, detail="Enrollment not found")


@app.delete("/enrollments/{student_id}")
def delete_enrollment(student_id: str):
    for index, enrollment in enumerate(enrollments):
        if enrollment["student_id"] == student_id:
            deleted = enrollments.pop(index)
            return deleted
    raise HTTPException(status_code=404, detail="Enrollment not found")