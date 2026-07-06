# Version Control Git

# TodoProject

A simple Flask-based Todo Project created for Git and GitHub practical exercises. This project demonstrates Git branching, merging, rebasing, resetting, and basic Flask application development.

---

## Features

- Flask Web Application
- Home Page
- JSON API
- To-Do Form
- MongoDB Integration
- Git Branch Management
- Merge and Conflict Resolution
- Git Reset
- Git Rebase

---

## Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- MongoDB
- Git
- GitHub

---

## Project Structure

```
TodoProject/
│
├── app.py
├── requirements.txt
├── README.md
├── data.json
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd TodoProject
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000/
```

---

## API

### Home Page

```
GET /
```

Returns the Home page.

### JSON API

```
GET /api
```

Example Response

```json
{
    "name": "S Kumar",
    "course": "MCA"
}
```

### Submit Todo Item

```
POST /submittodoitem
```

Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| itemName | String | Name of Todo Item |
| itemDescription | String | Description of Todo Item |

---

## Git Practical Tasks

This repository demonstrates:

- Creating GitHub Repository
- SSH Authentication
- Branch Creation
- Commit Changes
- Merge Branches
- Resolve Merge Conflicts
- Git Reset (--soft)
- Git Rebase
- Push Changes to GitHub

---

## Branches

- main
- HP (or your username)
- HP_new
- master_1
- master_2

---

## Future Improvements

- User Authentication
- CRUD Operations
- Responsive UI
- Search Todo Items
- Edit/Delete Todo
- Deployment on Render or Railway

---

## Author

**S Kumar**

MCA Student

---

## License

This project is created for educational and practical learning purposes.
