"""
Uploads the local database file to the remote S3 bucket.
"""

import logging

from pipelines.utils.storage_client import ObjectStorageClient

from ._common import DUCKDB_FILE

logger = logging.getLogger(__name__)


def upload_database_to_remote_s3(remote_path="database/data.duckdb"):
    """Upload the local database to the remote S3 bucket."""

    local_db_path = DUCKDB_FILE

    logger.info(f"Uploading database the remote S3 bucket at {remote_path}...")
    client = ObjectStorageClient()
    client.upload_object(local_db_path, remote_path)
    logger.info("Database uploaded successfully.")


def execute():
    upload_database_to_remote_s3()
