# final-drill-faults-api


# 🎓 IT6 Final Drill – Student Fault Tracking API

This project is part of the final drill for IT6, where I enhanced a Flask-based School Management System by implementing a REST API feature for tracking student faults (violations). The feature supports full CRUD operations and aligns with the goal of managing and monitoring student behavior.

---

## 🧠 Original Project Purpose

The original School Management System manages student records, registrations, and academic tracking. My enhancement adds the ability to:

- Record student violations (faults)
- View all reported faults
- Update fault status (e.g., resolved)
- Delete resolved or incorrect entries

---

## 🚀 New Feature: REST API for Student Faults

### ✅ Functionalities:
- Full **CRUD** support via HTTP methods
- JSON request and response format
- Proper error/status handling (`200`, `201`, `404`)
- Clean modular code using Blueprints

---

## 🛠 Technologies Used
- Python 3.x
- Flask
- Flask-SQLAlchemy
- unittest (for testing)
- Postman (for manual API testing)

---

## 📚 API Endpoints

| Method | Endpoint            | Description             |
|--------|---------------------|-------------------------|
| POST   | `/api/faults/`      | Create a new fault      |
| GET    | `/api/faults/`      | List all faults         |
| PUT    | `/api/faults/<id>`  | Update a fault by ID    |
| DELETE | `/api/faults/<id>`  | Delete a fault by ID    |

### 📥 Sample JSON Request:
```json
{
  "student_id": 1,
  "description": "Cheating in exam",
  "date_reported": "2025-05-29",
  "resolved": false
}
```

---

## ✅ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/sheenaaam/final-drill-faults-api.git
cd final-drill-faults-api
```

## GitHub Repository and Branch

- Original Repository : https://github.com/mostafa-hashhash/School-Managment-System.git
- My Repository with Feature Branch: https://github.com/sheenaaam/final-drill-faults-api.git 


### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python main.py
```

### 4. Run tests
```bash
python tests.py
```

---

## 🧪 Testing

Testing was done using `unittest`. It covers:

- Creating a fault
- Getting all faults
- Updating a non-existent fault (negative case)
- Deleting a non-existent fault (negative case)

✅ All tests passed.


---

## 👩‍💻 Author

**Name:** Sheenaaam  
**Course:** IT6  
**Date:** May 31, 2025

---

## 📎 Notes

- Follows RESTful principles
- All changes are committed in the `main` branch
- Feature is self-contained and modular (inside `api/faults.py`)
