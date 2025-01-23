import os
import subprocess

def download_and_install():
    # Replace the file ID with your actual file ID
    file_id = "1lJrznRMynipjh16soQXJPqkueOg_QtW4"
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    output_file = "dlib.whl"

    # Download the file
    subprocess.run(["curl", "-L", download_url, "-o", output_file], check=True)

    # Install the .whl file
    subprocess.run(["pip", "install", output_file, "--no-deps"], check=True)

    # Clean up
    os.remove(output_file)

if __name__ == "__main__":
    download_and_install()
