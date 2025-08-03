resource "google_storage_bucket" "this" {
  name     = var.bucket_name
  location = var.location
  project  = var.project_id

  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }
}