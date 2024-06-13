# ComfyUI-FrameSkipping
Q：为什么开发这个组件？
A：我想做一个视频，我的手触碰到物体之后会改变我手的材质。但是这样子需要渐变效果的话就比较麻烦，于是我开发这个组件可以把一段视频切分，而不是两条视频。

This plugin can precisely control the rendering between frames, completing the synthesis of multiple frames in a single load.
My homepage includes my attached workflow.
![Snipaste_2024-06-13_16-54-59](https://github.com/baicai99/ComfyUI-FrameSkipping/assets/101706274/619d209c-5337-43b8-a57b-0474f7496a21)
#### Frame Truncating
- 只保存前16张。
#### Frame Skipping
- 跳过前16张。

```
git add .
git commit -m "update"
git push
```