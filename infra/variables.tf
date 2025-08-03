variable "bucket_name" {
  description = "The name of the GCS bucket to create"
  type        = string
  default     = "crusades-rag-data"  # <- your actual bucket name
}

variable "location" {
  description = "The GCP region where the bucket will be created"
  type        = string
  default     = "us-central1"
}

variable "project_id" {
  description = "The ID of the GCP project to associate with this bucket"
  type        = string
}