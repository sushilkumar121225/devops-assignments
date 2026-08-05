# Flask Backend and Express Frontend Deployment on AWS EC2 using Terraform

## Project Overview

This project demonstrates the deployment of a Flask backend and an Express frontend on an Amazon EC2 instance using Terraform. The infrastructure is provisioned on AWS, and both applications are configured to run automatically.

---

## Technologies Used

- Amazon Web Services (AWS)
- Amazon EC2
- Terraform
- Python 3
- Flask
- Node.js
- Express.js
- Git
- Linux (Amazon Linux 2023)

---

## Project Structure

```
aws-terraform-project/

├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── provider.tf
│
├── flask/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── express/
│   ├── app.js
│   ├── package.json
│   └── Dockerfile
│
├── user_data.sh
│
└── README.md
```

---

## Prerequisites

Install the following software:

- AWS CLI
- Terraform
- Git
- Python 3
- Node.js
- Visual Studio Code

Verify installation:

```bash
aws --version
terraform version
git --version
python --version
node -v
npm -v
```

---

## AWS Configuration

Configure AWS CLI:

```bash
aws configure
```

Enter:

- AWS Access Key ID
- AWS Secret Access Key
- Region
- Output format

Example:

```
AWS Access Key ID: ****************
AWS Secret Access Key: ****************
Default region: ap-south-1
Default output format: json
```

---

## Create EC2 Key Pair

Create an EC2 Key Pair from the AWS Console.

Example:

```
terraform-key
```

Download:

```
terraform-key.pem
```

Store it securely.

---

## Initialize Terraform

```bash
terraform init
```

---

## Validate Configuration

```bash
terraform validate
```

---

## Preview Infrastructure

```bash
terraform plan
```

---

## Deploy Infrastructure

```bash
terraform apply
```

Type:

```
yes
```

Terraform will create:

- EC2 Instance
- Security Group
- Networking Resources

---

## Connect to EC2

```bash
ssh -i "terraform-key.pem" ec2-user@<PUBLIC-IP>
```

Example:

```bash
ssh -i "terraform-key.pem" ec2-user@13.233.100.120
```

---

## Install Required Packages

```bash
sudo dnf update -y

sudo dnf install git -y

sudo dnf install python3 python3-pip -y

pip3 install flask

sudo dnf install nodejs npm -y

node -v

npm -v
```

---

## Run Flask Backend

```bash
cd flask

python3 app.py
```

Flask runs on:

```
http://<PUBLIC-IP>:5000
```

---

## Run Express Frontend

```bash
cd express

npm install

node app.js
```

Express runs on:

```
http://<PUBLIC-IP>:3000
```

---

## Verify Deployment

Check both applications in your browser:

### Flask Backend

```
http://<PUBLIC-IP>:5000
```

Expected Output:

```
Hello from Flask Backend
```

### Express Frontend

```
http://<PUBLIC-IP>:3000
```

Expected Output:

```
Hello from Express Backend
```

---

## Useful Terraform Commands

Initialize:

```bash
terraform init
```

Validate:

```bash
terraform validate
```

Plan:

```bash
terraform plan
```

Apply:

```bash
terraform apply
```

Show Resources:

```bash
terraform show
```

Destroy Infrastructure:

```bash
terraform destroy
```

---

## Screenshots Required

Include the following screenshots:

- AWS EC2 Instance Running
- Terraform Init
- Terraform Plan
- Terraform Apply
- SSH Login
- Flask Application Running
- Express Application Running
- AWS Security Group
- Public IP Access
- GitHub Repository

---

## Author

**Name:** Sushil Kumar

**University:** Marwadi University

**Course:** B.Tech Computer Engineering

**Project:** Flask Backend and Express Frontend Deployment on AWS EC2 using Terraform

---

## License

This project is created for educational and academic purposes only.
