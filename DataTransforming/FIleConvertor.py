import json
from pycocotools.coco import COCO
import os

def load_coco_annotations(annotations_path):
    with open(annotations_path, 'r') as file:
        coco_annotations = json.load(file)
    return coco_annotations

def merge_annotations_with_images(coco_annotations, image_folder):
    merged_data = {'info': coco_annotations['info'], 'licenses': coco_annotations['licenses'],
                   'images': [], 'annotations': coco_annotations['annotations'],
                   'categories': coco_annotations['categories']}

    for image_info in coco_annotations['images']:
        image_filename = image_info['file_name']
        image_path = os.path.join(image_folder, image_filename)

        if os.path.exists(image_path):
            image_info['local_path'] = image_path
            merged_data['images'].append(image_info)
            print("done")
        else:
            print(f"Image not found: {image_filename}")

    return merged_data

# Example usage
coco_annotations_path = 'H:/DeepFashion2-master/evaluation/deepfashion_val.json'
image_folder_path = 'H:/DeepFashion2Dataset/validation/image'

coco_annotations = load_coco_annotations(coco_annotations_path)
merged_data = merge_annotations_with_images(coco_annotations, image_folder_path)

# Now 'merged_data' contains annotations with associated image paths
# You can save this merged data in the desired format (e.g., another JSON file).
output_file_path = 'H:/DeepFashion2Dataset/merged_annotations_val.json'

with open(output_file_path, 'w') as output_file:
    json.dump(merged_data, output_file, indent=2)

print(f"Merged data saved to {output_file_path}")
