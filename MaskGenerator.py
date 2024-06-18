import torch

class MaskGenerator:

    def __init__(self):
        """
        初始化 WhiteMaskGenerator 类。目前不需要特定的初始化操作。
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
                "num_masks": ("INT", {  # 要创建的蒙版数量的输入类型
                    "default": 1, 
                    "min": 1, 
                    "step": 1, 
                    "display": "number"
                }),
                "mask_height": ("INT", {  # 蒙版的高度
                    "default": 512,
                    "min": 1,
                    "max": 4096,
                    "step": 1,
                    "display": "number"
                }),
                "mask_width": ("INT", {  # 蒙版的宽度
                    "default": 512,
                    "min": 1,
                    "max": 4096,
                    "step": 1,
                    "display": "number"
                }),
                "mask_color": (["white", "black"],),
            },
        }

    RETURN_TYPES = ("MASK",)  # 输出的类型，将是一个蒙版的张量
    FUNCTION = "execute"  # 执行的主要函数
    CATEGORY = "baicai/mask"  # 此节点在UI中出现的类别

    def execute(self, num_masks, mask_height, mask_width, mask_color):
        """
        执行节点的主要功能：创建指定数量的白色蒙版。

        参数
        ----
        num_masks : int
            要创建的蒙版数量。
        mask_height : int
            每个蒙版的高度。
        mask_width : int
            每个蒙版的宽度。

        返回
        ----
        tuple
            包含生成的蒙版张量的元组。
        """
        # 根据颜色参数创建蒙版
        if mask_color == "black":
            masks = torch.zeros((num_masks, mask_height, mask_width), dtype=torch.float32)
        else:  # 默认为白色蒙版
            masks = torch.ones((num_masks, mask_height, mask_width), dtype=torch.float32)
        
        return (masks,)