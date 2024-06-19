import os
from pathlib import Path
import zipfile
from threading import Thread
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to compress a single file
def compress_file(file_path, zip_handle):
    logging.info(f"Compressing {file_path}...")
    zip_handle.write(file_path, arcname=file_path.name)

# Function to create a backup
def create_backup(source_dir, backup_zip):
    logging.info(f"Creating backup for directory: {source_dir}")
    with zipfile.ZipFile(backup_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        threads = []
        for file_path in Path(source_dir).rglob('*'):
            if file_path.is_file():
                thread = Thread(target=compress_file, args=(file_path, zipf))
                threads.append(thread)
                thread.start()
        
        for thread in threads:
            thread.join()

    logging.info(f"Backup completed: {backup_zip}")

# Main function
def main(source_dir, backup_zip):
    create_backup(source_dir, backup_zip)

if __name__ == "__main__":
    # Directory to backup
    source_directory = 'path/to/source_directory'
    # Backup zip file
    backup_zip_file = 'path/to/backup.zip'
    
    main(source_directory, backup_zip_file)
