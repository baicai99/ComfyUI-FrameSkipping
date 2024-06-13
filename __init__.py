# __init__.py
from .FrameSkipping import FrameSkipping

NODE_CLASS_MAPPINGS = {
    "FrameSkipping": FrameSkipping
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameSkipping": "Frame Skipping"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']