import os
import requests
import subprocess

def download_file(url, save_path):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"File downloaded successfully and saved to {save_path}")
    print(f"File size: {os.path.getsize(save_path)} bytes")

def download_and_install():
    file_id = "1lJrznRMynipjh16soQXJPqkueOg_QtW4"
    download_url = f"https://drive.google.com/uc?export=download&id=1lJrznRMynipjh16soQXJPqkueOg_QtW4"
    output_file = "downloads/dlib_bin-19.24.6-cp311-cp311-manylinux_2_17_x86_64-manylinux2014_x86_64.whl"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Download file
    download_file(download_url, output_file)

    # Validate the file extension
    if not output_file.endswith(".whl"):
        raise ValueError(f"Downloaded file is not a .whl file: {output_file}")

    # Install the .whl file
    subprocess.run(["pip", "install", output_file, "--no-deps"], check=True)

if __name__ == "__main__":
    download_and_install()

