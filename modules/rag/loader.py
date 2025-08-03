import os
import tempfile
import boto3
from typing import List
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_core.documents import Document

def download_s3_objects(bucket: str, prefix: str, local_dir: str) -> List[str]:
    s3 = boto3.client("s3")
    response = s3.list_objects_v2(Bucket=bucket, Prefix=prefix)
    downloaded_files = []

    for obj in response.get("Contents", []):
        key = obj["Key"]
        if key.endswith(".txt") or key.endswith(".pdf"):
            local_path = os.path.join(local_dir, os.path.basename(key))
            s3.download_file(bucket, key, local_path)
            downloaded_files.append(local_path)

    return downloaded_files

def load_documents_from_s3(bucket: str, prefix: str) -> List[Document]:
    with tempfile.TemporaryDirectory() as tmpdir:
        files = download_s3_objects(bucket, prefix, tmpdir)
        docs = []

        for path in files:
            if path.endswith(".txt"):
                docs.extend(TextLoader(path).load())
            elif path.endswith(".pdf"):
                docs.extend(PyPDFLoader(path).load())

        return docs