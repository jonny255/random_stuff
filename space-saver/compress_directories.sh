import os
import shutil
import subprocess
from pathlib import Path
import time
import sys

class CompressionManager:
    def __init__(self, source_dir: str, max_depth: int = 3, output_dir: str = "output", 
                 delete_original: bool = False):
        self.source_dir = source_dir
        self.max_depth = max_depth
        self.output_dir = output_dir
        self.delete_original = delete_original
        self.paused = False
        self.cancel_requested = False

    def process_directory(self, directory):
        """Process a single directory and its contents"""
        if not os.path.exists(directory) or os.path.isfile(directory):
            return

        print(f"Processing directory: {directory}")
        
        # Get list of files in this directory
        files = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                files.append(item_path)

        total_files = len(files)
        print(f"Found {total_files} files to process.")

        # Process each file
        for i, file in enumerate(files):
            current_file = file
            if self.paused:
                input("Operation paused. Press Enter to resume.")
                continue

            start_time = time.time()
            
            # Create output path for compressed file
            output_path = os.path.join(self.output_dir, f"{os.path.basename(current_file)}.7z")
            
            try:
                print(f"Compressing {current_file} ({i+1}/{total_files})")
                subprocess.run(['7z', 'a', output_path, current_file], 
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
                
                end_time = time.time()
                duration = end_time - start_time
                print(f"Completed in {duration:.2f} seconds")
                
            except Exception as e:
                print(f"Error processing file: {str(e)}")

        # Delete original directory if delete_original flag is True
        if self.delete_original and os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"Original directory '{directory}' deleted successfully.")

    def run(self):
        """Main execution method"""
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

        # Find all subdirectories up to max depth and process them
        for root, dirs, files in os.walk(self.source_dir, topdown=False):
            for dir_name in dirs[:self.max_depth]:
                dir_path = os.path.join(root, dir_name)
                self.process_directory(dir_path)

        print("Compression complete!")

def main():
    # Get user input for source directory
    while True:
        source_dir = input("Enter the source directory path: ").strip()
        if os.path.exists(source_dir):
            break
        print("Invalid directory. Please try again.")

    # Create compression manager instance with delete_original flag set to True
    compression_manager = CompressionManager(
        source_dir,
        delete_original=True
    )

    # Run the compression process
    compression_manager.run()

if __name__ == "__main__":
    main()
