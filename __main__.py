from pulumi.provider.experimental import component_provider_host

from s3Bucket import S3Bucket

if __name__ == "__main__":
    component_provider_host(name="s3bucket", components=[S3Bucket])
