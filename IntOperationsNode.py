class IntOperationsNode:
    """
    A node for performing basic arithmetic operations on integers.

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Specifies the input parameters of the node.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tuple.
    RETURN_NAMES (`tuple`):
        The name of each output in the output tuple.
    FUNCTION (`str`):
        The name of the entry-point method. This node uses the `execute` method.
    OUTPUT_NODE (`bool`):
        Indicates if this node outputs a result. Assumed to be True for demonstration.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    """

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("result",)
    FUNCTION = "execute"
    OUTPUT_NODE = True
    CATEGORY = "baicai/Operations"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "num1": ("INT", {
                    "default": 0, 
                    "step": 1, 
                    "display": "number"
                }),
                "num2": ("INT", {
                    "default": 0, 
                    "step": 1, 
                    "display": "number"
                }),
                "operation": (["add", "subtract"],)
            },
        }

    def execute(self, num1, num2, operation):
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        else:
            raise ValueError("Unsupported operation")
        return (result,)

