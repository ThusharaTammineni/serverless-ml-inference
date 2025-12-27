Serverless Machine Learning Inference (AWS Lambda Simulation)


Project Overview

This project demonstrates deployment of a lightweight machine learning inference

function using a serverless architecture similar to AWS Lambda behind API Gateway.



Due to AWS account limitations, the solution is implemented as a local simulation

that follows AWS Lambda’s execution model and request-response format.



The core inference logic is written to be fully compatible with AWS Lambda and

can be deployed directly without code changes.



---



Architecture

Client (curl / Postman)  

→ API Gateway (simulated using Flask)  

→ AWS Lambda Handler (lambda\_handler.py)  

→ Scikit-learn Model (model.pkl)  



---


Project Structure

ml\_inference\_local/

├── train\_model.py # Trains and saves ML model

├── model.pkl # Serialized scikit-learn model

├── lambda\_handler.py # AWS Lambda compatible handler

├── app.py # Local API Gateway simulation

├── requirements.txt # Lambda dependency list

└── README.md



---



Model Details

\- Algorithm: Logistic Regression

\- Dataset: Iris (scikit-learn built-in)

\- Purpose: Lightweight classification suitable for serverless deployment



---



How to Run Locally



1. Train the model

bash

python train\_model.py



2. Start the API (simulated API Gateway)
python app.py

Server starts at:



http://127.0.0.1:5000

API Invocation Example

curl -X POST http://127.0.0.1:5000/predict \\

-H "Content-Type: application/json" \\

-d '{"features":\[5.1,3.5,1.4,0.2]}'



Sample Response

{"prediction": 0}



**AWS Deployment Readiness**



The lambda\_handler.py file follows AWS Lambda handler specifications



JSON input and output format matches API Gateway integration



Dependencies are listed in requirements.txt



The project can be packaged into a Lambda deployment bundle without modification


