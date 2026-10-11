"""YOLO 模型训练脚本"""
from ultralytics import YOLO

# 加载预训练模型
model = YOLO('yolov8n.pt')

# 开始训练
results = model.train(
    data='datasets/coco8.yaml',  # 数据集配置
    epochs=3,                    # 训练轮数
    imgsz=640,                   # 图像尺寸
    device='cpu'                 # 训练设备 (cpu 或 0 表示 GPU)
)

# 训练完成后，最佳模型保存在 runs/detect/train/weights/best.pt
print("训练完成! 模型保存在 runs/detect/train/weights/best.pt")

