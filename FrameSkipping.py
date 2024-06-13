import torch
import numpy as np

class FrameSkipping:
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义节点的输入类型。

        返回值是一个字典，其中包括所有必需的输入参数。
        """
        return {
            "required": {
                "images": ("IMAGE",),  # 输入的一系列图片，类型为"IMAGE"
                "skip_initial_frames": ("INT", {"default": 10, "min": 0, "step": 1}),  # 要跳过的初始帧数，类型为整数
            }
        }

    CATEGORY = "baicai"  # 定义该节点在组件库中的分类

    RETURN_TYPES = ("IMAGE",)  # 定义节点的输出类型，这里返回处理后的图片
    RETURN_NAMES = ("skipped_images",)  # 定义输出的变量名

    FUNCTION = "skip_initial_frames"  # 定义节点的主要函数名

    def skip_initial_frames(self, images, skip_initial_frames):
        """
        跳过指定数量的初始帧，并返回剩余的帧。

        参数:
        images (torch.Tensor): 输入的一系列图片，作为 torch 张量
        skip_initial_frames (int): 要跳过的初始帧数

        返回值:
        torch.Tensor: 处理后的图片，跳过指定数量的初始帧
        """
        # images 是一个 torch 张量
        total_frames = images.shape[0]  # 获取总帧数
        
        # 跳过指定的初始帧
        if skip_initial_frames >= total_frames:
            # 如果要跳过的帧数大于或等于总帧数，返回空张量
            skipped_images = torch.empty((0, *images.shape[1:]), dtype=images.dtype)
        else:
            # 否则，跳过初始帧数，返回剩余的帧
            skipped_images = images[skip_initial_frames:, :, :, :]

        return (skipped_images,)  # 返回处理后的图片

# 注册新节点
NODE_CLASS_MAPPINGS = {
    "FrameSkipping": FrameSkipping
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameSkipping": "Frame Skipping Node"  # 节点显示名称
}
