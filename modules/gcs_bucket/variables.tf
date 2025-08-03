variable "bucket_name" {
  description = "The name of the GCS bucket to create"
  type        = string
  default     = "crusades-rag-data"
}

variable "location" {
  description = "The GCP region where the bucket will be created"
  type        = string
  default     = "us-central1"
}

variable "project_id" {
  description = "The GCP project ID to create the bucket in"
  type        = string
}
