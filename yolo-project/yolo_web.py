"""
YOLO Web 应用
使用 Flask 提供 Web 界面进行目标检测
"""
from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import base64
from datetime import datetime
import os

app = Flask(__name__)

# 加载模型（使用相对路径）
model_path = os.path.join(os.path.dirname(__file__), "runs", "detect", "train", "weights", "best.pt")
model = YOLO(model_path)
print(f"模型加载成功: {model_path}")

@app.route('/')
def index():
    """主页"""
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    """处理图片检测请求"""
    try:
        # 获取上传的图片
        if 'image' not in request.files:
            return jsonify({'error': '没有上传图片'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': '没有选择文件'}), 400
        
        # 读取图片
        img_bytes = file.read()
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return jsonify({'error': '无法读取图片'}), 400
        
        # 目标检测
        start_time = datetime.now()
        results = model(img, device='cpu', verbose=False)
        inference_time = (datetime.now() - start_time).total_seconds() * 1000
        
        # 获取检测结果
        detections = []
        for box in results[0].boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            detections.append({
                'class': model.names[cls],
                'confidence': round(conf, 3),
                'bbox': [x1, y1, x2, y2]
            })
        
        # 绘制检测框
        annotated_frame = results[0].plot()
        
        # 转换为 base64
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return jsonify({
            'success': True,
            'image': img_base64,
            'detections': detections,
            'inference_time': round(inference_time, 2),
            'num_detections': len(detections)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
