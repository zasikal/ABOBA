# MNIST
Classification of handwritten digits on a canvas (white on black, 28 x 28 pixels) using an SVC model (scikit-learn).
Built with FastAPI and containerized using Docker.

## Project structure

'''
main.py # FastAPI app
train.ipynb # Trains and saves the model
model.joblib # Saved model
requirements.txt # Python dependencies
sample.json # json file containing 5 samples of numbers
Dockerfile # container instructions
README.md # project description and run steps
'''

## Model
Dataset - MNIST (70000 images, 28x28 pixels - 784 parameters, normalization - dividing by 255.0)
Algorithm - SVC
Accuracy - 94%

## Starting steps

local:
'''Terminal
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
'''

docker:
'''Terminal
docker build -t mnist-svc-api .
docker run -p 8000:8000 mnist-svc-api
'''

## Verification
go to http://127.0.0.1:8000/docs
GET - Try it out - Execute
Output: "message": "ML API is running"
POST - Try it out - write one row from json file to Example Value - Execute
Output: prediction of the model
