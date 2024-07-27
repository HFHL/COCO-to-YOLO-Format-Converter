# COCO to YOLO Format Converter

## 介绍
此脚本用于将COCO格式的图像标注数据转换为YOLO（You Only Look Once）目标检测模型所需的标签格式。它还可以选择性地复制图像文件到指定目录。

## 数据结构需求
为了确保脚本正常运行，您的JSON输入文件必须包含以下字段：

- `images`: 图像列表，每个图像信息包含：
  - `id`: 图像的唯一标识符
  - `file_name`: 图像文件名称
  - `width`: 图像的宽度（像素）
  - `height`: 图像的高度（像素）

- `annotations`: 标注列表，每个标注信息包含：
  - `image_id`: 对应图像的ID
  - `category_id`: 标注的类别ID
  - `bbox`: 标注的边界框，格式为[x, y, width, height]

## 安装依赖
确保您的环境中已安装Python，并具有以下库：
- `json`: 处理JSON文件
- `os`: 文件和目录操作
- `shutil`: 文件复制功能

这些库在标准Python环境中默认存在，无需额外安装。

## 使用说明
1. 确保您的JSON文件结构符合上述要求。
2. 调整脚本中的路径设置，包括：
   - `data_path`: 指向您的JSON文件的路径。
   - `images_dir`: 您希望存储图像的目录路径。
   - `labels_dir`: 存储生成的标签文件的目录路径。
3. 运行脚本：
   ```bash
   python your_script_name.py
