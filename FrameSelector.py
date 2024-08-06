import torch

class FrameSelector:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "start_frame": ("INT", {
                    "default": 0,
                    "min": 0, 
                    "max": 10000, 
                    "step": 1, 
                    "display": "number" 
                }),
                "end_frame": ("INT", {
                    "default": 1,
                    "min": 1, 
                    "max": 10000, 
                    "step": 1, 
                    "display": "number" 
                }),
                "images": ("IMAGE",),  # 输入的一系列图片，类型为"IMAGE"
                "addition_value": ("INT", {
                    "default": 0,
                    "min": 0, 
                    "max": 10000, 
                    "step": 1, 
                    "display": "number" 
                }),
            },
        }

    RETURN_TYPES = ("IMAGE", "INT")
    RETURN_NAMES = ("selected_images", "num_frames")

    FUNCTION = "select_frames"

    CATEGORY = "baicai"

    def select_frames(self, start_frame, end_frame, images, addition_value):
        total_frames = images.shape[0]

        # 将addition_value先加到end_frame
        adjusted_end_frame = end_frame + addition_value

        if start_frame >= total_frames or adjusted_end_frame >= total_frames or start_frame < 0 or adjusted_end_frame < 0:
            selected_images = torch.empty((0, *images.shape[1:]), dtype=images.dtype)
            num_frames = 0
        else:
            selected_images = images[start_frame:adjusted_end_frame, :, :, :]
            num_frames = selected_images.shape[0]

        return (selected_images, num_frames)

    @classmethod
    def IS_CHANGED(cls, start_frame, end_frame, addition_value):
        return f"{start_frame}-{end_frame}-{addition_value}"

NODE_CLASS_MAPPINGS = {
    "FrameSelector": FrameSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameSelector": "Frame Selector"
}
