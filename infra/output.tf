output "gcs_bucket_name" {
  description = "The name of the GCS bucket"
  value       = module.gcs_bucket.bucket_name
}

output "gcs_bucket_url" {
  description = "The gs:// URI of the GCS bucket"
  value       = module.gcs_bucket.bucket_url
}