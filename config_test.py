from app.config import settings

print("Settings loaded for testing:")
print(f"AWS Region: {settings().aws_region}")
print(f"AWS Access Key ID: {settings().aws_access_key_id}")
print(f"AWS Secret Access Key: {settings().aws_secret_access_key}")
print(f"S3 Bucket: {settings().s3_bucket}")
