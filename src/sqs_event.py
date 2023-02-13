import logging
import os
import json


FORMAT = "[%(asctime)s.%(msecs)03d %(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO, force=True, datefmt='%Y-%m-%d %H:%M:%S')


def handler(event, context):
    logging.info("sqs event received %s", event)

    for record in event['Records']:
        recordBody=(json.loads(record["body"]))
    
        bucket_name = recordBody["Records"][0]["s3"]["bucket"]["name"]
        key=recordBody["Records"][0]["s3"]["object"]["key"]

        logging.info("bucket_name %s", bucket_name)
        logging.info("key %s", key)


    