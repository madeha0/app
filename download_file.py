import os
import requests

def download_file(url, save_path):
    """
    Download a file from the given URL and save it to the specified path.
    """
    try:
        # Stream the file to avoid memory issues
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # Create directories if they don't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # Save the file in chunks
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):  # Download in 8KB chunks
                if chunk:
                    file.write(chunk)
        print(f"File downloaded successfully and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        raise

if __name__ == "__main__":
    # URL to the file you want to download (replace this with the actual URL)
    file_url = "https://drive.google.com/uc?export=download&id=1N3hFvwwQ50THJ6MpyDeMASMOScm6V4W-"
    # Path where you want to save the file
    save_path = "downloads/shape_predictor_68_face_landmarks.dat" # Save in the project root directory

    # Download the file
    download_file(file_url, save_path)
