module "s3_bucket" {
  source      = "../modules/s3_bucket"
  bucket_name = "crusades-rag-data-s3"   # a globally unique S3 bucket name
  environment = "dev"
}