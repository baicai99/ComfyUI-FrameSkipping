# 用于跳过指定数量的蒙版并处理剩余的蒙版

import torch

class MaskFrameSkipping:

    def __init__(self):
        """
        初始化 MaskFrameSkipping 类。目前不需要特定的初始化操作。
        """
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        """
        定义节点的输入类型。

        返回
        ----
        dict
            一个指定所需输入类型的字典。
        """
        return {
            "required": {
                "masks": ("MASK",),  # 蒙版的输入类型，预计是一个包含多个蒙版的张量
                "skip_count": ("INT", {  # 要跳过的蒙版数量的输入类型
                    "default": 0, 
                    "min": 0, 
                    "max": 100, 
                    "step": 1, 
                    "display": "number"
                }),
            },
        }

    RETURN_TYPES = ("MASK",)  # 输出的类型，将是一个蒙版的张量
    FUNCTION = "execute"  # 执行的主要函数
    CATEGORY = "baicai/mask"  # 此节点在UI中出现的类别

    def execute(self, masks, skip_count):
        """
        执行节点的主要功能：跳过指定数量的蒙版并处理剩余的蒙版。

        参数
        ----
        masks : torch.Tensor
            包含多个蒙版的张量。
        skip_count : int
            在处理剩余蒙版之前要跳过的蒙版数量。

        返回
        ----
        tuple
            包含处理后蒙版张量的元组。
        """
        if skip_count >= masks.shape[0]:
            # 如果 skip_count 大于或等于蒙版的数量，则返回一个与单个蒙版形状相同的空张量
            return (torch.empty(0, *masks.shape[1:]),)
        
        # 跳过前 `skip_count` 个蒙版
        remaining_masks = masks[skip_count:]
        
        # 处理剩余的蒙版（在此例中，反转每个蒙版）
        processed_masks = [1.0 - mask for mask in remaining_masks]
        
        # 将处理后的蒙版重新堆叠成一个张量
        return (torch.stack(processed_masks),)