# Flask + Node.js Docker Assignment

## 📌 Project Overview

This project demonstrates communication between a **Node.js (Express)** frontend and a **Flask (Python)** backend.

The frontend provides a form where users enter their details. The data is sent to the Flask backend using an HTTP POST request. The backend processes the data and returns a success response.

---

## 🛠 Technologies Used

### Frontend
- Node.js
- Express.js
- EJS
- Axios

### Backend
- Python
- Flask
- Flask-CORS

### DevOps
- Docker
- Docker Compose
- Git
- GitHub

---

## 📁 Project Structure

```
FlaskNodeDocker/
│
├── frontend/
│   ├── app.js
│   ├── package.json
│   ├── Dockerfile
│   └── views/
│       └── index.ejs
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/FlaskNodeDocker.git
```

Go to project folder

```bash
cd FlaskNodeDocker
```

---

# Backend Setup

Move to backend directory

```bash
cd backend
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Flask Server

```bash
python app.py
```

Backend runs on

```
http://127.0.0.1:5000
```

---

# Frontend Setup

Open another terminal.

Move to frontend directory

```bash
cd frontend
```

Install dependencies

```bash
npm install
```

Run Express Server

```bash
node app.js
```

Frontend runs on

```
http://localhost:3000
```

---

## 🚀 How it Works

1. Open the frontend in your browser.
2. Fill out the form.
3. Click **Submit**.
4. Express sends the data to Flask.
5. Flask processes the request.
6. Flask returns a success message.
7. Express displays the response.

---

## 🐳 Docker Files

The project contains

- Dockerfile (Frontend)
- Dockerfile (Backend)
- docker-compose.yml

These files allow containerizing the application.

---

## 📸 Output

### Frontend

- Form Page
- User enters Name, Email and Message

### Backend

Receives submitted data and prints it in the terminal.

Example

```
Received Data

Name : S Kumar
Email : skumar@gmail.com
Message : Hello Flask
```

---

## 📂 Git Ignore

```
node_modules/
__pycache__/
.vscode/
.env
```

---

## 👨‍💻 Author

**Name:** Sushil Kumar

**Course:** Computer Engineering

**Assignment:** Flask + Node.js Docker Integration

---

## 📄 License

This project is created for educational purposes only.
