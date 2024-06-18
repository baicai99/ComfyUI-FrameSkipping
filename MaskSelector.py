import torch

class MaskSelector:

    def __init__(self):
        """
        初始化 MaskSelector 类。目前不需要特定的初始化操作。
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
                "start_frame": ("INT", {  # 开始帧的输入类型
                    "default": 0, 
                    "min": 0, 
                    "max": 10000, 
                    "step": 1, 
                    "display": "number"
                }),
                "end_frame": ("INT", {  # 结束帧的输入类型
                    "default": 1, 
                    "min": 1, 
                    "max": 10000, 
                    "step": 1, 
                    "display": "number"
                }),
                "addition_value": ("INT", {  # 附加值的输入类型
                    "default": 0, 
                    "min": 0, 
                    "max": 10000, 
                    "step": 1, 
                    "display": "number"
                }),
            },
        }

    RETURN_TYPES = ("MASK",)  # 输出的类型，将是一个蒙版的张量
    FUNCTION = "select_masks"  # 执行的主要函数
    CATEGORY = "baicai"  # 此节点在UI中出现的类别

    def select_masks(self, masks, start_frame, end_frame, addition_value):
        """
        执行节点的主要功能：选择中间帧的蒙版。

        参数
        ----
        masks : torch.Tensor
            包含多个蒙版的张量。
        start_frame : int
            开始帧的索引。
        end_frame : int
            结束帧的索引。
        addition_value : int
            附加值，会加到结束帧索引上。

        返回
        ----
        tuple
            包含选择后蒙版张量的元组。
        """
        total_frames = masks.shape[0]

        # 将 addition_value 加到 end_frame 上
        adjusted_end_frame = end_frame + addition_value

        if start_frame >= total_frames or adjusted_end_frame >= total_frames or start_frame < 0 or adjusted_end_frame < 0:
            # 如果开始帧或调整后的结束帧超出范围，返回一个空张量
            selected_masks = torch.empty((0, *masks.shape[1:]), dtype=masks.dtype)
        else:
            # 选择中间帧的蒙版
            selected_masks = masks[start_frame:adjusted_end_frame]

        return (selected_masks,)

    @classmethod
    def IS_CHANGED(cls, start_frame, end_frame, addition_value):
        return f"{start_frame}-{end_frame}-{addition_value}"