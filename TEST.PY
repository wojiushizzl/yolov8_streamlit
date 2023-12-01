from ultralytics import YOLO
import cv2
# 加载模型
model = YOLO('weights/detection/marking_work.pt')  # 加载官方模型

# 使用模型进行预测
# results = model('../../datasets/MissingPartsCLS/train/NonMissingParts/IMG_20231127_085731.jpg')  # 对图像进行预测
results = model.track('../../datasets/打码视频3.mp4',conf=0.75,save=True)  # 对图像进行预测

# # print(results)
#
#
# # 导出模型
# # model.export(format='onnx')
#


#
# import torch
# print(torch.version.cuda)   # CUDA版本
# print(torch.cuda.is_available())   # torch能否成功调用CUDA