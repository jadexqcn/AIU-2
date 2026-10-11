# YOLO 目标检测项目

基于 YOLOv8 的实时目标检测系统，包含训练、推理和 Web 应用。

## 快速开始

### 1. 环境配置

```bash
conda create -n yolo python=3.11 -y
conda activate yolo
pip install -r requirements.txt
```

### 2. 训练模型

```bash
python train.py
```

训练参数：COCO8 数据集，3 epochs，640x640，CPU
模型保存：`runs/detect/train/weights/best.pt`

### 3. 实时检测

```bash
python yolo_realtime.py
```

按 `q` 退出。

### 4. Web 应用

```bash
python yolo_web.py
```

访问 http://127.0.0.1:5000 上传图片检测。

## 项目结构

```
.
├── train.py              # 训练脚本
├── yolo_realtime.py      # 摄像头实时检测
├── yolo_web.py           # Web 应用
├── templates/index.html  # Web 前端
├── yolov8n.pt            # 预训练模型
├── datasets/coco8/       # 训练数据集
└── runs/detect/train/    # 训练结果
```