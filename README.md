# alphabet-checker


## Coding Assessment


### Statement: API checks if a given string contains all the letters of the English alphabet, regardless of the case.
a. Endpoint: POST /check-alphabet/
b. Input: A JSON object containing a string
c. Output: A JSON object with a boolean field 
d. Code Strucuture:
alphabet-checker/
   main.py
   test_main.py
   requirement.txt
   README.md
e. main.py file contains the FastAPI application and the endpoint /check-alphabet/. The check_alphabet function validates the imput and checks whether all the letters of the alphabet are present. 
f. test_main.py contains test cases to validate the functionality of API. 
g.requirements.txt contains a list of python dependencies required to run the application.
 
#### Steps to Install Dependencies and Run the Application
1. Install Python: "python --version"
2. Install Dependencies: Create a virtual environment to isolate project dependencies "python -m venv venv"
3. Activate the virtual environment: "venv\Scripts\activate"
4. Install required dependencies: pip install -r requirements.txt
5. Run the application: "uvicorn main:app --reload", this will start the server on http://127.0.0.1.8000 by default. You can access swagger documentation at http://127.0.0.1.8000/docs.
6. Test the application: "pytest"
 
### Deployment in AWS
To deploy the FastAPI application with AWS.
 
Elastic Beanstalk: It simplifies the deployment and management. Supports Python-based applications and integrates seamlessly with FastAPI.
AWS CloudWatch: To monitor application logs, track metrics, and set alarms for resource utilization or application performance.
IAM: To manage permissions for Elastic Beanstalk.
 
1. Project Structure:
app/
   _init_.py
   main.py
   requirements.txt
.ebextensions/
   python.config
README.md
tests/
   test_main.py
runtime.txt
 
2. Create a requirements.txt file:
List all dependencies -
fastapi
uvicorn
pytest
httpx
 
3. Install the Elstic Beanstalk CLI and initialize "eb init" by navigating to the root of the project directory.
Choose the AWS Region
Select Python as platform
Use default Elastic Beanstalk aaplication name or specify.
 
4. Create an Environment, "eb create <environment-name>". This will automatically deploy the application.
This sets up -
An EC2 instance for hosting the application.
 
5. Deploy the code to Environment, "eb deploy".
 
6. Test the Deployment
Visit the application URL provided by Elastic Beanstalk and use tools like Postman to test the API endpoints.
