Google Cloud:

* Create Account
* Cloud Build 
* Cloud Run
* CLI Configuration
* https://cloud.google.com/sdk/docs/install
* gcloud init
* gcloud config set project <your project name>
* gcloud auth login
* gcloud artifacts repositories create deployementbiogpt --repository-format=docker --location=asia-south1 --description="biogpt deployment" --immutable-tags --async
 gcloud auth configure-docker asia-south1-docker.pkg.dev
 gcloud builds submit --tag asia-south1-docker.pkg.dev/<project_ID>/<repo_name>/bioimg:biotag
