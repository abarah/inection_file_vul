# File Injection Demonstration with Flask

This project demonstrates a vulnerability in a Flask web application that allows users to upload files without proper validation. 
This exposes the application to potential attacks, such as uploading malicious files (e.g., HTML or JavaScript) that can be executed by 
users accessing those files.

## Features

 -File Upload Vulnerability: A Flask app that allows users to upload any type of file without validation or checks, making it 
susceptible to malicious file uploads (such as HTML, JavaScript, etc.).
 -Malicious File Execution: Demonstrates how an attacker can upload a file with embedded JavaScript and execute malicious scripts on the client side.
 -No File Type Restriction: No control on file types, allowing potentially dangerous files (e.g., .html, .js) to be uploaded.
No Authentication: The application lacks authentication, meaning anyone can upload files without restriction.

## Prerequisites

Docker: Install Docker on your machine.
Python: Ensure you have Python 3.8 or higher if you plan to run the app outside of Docker.

## Installation

1. Clone the Repository
```bash
git clone https://github.com/abarah/inection_file_vul.git
cd inection_file_vul
```
2.Build the Docker Image
```bash
docker build -t flask-vulnerable-upload .
```
3. Run the Docker Container
```bash
docker run -d -p 5000:5000 flask-vulnerable-upload
```
The application will now be running and accessible at http://127.0.0.1:5000.

## Usage

1. Access the Application
Open your browser and navigate to the following URL:
```bash
http://127.0.0.1:5000
```
2. Test the Vulnerability
You can now attempt to upload a file. Below is an example of how you can test uploading a malicious .html file containing a simple JavaScript alert.

Example: Malicious File Upload
Create a malicious file named malicious.html with the following content:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Malicious File</title>
</head>
<body>
    <script>
        alert('The malicious script was executed!');
    </script>
</body>
</html>

```
Example 1: List Running Containers
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"ps\"}" http://127.0.0.1:5000/vulnerable
```
Example 2: List All Containers (Including Stopped)
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"ps -a\"}" http://127.0.0.1:5000/vulnerable
```
Example 3: Inspect a Container
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"inspect <container_id>\"}" http://127.0.0.1:5000/vulnerable
```
Example 4: Execute a Command Inside a Container (e.g., bash)
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"exec <container_id> bash\"}" http://127.0.0.1:5000/vulnerable
```
Example 5: Stop a Container
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"stop <container_id>\"}" http://127.0.0.1:5000/vulnerable
```
You can replace <container_id> with actual IDs obtained from the ps command.

## Observing the Results
After sending requests, check the Flask server logs to observe the Docker commands being executed and their results. If the API is exposed to the public, an attacker could remotely execute arbitrary commands on the host machine, compromising security.






