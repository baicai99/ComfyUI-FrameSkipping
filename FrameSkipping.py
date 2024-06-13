class FrameSkipping:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "frame": ("INT", {
                    "default": 1,
                    "min": 1,
                    "step": 1,
                    "display": "number"
                }),
                "skip_frame": ("INT", {
                    "default": 1,
                    "min": 1,
                    "step": 1,
                    "display": "number"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "execute"
    CATEGORY = "FrameSkipping"

    def execute(self, frame, skip_frame):

        def generate_sequence(frame, skip_frame):
            sequence = []
            for i in range(skip_frame + 1, frame + 1):
                sequence.append(i)
            return sequence

        result = generate_sequence(frame, skip_frame)
        result_str = ", ".join(map(str, result))

        print(f"生成的序列: {result_str}")

        return (result_str,)

NODE_CLASS_MAPPINGS = {
    "FrameSkipping": FrameSkipping
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameSkipping": "Frame Skipping Node"
}
