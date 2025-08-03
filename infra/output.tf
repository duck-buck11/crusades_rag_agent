output "gcs_bucket_name" {
  description = "The name of the GCS bucket"
  value       = module.gcs_bucket.bucket_name
}

output "gcs_bucket_url" {
  description = "The GCS bucket's public or internal URL"
  value       = module.gcs_bucket.bucket_url
}

output "s3_bucket_name" {
  description = "S3 bucket name from s3_bucket module"
  value       = module.s3_bucket.bucket_name
}

output "s3_bucket_arn" {
  description = "S3 bucket ARN from s3_bucket module"
  value       = module.s3_bucket.bucket_arn
}