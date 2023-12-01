import os
import random

# 指定图片所在的文件夹路径
folder_path = "../../datasets/holesaw/images"

# 获取文件夹中所有图片的文件名
all_images = os.listdir(folder_path)

# 计算要删除的图片数量
images_to_delete = len(all_images) // 2

# 随机选择要删除的图片
images_to_delete_list = random.sample(all_images, images_to_delete)

# 删除选定的图片
for image in images_to_delete_list:
    image_path = os.path.join(folder_path, image)
    os.remove(image_path)

print(f"{images_to_delete} images randomly deleted.")