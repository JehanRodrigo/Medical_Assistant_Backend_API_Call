Google Cloud:

Create Account
Cloud Build 
Cloud Run
CLI Configuration
https://cloud.google.com/sdk/docs/install
gcloud init
gcloud config set project <your project name>
gcloud auth login
gcloud artifacts repositories create deployementbiogpt --repository-format=docker --location=asia-south1 --description="biogpt deployment" --immutable-tags --async
