# COCO to YOLO Format Converter and Dataset Organizer

## 介绍
此项目包含两个主要的Python脚本：
1. **COCO to YOLO Converter**：用于将COCO格式的图像标注数据转换为YOLO目标检测模型所需的标签格式。
2. **Dataset Organizer**：用于将图像文件及其对应的标签文件从源文件夹分配到训练集和验证集。

## 数据结构需求
- 对于COCO to YOLO Converter，您的JSON输入文件必须包含：
  - `images`: 图像列表，每个图像信息包含：
    - `id`: 图像的唯一标识符
    - `file_name`: 图像文件名称
    - `width`: 图像的宽度（像素）
    - `height`: 图像的高度（像素）
  - `annotations`: 标注列表，每个标注信息包含：
    - `image_id`: 对应图像的ID
    - `category_id`: 标注的类别ID
    - `bbox`: 标注的边界框，格式为[x, y, width, height]

- 对于Dataset Organizer，源文件夹中应包含图像文件及其对应的标签文件。

## 安装依赖
确保您的环境中已安装Python，并具有以下库：
- `json`: 处理JSON文件
- `os`: 文件和目录操作
- `shutil`: 文件复制功能
- `random`: 数据随机化

## 使用说明
确保您的文件结构符合上述要求，并调整脚本中的路径设置，然后运行相应的脚本：
- 对于COCO to YOLO Converter：
  ```bash
  python coco_to_yolo_converter.py

  •	对于Dataset Organizer：

  ```python
  python dataset_organizer.py
  ```

  注意事项

	•	确保有足够的磁盘空间来复制或移动文件。
	•	检查生成的标签文件和图像文件确保格式正确无误。

联系方式

如有问题，请通过以下方式联系我：

	•	邮箱: your_email@example.com
	•	GitHub: your_github_profile
