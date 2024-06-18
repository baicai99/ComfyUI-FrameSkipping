# ComfyUI-FrameSkipping Component Introduction

[中文](README.zh.md) | [ENGLISH](README.md)

## Question: Why was this component developed?
Answer: The primary motivation for developing this component was to create a video where the texture of a hand changes upon touching an object. To achieve this gradient effect, I developed this component to allow for precise splitting of a video, rather than simply dividing it into two segments.

This plugin enables precise control over frame-to-frame rendering, allowing for the composition of multiple frames in a single load.

The node group is named: baicai

The ComfyUI workflow will be uploaded in the future.

## Developed Features
### Frame Selector
- Frame Selector: By inputting the start frame and end frame, it selects the frames in between. If extension frames are needed, any number of frames can be added.
  - Development Reason: Although similar results could be achieved with the previous node using IntOperationsNode, it was cumbersome. Therefore, a single node was developed to simplify the process.
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/3a36b65a-5573-4abb-9708-5422f48dd74c)

### Mask Selector
- **Mask Frame Selector**: Obtain intermediate frames by inputting the start and end frames. Additional frames can be added if continuation is needed.
  - **Reason for Development**: The mask and image need to be synchronized to avoid errors.
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/9f79fbd4-77d2-46ea-9de7-0c1291ed1276)

### Frame Truncating
- Frame Truncating: Retains only the first n frames.
  - Development Reason: To achieve the desired animation effect, the first 16 frames need to be processed separately from the subsequent frames.
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/309f9ae2-442f-4d71-b065-db3c13f967ff)

### Frame Skipping
- Frame Skipping: Skips the first n frames.
  - Development Reason: To avoid animation overlap, the first 16 frames need to be skipped.
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/dd925c20-3bd8-44c6-8869-35296af99c21)

### Mask Frame Skipping
- Mask Frame Skipping: Skips the first n mask frames.
  - Development Reason: To avoid animation overlap, the first 16 mask frames need to be skipped.

### Mask Generator
- Mask Generator: Generates masks of any quantity and size, in white and black.
  - Development Reason: To prevent errors caused by masks not corresponding one-to-one with images in the workflow, this component was developed to generate blank masks.
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/80df546b-1497-4316-8bc7-819ddc50a37c)

### IntOperationsNode
- IntOperationsNode: Defines a node class that performs basic integer arithmetic operations, supporting addition and subtraction.
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/1515c260-4e9c-43f0-9198-8c5ef9962cee)

## Features to be Developed
- Mask Editor: 1. Black in the middle, white outside. 2. Black from top to bottom.

```bash
git add .
git commit -m "update"
git push
```