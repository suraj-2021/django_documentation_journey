AMAZON Web services setting
AWS_ACCESS_KEY_Id = "your_access_key"
AWS_SECRECT_ACCESS_KEY = 'your_secrect_key'
AWS_STORAGE_BUCKET_NAME = 'your_bucket_name'
AWS_S3_REGION_NAME = 'your_region'
AWS_S3_CUSTOM_DOMAIN= f'{AWS_STORAGE_BUCKET_NAME}.s3.amazon.com'

#Default file Storage Settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storagee'

#Define Custom Storage Backends
STORAGES = {
    "default":{
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",

    "OPTIONS": {
        "bucket_name": AWS_STORAGE_BUCKET_NAME,
        "custom_domain": AWS_S3_CUSTOM_DOMAIN,
    },
    },
    "public_media": {
        "BACKEND": "storages.backends.s3boto3.S3BotoStorage",
        'OPTIONS': {
            "bucket_name": AWS_STORAGE_BUCKET_NAME,
        "location": "media",
        "default_acl":"public_read",
    
        },
        
    },

    "private_media": {
        "BACKEND": 'storage.backends.s3boto3.S3Boto3Storage',
        "OPTIONS":{
            "bucket_name": AWS_STORAGE_BUCKET_NAME
            "location": "media",
            "default_acl": "private",
            
            
        },
    },
},
