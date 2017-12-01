# Converted from S3_Bucket.template located at:
# http://aws.amazon.com/cloudformation/aws-cloudformation-templates/
# convert default JSON output to YAML

import json
import yaml
from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket, PublicRead

t = Template()

t.add_description(
    "AWS CloudFormation Template S3_Bucket: template showing "
    "how to create a publicly accessible S3 bucket. in YAML")

s3bucket = t.add_resource(Bucket("S3Bucket", AccessControl=PublicRead,))

t.add_output(Output(
    "BucketName",
    Value=Ref(s3bucket),
    Description="Name of S3 bucket to hold website content"
))

# For JSON
#print(t.to_json())

# For YAML
print(yaml.safe_dump(json.loads(t.to_json()), None, allow_unicode=True))