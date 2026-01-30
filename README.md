# AWS_Image_Analyzer_Rekognition
## Project Overview
**AWS_Image_Analyzer_Rekognition** is a Python project that leverages **AWS Rekognition** to detect labels in images stored in an **S3 bucket**.  
The project analyzes multiple images, extracts labels with confidence scores, and stores the results in a **JSON**file.  

This repository demonstrates **AWS image analysis**, integration with S3, and automated data collection for image metadata.  

## Architecture Diagram
Below is the high-level architecture of the project:
<img width="1201" height="292" alt="image" src="https://github.com/user-attachments/assets/019990dd-aeb0-4774-bfcd-e98db5a63475" />
## Description:
1. Images are uploaded to an **S3 bucket**.  
2. Python script uses **Boto3** to call **AWS Rekognition DetectLabels API**.  
3. Labels and confidence scores are extracted.  
4. Results are saved to **JSON** and/or **CSV** files locally.  
## Screenshots

### Sample Images in S3
<img width="1352" height="636" alt="image" src="https://github.com/user-attachments/assets/4c15b849-3685-4f5e-b215-be5b623bab15" />

### Detected Labels Output (JSON)
<img width="1357" height="675" alt="image" src="https://github.com/user-attachments/assets/e229b0d2-7a2f-4bc3-8cfb-444e4009849e" />

## Installation & Setup

#### 1. Clone the repository:
   * git clone https://github.com/alimirza817/AWS_Image_Analyzer_Rekognition.git
   * cd AWS_Image_Analyzer_Rekognition
#### 2. Create a virtual environment and activate it:
   * python -m venv .venv
   * source .venv/Scripts/activate   # Windows  
   *  or for Linux/Mac: source .venv/bin/activate
#### 3. Install dependencies:
   * pip install boto3
#### 4. Make sure your AWS CLI is configured:
   * aws configure
   * Provide your Access Key, Secret Key, Region, and Output Format.
## Usage
#### 1. Place images in your S3 bucket.
#### 2. Update the bucket and images variables in detect_labels.py:
   * bucket = 'your-s3-bucket-name'
   * images = ['image1.jpg', 'image2.jpg']
#### 3. Run the script:
   * python detect_labels.py
#### 4. The script will generate:
   * rekognition_results.json → JSON file with detected labels.
