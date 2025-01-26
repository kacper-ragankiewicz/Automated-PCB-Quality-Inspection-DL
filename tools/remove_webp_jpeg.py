import os


def update_file_extensions(directory):
    """
    Update filenames in the specified directory:
    - Remove '.webp' from filenames.
    - Change '.jpeg' to '.jpg'.

    :param directory: Path to the directory containing files.
    """
    try:
        # List all files in the directory
        for filename in os.listdir(directory):
            # Initialize the new filename as the current filename
            new_filename = filename

            # Remove '.webp' from the filename if present
            if '.webp' in new_filename:
                new_filename = new_filename.replace('.webp', '')

            # Change '.jpeg' to '.jpg' if present
            if '.jpeg' in new_filename:
                new_filename = new_filename.replace('.jpeg', '.jpg')

            # If the filename has changed, rename the file
            if new_filename != filename:
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with the path to your directory
    directory_path = "reddit_dataset/train/good/"
    update_file_extensions(directory_path)
