Explanation for app.py: This Python script is a Flask web application that provides a simple interface for uploading, searching, and downloading files stored in an AWS S3 bucket. It uses the Boto3 library to interact with AWS services, and you should replace 'YOUR_ACCESS_KEY_ID', 'YOUR_SECRET_ACCESS_KEY', and 'YOUR_BUCKET_NAME' with your actual AWS credentials and S3 bucket name. The application has four routes: /: Displays the main page with upload and search forms. /upload: Handles file uploads to S3. /search: Handles file searches in S3. /download/: Generates a pre-signed URL to download a file from S3. The application uses Flask templates to render the HTML pages, which are defined in the templates folder.

Explanation for index.html: This HTML file serves as the main user interface for your Flask application. It provides three main sections:
Upload Files: Allows users to input their email, a filename, and select a file to upload to the S3 bucket. Search Files: Enables users to search for files by email and search query. Search Results: Displays a list of search results (file names) with download links. The HTML file uses Flask's templating engine to insert dynamic content, such as search results. The {% for result in results %} loop iterates over search results received from the /search route in app.py.


Key pair name = important.pem
Public IP = 	44.218.208.54
region = us-east-1
