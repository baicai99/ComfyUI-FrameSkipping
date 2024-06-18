# ComfyUI-FrameSkipping 组件介绍

[中文](README.zh.md) | [ENGLISH](README.md)

## 问：为什么开发这个组件？
答：开发此组件的初衷是为了制作一个在手触碰到物体后手的材质发生变化的视频。为了实现这一渐变效果，我开发了这个组件，使其可以对视频进行精细切分，而不仅仅是将视频简单分成两段。

该插件能够精确控制帧与帧之间的渲染，实现单次加载中多帧的合成。

组件节点命名为：baicai

未来将上传ComfyUI工作流。

## 已开发功能
### Frame Selector
- 帧选择器：通过输入开始帧和结束帧来获取中间帧，如果需要延续帧，可以往后添加任意帧数。
  - 开发原因：虽然之前的节点可以使用 IntOperationsNode 来实现相似效果，但操作较为繁琐，因此开发了此节点以简化操作。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/3a36b65a-5573-4abb-9708-5422f48dd74c)

### Mask Selector
- 蒙版帧选择器：通过输入开始帧和结束帧来获取中间帧，如果需要延续帧，可以往后添加任意帧数。
  - 开发原因：蒙版和图片需要同步，不然会报错。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/9f79fbd4-77d2-46ea-9de7-0c1291ed1276)

### Frame Truncating
- 帧截取：仅保留前 n 张图片。
  - 开发原因：为了实现动画效果，前16张和后续图片需要分别处理。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/309f9ae2-442f-4d71-b065-db3c13f967ff)

### Frame Skipping
- 帧跳过：跳过前 n 张图片。
  - 开发原因：为避免动画重叠，需要跳过前16张图片。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/dd925c20-3bd8-44c6-8869-35296af99c21)

### Mask Frame Skipping
- 蒙版帧跳过：跳过前 n 张蒙版图片。
  - 开发原因：为避免动画重叠，需要跳过前16张蒙版图片。

### Mask Generator
- 蒙版生成器：可以生成任意数量和大小的白色与黑色蒙版。
  - 开发原因：为了避免工作流中蒙版与图片不一一对应导致报错，开发了此组件用于生成空白蒙版。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/80df546b-1497-4316-8bc7-819ddc50a37c)

### IntOperationsNode
- 整数运算节点：定义了一个执行基本整数算术操作的节点类，支持加法和减法运算。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/1515c260-4e9c-43f0-9198-8c5ef9962cee)

## 待开发功能
- 蒙版编辑器：1.中间黑，外面白。2.从上到下黑。

```bash
git add .
git commit -m "update"
git push
```