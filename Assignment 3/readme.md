# Flask API and MongoDB Atlas Integration

# Aim of the Assignment:
The aim of this assignment is to develop a Flask web application that provides a REST API to return JSON data from a backend file and allows users to submit data through a web form that is stored in MongoDB Atlas. The application should redirect to a success page after successful data submission and display an error message on the same page if any error occurs.

# Objectives

* To understand the basics of the Flask framework.
* To create REST API endpoints.
* To read JSON data from a backend file.
* To connect Flask with MongoDB Atlas.
* To insert user data into MongoDB Atlas.
* To create HTML forms using Flask templates.
* To implement success and error handling.
* To upload the project to GitHub.

---

# Software Requirements

* Operating System: Windows 10/11
* Python 3.x
* Visual Studio Code
* Flask
* PyMongo
* DNSPython
* Git
* GitHub Account
* MongoDB Atlas
* Google Chrome (or any web browser)

---

# Python Libraries Used

* Flask
* pymongo
* dnspython
* json (built-in library)

# Project Folder Structure

```
FlaskAssignment
│
├── app.py
├── data.json
├── requirements.txt
│
├── templates
│   ├── index.html
│   └── success.html
│
└── venv
```

---

# Implementation Steps

## Step 1: Create Project Folder

Created a project folder named **FlaskAssignment**.

---

## Step 2: Create Virtual Environment

Created a Python virtual environment to isolate project dependencies.

Command:

```
python -m venv venv
```

---

## Step 3: Activate Virtual Environment

Windows Command:

```
venv\Scripts\activate
```

After activation, `(venv)` appeared in the terminal.

---

## Step 4: Install Required Libraries

Installed Flask and MongoDB libraries.

Command:

```
pip install flask pymongo dnspython
```

---

## Step 5: Create Backend JSON File

Created a file named **data.json** containing sample student data.

Example:

```json
[
    {
        "id":1,
        "name":"Rahul",
        "course":"Python"
    },
    {
        "id":2,
        "name":"Amit",
        "course":"Flask"
    },
    {
        "id":3,
        "name":"Priya",
        "course":"MongoDB"
    }
]
```

---

## Step 6: Create MongoDB Atlas Cluster

* Created MongoDB Atlas account.
* Created Free M0 Cluster.
* Created Database User.
* Allowed Network Access (0.0.0.0/0).
* Copied MongoDB Connection String.

---

## Step 7: Create Flask Application

Created **app.py**.

The application performs the following tasks:

* Connects with MongoDB Atlas.
* Reads JSON file.
* Returns JSON data through `/api`.
* Accepts HTML form data.
* Stores submitted data into MongoDB Atlas.
* Redirects to success page.
* Displays error message if insertion fails.

---

## Step 8: Create HTML Templates

Created:

* index.html
* success.html

The index page contains the registration form.

The success page displays:

```
Data submitted successfully
```

---

## Step 9: Run Flask Application

Command:

```
python app.py
```

Output:

```
Running on http://127.0.0.1:5000
```

---

## Step 10: Test API

Opened:

```
http://127.0.0.1:5000/api
```

The application successfully returned JSON data from **data.json**.

---

## Step 11: Test Form Submission

Opened:

```
http://127.0.0.1:5000
```

Entered:

* Name
* Email

Clicked **Submit**.

The data was successfully inserted into MongoDB Atlas.

---

## Step 12: Verify MongoDB Atlas

Opened MongoDB Atlas.

Verified that the submitted document was stored successfully inside the **students** collection.

---

## Step 13: Upload Project to GitHub

Initialized Git repository.

Commands used:

```
git init

git add .

git commit -m "Initial Commit"

git branch -M main

git remote add origin https://github.com/yourusername/FlaskAssignment.git

git push -u origin main
```

---

# Source Code Snippets

## Flask API Route

```python
@app.route("/api")
def api():
    with open("data.json","r") as file:
        data=json.load(file)
    return jsonify(data)
```

---

## Form Submission Route

```python
@app.route("/submit",methods=["POST"])
def submit():
    try:
        name=request.form["name"]
        email=request.form["email"]

        collection.insert_one({
            "name":name,
            "email":email
        })

        return redirect(url_for("success"))

    except Exception as e:
        return render_template("index.html",error=str(e))
```

---

# Commands Used

Create Virtual Environment

```
python -m venv venv
```

Activate Environment

```
venv\Scripts\activate
```

Install Libraries

```
pip install flask pymongo dnspython
```

Run Flask Application

```
python app.py
```

Generate Requirements File (Optional)

```
pip freeze > requirements.txt
```

Initialize Git

```
git init
```

Add Files

```
git add .
```

Commit Changes

```
git commit -m "Initial Commit"
```

Push to GitHub

```
git push -u origin main
```

---

# Result

The Flask application was successfully developed. The `/api` route reads data from the backend JSON file and returns it as JSON. The HTML form successfully inserts user information into MongoDB Atlas. Upon successful insertion, the application redirects the user to the success page. In case of any error, the application displays the error message on the same page without redirection.

---

# Conclusion

This assignment provided practical experience in developing web applications using Flask and integrating them with MongoDB Atlas. It demonstrated how to create REST APIs, read data from JSON files, process form submissions, perform database operations, and implement proper success and error handling. Additionally, the project was successfully uploaded to GitHub for version control and future reference.
