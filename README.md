# ComfyUI-FrameSkipping
Q：为什么开发这个组件？  
A：我想做一个视频，我的手触碰到物体之后会改变我手的材质。但是这样子需要渐变效果的话就比较麻烦，于是我开发这个组件可以把一段视频切分，而不是两条视频。

这个插件可以精确地控制帧与帧之间的渲染，在单次加载中完成多帧的合成。  

节点组的名字叫：baicai

在未来会上传ComfyUI工作流。  

![Snipaste_2024-06-13_16-54-59](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/619d209c-5337-43b8-a57b-0474f7496a21)

![Snipaste_2024-06-14_16-41-39](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/030c30c3-132b-4741-b388-9406abc9c1a7)

# 已开发

#### Frame Truncating

- 图片仅保存前16张。
    - 开发原因：因为需要动画效果，前16张和后面剩余需要分开。
#### Frame Skipping
- 图片仅跳过前16张。
    - 开发原因：如果不过跳过前16张的话，就会动画重叠。
#### Mask Frame Skipping
- 蒙版仅跳过前16张。
    - 开发原因：如果不过跳过前16张的话，就会动画重叠。
#### White Mask Generator
- 白色蒙版生成器。
    - 开发原因：因为工作流蒙版和图片不是一一对应的话，就会报错，所以开发这个组件，用于生成空白蒙版。

# 待开发

- 帧数选择器，输入开始帧和结束帧获得视频中间帧，并且可以向前添加帧和向后添加帧。

```git
git add .
git commit -m "update"
git push
```