# 组织主页配图源文件

`profile/README.md` 里的图都从这里渲染出来：用 chatjevs.com 同一套设计令牌写 HTML，本机无头 Chrome 按 2 倍像素截图，再量化压缩。每张图都有浅色、深色两版，README 用 `<picture>` 按访客的系统主题切换。

| 源文件 | 出图 | CSS 尺寸 | 内容 |
|---|---|---|---|
| `banner.html` | `banner-light.png` / `banner-dark.png` | 880×470 | 横幅：logo、口号、官网首屏手机样机的收尾状态（已填入、发送键不动） |
| `card.html?p=android` | `card-android-*.png` | 176×252 | Android 平台卡 |
| `card.html?p=windows` | `card-windows-*.png` | 176×252 | Windows 平台卡 |
| `card.html?p=ios` | `card-ios-*.png` | 176×252 | iOS 平台卡 |
| `card.html?p=macos` | `card-macos-*.png` | 176×252 | macOS 平台卡 |
| `flow.html` | `core-flow-*.png` | 880×380 | 「一套内核」流程图：四端各自采集 → 共用的判断、起草、排序、填入 |

`tokens.css` 是共用令牌（颜色、字体、气泡尾巴标签），和官网 `style.css` 开头的 `:root` 保持一致。`fonts/` 里是官网同款拉丁字体 Figtree（SIL OFL 1.1，许可见 `fonts/OFL.txt`），中文用系统字体。

## 重新出图

需要 Windows 上装好的 Chrome，和 Python 的 Pillow、imagequant：

```bash
pip install pillow imagequant
python profile/assets/src/render.py              # 全部重出（12 张）
python profile/assets/src/render.py card         # 只出名字里含 card 的
python profile/assets/src/render.py banner flow  # 可以给多个
```

脚本把 PNG 直接写到 `profile/assets/`，并打印每张的尺寸和大小，超过 150KB 会标出来。Chrome 不在默认位置时，用环境变量 `CHROME` 指定 `chrome.exe` 的路径。

想先看效果，直接用浏览器打开 HTML：`card.html?p=ios`、`banner.html?theme=dark` 这样带参数即可。

## 常见改动

- **升版本号**：图里不写版本号，版本由 README 里的 shields 徽章动态显示，发版不用重出图。只有 README 里 Android 直链的文件名（`jev-assistant-v1.5-release.apk`）要跟着改。
- **改平台卡文字**：改 `card.html` 里的 `DATA`（形态、怎么拿到对话、状态）；形态示意图在 `ART`，设备是中性线条，Jev 那一块用蓝色。
- **加一个平台**：在 `card.html` 的 `ICON` / `ART` / `DATA` 各加一项，在 `render.py` 的 `JOBS` 里加一行，再到 `flow.html` 的采集那一排加一格（`.cap-row` 改列数，连线 `<svg class="wires">` 里按新的格子中心重算 x 坐标）。README 里的卡片表、徽章行、链接行、仓库表按 Android → Windows → iOS → macOS 的顺序往后排。
- **改配色**：只改 `tokens.css`，四类图一起变。

## 写图时的规矩

- 演示对话只用官网那一段（「你根本就不懂我」），图里不出现任何真人名字，聊天界面是通用样式，不仿任何具体 App。
- 悬浮窗面板在深色主题下也保持浅色（App 里就是浅色的）。
- 源文件同样要过禁词检查。候选排名的井号由 CSS `::before` 补上，以 1 开头的十六进制颜色改写成 `rgb()`，这样源码里不会出现「井号 + 1」。
