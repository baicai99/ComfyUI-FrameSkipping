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

### Frame Skipping
- 跳过前 n 张图片。
  - 开发原因：避免动画重叠，需要跳过前16张图片。

### Mask Frame Skipping
- 蒙版跳过前 n 张图片。
  - 开发原因：避免动画重叠，需要跳过前16张蒙版。

### White Mask Generator
- 白色蒙版生成器。
  - 开发原因：如果工作流中的蒙版与图片不一一对应，会导致报错，因此开发了这个组件用于生成空白蒙版。

### IntOperationsNode
- 定义了一个执行基本整数算术操作的节点类，支持加法和减法运算。

## 待开发功能
- 帧数选择器：通过输入开始帧和结束帧来获取视频中的中间帧，并可以向前或向后添加帧。

```git
git add .
git commit -m "update"
git push
```