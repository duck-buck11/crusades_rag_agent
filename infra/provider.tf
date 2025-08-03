provider "aws" {
  region  = "us-east-1"
  profile = "default"
}

provider "google" {
  project = "rag-crusade-pipeline"
  region  = "us-central1"
}