import os


def remove_webp_from_filenames(directory):
    """
    Remove '.webp' from filenames in the specified directory.

    :param directory: Path to the directory containing files.
    """
    try:
        # List all files in the directory
        for filename in os.listdir(directory):
            # Check if the file has '.webp' in its name
            if '.webp' in filename:
                # Remove '.webp' from the filename
                new_filename = filename.replace('.webp', '')
                # Get the full paths
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_filename)
                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with the path to your directory
    directory_path = "pcb_data/test/good/"
    remove_webp_from_filenames(directory_path)
