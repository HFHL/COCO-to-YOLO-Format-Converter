import json
import os
import shutil


def load_data(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except IOError:
        print(f"Error: Unable to read file {filepath}")
        return None


def organize_annotations(annotations):
    organized = {}
    for annotation in annotations:
        image_id = annotation['image_id']
        if image_id not in organized:
            organized[image_id] = []
        organized[image_id].append(annotation)
    return organized


def convert_to_yolo_format(data, images_dir, labels_dir, copy_images=False):
    annotations_by_id = organize_annotations(data['annotations'])

    for image in data['images']:
        image_id = image['id']
        file_name = image['file_name']
        width = image['width']
        height = image['height']

        label_file = file_name.split('.')[0] + '.txt'
        label_path = os.path.join(labels_dir, label_file)

        try:
            with open(label_path, 'w') as f:
                for annotation in annotations_by_id.get(image_id, []):
                    category_id = annotation['category_id']
                    x, y, w, h = annotation['bbox']

                    x_center = (x + w / 2) / width
                    y_center = (y + h / 2) / height
                    w /= width
                    h /= height

                    f.write(f"{category_id} {x_center} {y_center} {w} {h}\n")
        except IOError:
            print(f"Error: Unable to write to file {label_path}")

        if copy_images:
            shutil.copy(os.path.join(images_dir, file_name), os.path.join(images_dir, file_name))


def main():
    data_path = 'new_coco.json'
    images_dir = './your/dataset/images'  # 调整为实际的图片目录
    labels_dir = './your/dataset/labels'
    copy_images = False  # 根据需要设置为True或False

    os.makedirs(images_dir, exist_ok=True)
    os.makedirs(labels_dir, exist_ok=True)

    data = load_data(data_path)
    if data:
        convert_to_yolo_format(data, images_dir, labels_dir, copy_images)
        print("标签转换完成，并存储在指定目录下。")


if __name__ == "__main__":
    main()
