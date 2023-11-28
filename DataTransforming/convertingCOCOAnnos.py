import json
import os

# Load the COCO annotations file
coco_annotations_file = 'H:/DeepFashion2Dataset/merged_annotations2.json'   # Replace with the actual path to your file
with open(coco_annotations_file, 'r') as f:
    coco_data = json.load(f)

# Specify the directory where you want to save the separated files
output_directory = "H:/DeepFashion2Dataset/Annos"  # Replace with the desired output directory
os.makedirs(output_directory, exist_ok=True)

# Iterate through each image in the COCO data
for image_data in coco_data['images']:
    image_id = image_data['id']

    # Create a new dictionary for each image
    new_coco_data = {
        'info': coco_data['info'],
        'licenses': coco_data['licenses'],
        'images': [image_data],
        'annotations': [annotation for annotation in coco_data['annotations'] if annotation['image_id'] == image_id],
        'categories': coco_data['categories']
    }
    print(image_id)

    # Save the new COCO data to a separate file
    output_file_path = os.path.join(output_directory, f'image_{image_id}_annotations.json')
    with open(output_file_path, 'w') as f:
        json.dump(new_coco_data, f, indent=2)

print("Separation complete. Each image's annotations are saved in a separate file.")

