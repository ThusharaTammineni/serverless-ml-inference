import json
import pickle

# Load the trained model (this simulates Lambda cold start)
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def lambda_handler(event, context=None):
    """
    AWS Lambda compatible handler function
    """

    # Get request body
    body = event.get("body")

    # If body comes as string (API Gateway behavior)
    if isinstance(body, str):
        body = json.loads(body)

    # Extract features
    features = body["features"]

    # Predict
    prediction = model.predict([features])

    # Return response in Lambda format
    return {
        "statusCode": 200,
        "body": json.dumps({
            "prediction": int(prediction[0])
        })
    }
