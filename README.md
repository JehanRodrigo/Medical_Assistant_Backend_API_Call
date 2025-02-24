Adding Python Backend to the Google Cloud Platform:

* Create Google Cloud Platform Account
* Check Cloud Build Status 
* [Follow the documentation for Gcloud CLI Configuration](https://cloud.google.com/sdk/docs/install)
* Open cloud CLI
  ```
  gcloud init
  ```
* gcloud config set project <your_project_name>
* gcloud auth login
* gcloud artifacts repositories create <repo_rame_you_like> --repository-format=docker --location=asia-south1 --description="<add_description>" --immutable-tags --async
* gcloud auth configure-docker asia-south1-docker.pkg.dev
* gcloud builds submit --tag asia-south1-docker.pkg.dev/<project_ID>/<repo_name>/<Imagename>img:<Tagname>tag
* Cloud Run
