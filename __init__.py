# __init__.py
from .FrameSkipping import FrameSkipping
from .FrameTruncating import FrameTruncating

NODE_CLASS_MAPPINGS = {
    "FrameSkipping": FrameSkipping,
    "FrameTruncating": FrameTruncating  # 添加新的组件到节点类映射
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameSkipping": "Frame Skipping",
    "FrameTruncating": "Frame Truncating"  # 添加新的组件到节点显示名称映射
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
