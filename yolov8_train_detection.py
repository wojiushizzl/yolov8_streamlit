from ultralytics import YOLO

# # 从头开始创建一个新的YOLO模型
# model = YOLO('yolov8s.yaml')

# 加载预训练的YOLO模型（推荐用于训练）
model = YOLO('./preModels/yolov8n.pt')
# model = YOLO('./weights/detection/marking.pt')

# # 使用“coco128.yaml”数据集训练模型3个周期
results = model.train(data='holesaw.yaml', epochs=50,batch=2)

# 评估模型在验证集上的性能
# results = model.val()

