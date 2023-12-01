from ultralytics import YOLO



# 加载预训练的YOLO模型（推荐用于训练）
model = YOLO('./preModels/yolov8n-cls.pt')

# 使用“coco128.yaml”数据集训练模型3个周期
# results = model.train(data='marking.yaml', epochs=50,batch=2)
results = model.train(data='../datasets/MissingPartsCLS', epochs=30,imgsz=640)


#
# # 将模型导出为ONNX格式
# success = model.export(format='onnx')