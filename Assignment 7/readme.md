# Flask Frontend & Express Backend Deployment on Kubernetes using Minikube

## 📌 Project Overview

This project demonstrates how to deploy a **Flask Frontend** and an **Express.js Backend** on a local Kubernetes cluster using **Minikube** and **Docker**.

The frontend communicates with the backend through a Kubernetes Service, showing how multiple applications can interact within a Kubernetes cluster.

---

## 🛠 Technologies Used

- Python 3.11
- Flask
- Node.js
- Express.js
- Docker
- Kubernetes
- Minikube
- kubectl

---

## 📂 Project Structure

```
flask-express-k8s/

├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── backend/
│   ├── app.js
│   ├── package.json
│   └── Dockerfile
│
├── k8s/
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── backend-deployment.yaml
│   └── backend-service.yaml
│
└── README.md
```

---

## ⚙ Prerequisites

Before running the project, install the following software:

- Docker Desktop
- Minikube
- kubectl
- Git

Verify installation:

```bash
docker --version
```

```bash
kubectl version --client
```

```bash
minikube version
```

---

## 🚀 Start Minikube

```bash
minikube start --driver=docker
```

Verify cluster:

```bash
kubectl get nodes
```

---

## 🐳 Build Docker Images

Build Flask image:

```bash
docker build -t flask-frontend ./frontend
``
