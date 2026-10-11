"""
YOLO实时目标检测
使用摄像头进行实时目标检测
"""
from ultralytics import YOLO
import cv2
import time
import os

def real_time_detection(model_path, camera_id=0):
    """
    实时目标检测
    
    Args:
        model_path: 模型权重路径
        camera_id: 摄像头ID，默认0
    """
    # 加载模型
    model = YOLO(model_path)
    print(f"模型加载成功: {model_path}")
    
    # 打开摄像头
    cap = cv2.VideoCapture(camera_id)
    if not cap.isOpened():
        print(f"无法打开摄像头 {camera_id}")
        return
    
    print("开始实时检测，按 'q' 退出")
    
    frame_count = 0
    start_time = time.time()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取帧")
            break
        
        # 目标检测
        results = model(frame, device='cpu', verbose=False)
        
        # 绘制检测结果
        annotated_frame = results[0].plot()
        
        # 计算FPS
        frame_count += 1
        elapsed_time = time.time() - start_time
        if elapsed_time > 0:
            fps = frame_count / elapsed_time
            cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # 显示检测结果数量
        num_detections = len(results[0].boxes)
        cv2.putText(annotated_frame, f"Detections: {num_detections}", (10, 60), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # 显示画面
        cv2.imshow('YOLO Real-time Detection', annotated_frame)
        
        # 按 'q' 退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # 释放资源
    cap.release()
    cv2.destroyAllWindows()
    print("检测结束")

if __name__ == "__main__":
    model_path = os.path.join(os.path.dirname(__file__), "runs", "detect", "train", "weights", "best.pt")
    real_time_detection(model_path)
