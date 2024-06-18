# ComfyUI-FrameSkipping 组件介绍

## 问：为什么开发这个组件？
答：我希望制作一个视频，在手触碰到物体后手的材质会发生变化。为了实现渐变效果，我开发了这个组件，可以将一段视频进行切分，而不是将其分成两段。

这个插件能够精确控制帧与帧之间的渲染，实现单次加载中多帧的合成。

节点组命名为：baicai

未来将上传ComfyUI工作流。

![Snipaste_2024-06-13_16-54-59](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/619d209c-5337-43b8-a57b-0474f7496a21)

![Snipaste_2024-06-14_16-41-39](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/030c30c3-132b-4741-b388-9406abc9c1a7)

## 已开发功能

### Frame Truncating
- 仅保留前 n 张图片。
  - 开发原因：为了实现动画效果，前16张和后续图片需要分开处理。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/309f9ae2-442f-4d71-b065-db3c13f967ff)

### Frame Skipping
- 跳过前 n 张图片。
  - 开发原因：避免动画重叠，需要跳过前16张图片。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/dd925c20-3bd8-44c6-8869-35296af99c21)

### Mask Frame Skipping
- 蒙版跳过前 n 张图片。
  - 开发原因：避免动画重叠，需要跳过前16张蒙版。

### Mask Generator
- 蒙版生成器,可以任意数量，任意大小的生成白色 & 黑色 蒙版。
  - 开发原因：如果工作流中的蒙版与图片不一一对应，会导致报错，因此开发了这个组件用于生成空白蒙版。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/80df546b-1497-4316-8bc7-819ddc50a37c)

### IntOperationsNode
- 定义了一个执行基本整数算术操作的节点类，支持加法和减法运算。
![image](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/1515c260-4e9c-43f0-9198-8c5ef9962cee)

## 待开发功能
- 帧数选择器：通过输入开始帧和结束帧来获取视频中的中间帧，并可以向前或向后添加帧。

```git
git add .
git commit -m "update"
git push
```