import imageio
import os

def convert_avi_to_images(input_avi, output_folder):
    # 读取AVI文件
    reader = imageio.get_reader(input_avi)

    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历每一帧并保存为图片
    for i, frame in enumerate(reader):
        imageio.imwrite(os.path.join(output_folder, f"frame_{i}.png"), frame)

    print(f"Conversion completed. {i+1} frames saved in {output_folder}")

# 替换为您的AVI文件路径和输出文件夹路径
avi_file = '../../datasets/holesaw.mp4'
output_folder = '../../datasets/holesaw/images'

convert_avi_to_images(avi_file, output_folder)
