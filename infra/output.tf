output "gcs_bucket_name" {
  description = "The name of the GCS bucket"
  value       = module.gcs_bucket.bucket_name
}

output "gcs_bucket_url" {
  description = "The GCS bucket's public or internal URL"
  value       = module.gcs_bucket.bucket_url
}

output "s3_bucket_name" {
  description = "The name of the S3 bucket"
  value       = module.s3_bucket.bucket_name
}

output "s3_bucket_arn" {
  description = "The ARN of the S3 bucket"
  value       = module.s3_bucket.bucket_arn
}