# File Injection Demonstration with Flask

This project demonstrates a vulnerability in a Flask web application that allows users to upload files without proper validation. 
This exposes the application to potential attacks, such as uploading malicious files (e.g., HTML or JavaScript) that can be executed by 
users accessing those files.

## Features

 - File Upload Vulnerability: A Flask app that allows users to upload any type of file without validation or checks, making it 
  susceptible to malicious file uploads (such as HTML, JavaScript, etc.).
 - Malicious File Execution: Demonstrates how an attacker can upload a file with embedded JavaScript and execute malicious scripts on the client side.
 - No File Type Restriction: No control on file types, allowing potentially dangerous files (e.g., .html, .js) to be uploaded.
 - No Authentication: The application lacks authentication, meaning anyone can upload files without restriction.

## Prerequisites

- Docker: Install Docker on your machine.
- Python: Ensure you have Python 3.8 or higher if you plan to run the app outside of Docker.

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
Use the web interface to upload this file. After the upload, the file will be accessible at the following URL:
```bash
http://localhost:5000/uploads/malicious.html
```
3. Access the Malicious File
Once the file is uploaded, navigate to its URL to test if the malicious JavaScript code is executed.
The browser should show an alert indicating the script has been executed.

## Observing the Results
After uploading the file and accessing it via the provided URL, you should observe the following:
If the file is executed: The alert should trigger, indicating that the JavaScript code inside the HTML file was executed. This demonstrates the vulnerability of the application to Cross-Site Scripting (XSS) attacks.
If the file is not executed: The application might be slightly secured by browser protections or you might have certain security configurations that prevent JavaScript execution.

## Risks and Mitigations
- This type of vulnerability is common in applications that do not properly sanitize or restrict uploaded files.
- Potential risks include:
    - XSS Attacks: Malicious files uploaded by attackers could execute harmful scripts on the user's browser, leading to information theft, 
    session hijacking, or defacement of the site.
    - Denial of Service: Large files or unexpected file formats might overwhelm the server or storage system, causing service disruptions.






