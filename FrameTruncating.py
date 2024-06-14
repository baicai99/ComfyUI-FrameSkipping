# 图片第几张结束节点

import torch
import numpy as np

class FrameTruncating:
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义节点的输入类型。

        返回值是一个字典，其中包括所有必需的输入参数。
        """
        return {
            "required": {
                "images": ("IMAGE",),  # 输入的一系列图片，类型为"IMAGE"
                "keep_frames": ("INT", {"default": 10, "min": 0, "step": 1}),  # 要保留的帧数，类型为整数
            }
        }

    CATEGORY = "baicai/picture"  # 定义该节点在组件库中的分类

    RETURN_TYPES = ("IMAGE",)  # 定义节点的输出类型，这里返回处理后的图片
    RETURN_NAMES = ("truncated_images",)  # 定义输出的变量名

    FUNCTION = "truncate_frames"  # 定义节点的主要函数名

    def truncate_frames(self, images, keep_frames):
        """
        保留指定数量的帧，并舍弃其后的帧。

        参数:
        images (torch.Tensor): 输入的一系列图片，作为 torch 张量
        keep_frames (int): 要保留的帧数

        返回值:
        torch.Tensor: 处理后的图片，仅保留指定数量的帧
        """
        # images 是一个 torch 张量
        total_frames = images.shape[0]  # 获取总帧数
        
        # 保留指定的帧数
        if keep_frames >= total_frames:
            # 如果要保留的帧数大于或等于总帧数，返回原始图像
            truncated_images = images
        else:
            # 否则，保留指定帧数，舍弃其后的帧
            truncated_images = images[:keep_frames, :, :, :]

        return (truncated_images,)  # 返回处理后的图片

# 注册新节点
NODE_CLASS_MAPPINGS = {
    "FrameTruncating": FrameTruncating
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameTruncating": "Frame Truncating Node"  # 节点显示名称
}
