import boto3
import json

rekognition = boto3.client('rekognition')

bucket_name = "image-rekognition-ali"
images = ["person.jpg", "dog.jpg", "car.jpg"]

results = {}

for image in images:
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': image
            }
        },
        MaxLabels=10,
        MinConfidence=70
    )

    results[image] = [
        {
            "Label": label["Name"],
            "Confidence": round(label["Confidence"], 2)
        }
        for label in response["Labels"]
    ]

with open("rekognition_results.json", "w") as f:
    json.dump(results, f, indent=4)

print("✅ Rekognition analysis completed")
