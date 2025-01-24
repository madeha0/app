import os
import subprocess
import gdown

def download_and_install():
    # Replace the file ID with your actual file ID
    file_id = "1lJrznRMynipjh16soQXJPqkueOg_QtW4"
    download_url = f"https://drive.google.com/uc?id=1lJrznRMynipjh16soQXJPqkueOg_QtW4"
    output_file = "downloads/dlib.whl"

    # Ensure the downloads directory exists
    os.makedirs("downloads", exist_ok=True)

    # Download the file
    gdown.download(download_url, output_file, quiet=False)

    # Verify the file
    if not output_file.endswith(".whl") or not os.path.exists(output_file):
        raise ValueError(f"Downloaded file is invalid: {output_file}")

    # Install the .whl file
    subprocess.run(["pip", "install", output_file, "--no-deps"], check=True)

    # Clean up
    os.remove(output_file)

if __name__ == "__main__":
    download_and_install()
