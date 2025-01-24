import os
import requests
import subprocess

def download_file(url, save_path):
    """
    Downloads a file from the specified URL and saves it to the given path.
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Raise an error if the request fails
    with open(save_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    print(f"File downloaded successfully and saved to {save_path}")
    print(f"File size: {os.path.getsize(save_path)} bytes")

def download_and_install():
    file_id = "1lJrznRMynipjh16soQXJPqkueOg_QtW4"
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    output_file = "downloads/dlib_bin-19.24.6-cp311-cp311-manylinux_2_17_x86_64-manylinux2014_x86_64.whl"
    renamed_file = "downloads/dlib-19.24.6-cp311-cp311-manylinux2014_x86_64.whl"

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Download file
    download_file(download_url, output_file)

    # Validate the file extension
    if not output_file.endswith(".whl"):
        raise ValueError(f"Downloaded file is not a .whl file: {output_file}")

    # Rename the file
    os.rename(output_file, renamed_file)
    print(f"File renamed to: {renamed_file}")

    # Install the renamed file
    subprocess.run(["pip", "install", "--force-reinstall", "--ignore-installed", renamed_file, "--no-deps"], check=True)
    print("Installation complete!")

if __name__ == "__main__":
    try:
        download_and_install()
    except Exception as e:
        print(f"An error occurred: {e}")
