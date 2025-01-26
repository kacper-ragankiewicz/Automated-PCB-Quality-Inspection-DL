import os
import shutil

# Define paths
base_dir = "pcb_data/PCB_DATASET"
annotations_dir = os.path.join(base_dir, "Annotations")
images_dir = os.path.join(base_dir, "images")
correct_pcbs_dir = os.path.join(base_dir, "PCB_USED")
rotated_images_dir = os.path.join(base_dir, "rotation")
output_dir = "organized_pcb_data"

# Collect all defect types dynamically from the folder structure
# Subdirectories represent defect types
defect_types = set(os.listdir(annotations_dir))

# Create train and test folders with defect subfolders
for split in ["train", "test"]:
    os.makedirs(os.path.join(output_dir, split, "correct"),
                exist_ok=True)  # Folder for correct PCBs
    for defect_type in defect_types:
        os.makedirs(os.path.join(output_dir, split,
                    defect_type), exist_ok=True)

# Organize defect images
for defect_type in defect_types:
    annotation_path = os.path.join(annotations_dir, defect_type)
    image_path = os.path.join(images_dir, defect_type)
    rotation_path = os.path.join(rotated_images_dir, defect_type)

    # Handle original defect images
    if os.path.exists(annotation_path) and os.path.exists(image_path):
        for image_name in os.listdir(image_path):
            src = os.path.join(image_path, image_name)
            if not os.path.exists(src):
                print(f"Warning: Missing image {image_name} in {image_path}. Skipping...")
                continue

            # 80-20 split for train-test
            split = "train" if hash(image_name) % 10 < 8 else "test"
            dest = os.path.join(output_dir, split, defect_type, image_name)
            print(f"Moving {src} to {dest}")
            shutil.move(src, dest)

    # Handle rotated defect images
    if os.path.exists(rotation_path):
        for rotated_image_name in os.listdir(rotation_path):
            src = os.path.join(rotation_path, rotated_image_name)
            if not os.path.exists(src):
                print(f"Warning: Missing rotated image {rotated_image_name} in {rotation_path}. Skipping...")
                continue

            # 80-20 split for train-test
            split = "train" if hash(rotated_image_name) % 10 < 8 else "test"
            dest = os.path.join(output_dir, split,
                                defect_type, rotated_image_name)
            print(f"Moving {src} to {dest}")
            shutil.move(src, dest)

# Organize correct PCBs
if os.path.exists(correct_pcbs_dir):
    for correct_image_name in os.listdir(correct_pcbs_dir):
        src = os.path.join(correct_pcbs_dir, correct_image_name)
        if not os.path.exists(src):
            print(f"Warning: Missing correct PCB image {correct_image_name} in {correct_pcbs_dir}. Skipping...")
            continue

        # 80-20 split for train-test
        split = "train" if hash(correct_image_name) % 10 < 8 else "test"
        dest = os.path.join(output_dir, split, "correct", correct_image_name)
        print(f"Moving {src} to {dest}")
        shutil.move(src, dest)

print("Dataset organization completed.")
