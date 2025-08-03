output "bucket_name" {
  description = "The name of the GCS bucket"
  value       = google_storage_bucket.this.name
}

output "bucket_url" {
  description = "The GCS bucket's public or internal URL"
  value       = "gs://${google_storage_bucket.this.name}"
}