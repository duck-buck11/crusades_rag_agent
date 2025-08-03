module "gcs_bucket" {
  source      = "../modules/gcs_bucket"
  bucket_name = "crusades-rag-data"
  location    = "us-central1"
  project_id  = "rag-crusade-pipeline"
}