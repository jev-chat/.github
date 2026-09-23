
<h1 align="center">Jev 聊天助手</h1>

<p align="center"><b>非侵入式对话副驾：看屏读懂对方、给出候选回复，发不发由你——Android / macOS / Windows 三端同源</b></p>

<p align="center">
  <a href="https://github.com/jev-chat/jev-chat-jarvis"><img src="https://img.shields.io/github/stars/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=Stars" alt="GitHub stars" /></a>
  <a href="https://github.com/jev-chat/jev-chat-jarvis/blob/main/LICENSE"><img src="https://img.shields.io/github/license/jev-chat/jev-chat-jarvis" alt="MIT License" /></a>
  <img src="https://img.shields.io/badge/Android-v1.4-3DDC84?logo=android&logoColor=white" alt="Android v1.4" />
  <img src="https://img.shields.io/badge/Windows-v0.1.6-0078D6?logo=windows&logoColor=white" alt="Windows v0.1.6" />
  <img src="https://img.shields.io/github/v/release/jev-chat/jev-chat-jarvis-mac?style=flat&amp;logo=apple&amp;logoColor=white&amp;label=macOS" alt="macOS 最新版" />
</p>

<p align="center">
  <a href="https://chatjevs.com"><b>官网 chatjevs.com</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/jev-chat/jev-chat-jarvis/raw/main/apk/jev-assistant-v1.4-release.apk"><b>Android 下载</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/jev-chat/jev-chat-windows/releases"><b>Windows 下载</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/jev-chat/jev-chat-jarvis-mac/releases"><b>macOS 下载</b></a>
</p>

---

## 选你的平台

<table>
  <thead>
    <tr>
      <th></th>
      <th>📱 Android</th>
      <th>🪟 Windows</th>
      <th>🍎 macOS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>适用系统</b></td>
      <td>Android 11+</td>
      <td>Windows 10 / 11，微信 Windows 4.x</td>
      <td>macOS，微信 macOS</td>
    </tr>
    <tr>
      <td><b>支持的聊天 App</b></td>
      <td>微信 8.0.78 ✅ · QQ 9.3.50 ✅ · X/Twitter 私信 12.25 ✅（均真机全链路）· 飞书 ✅（正文靠离线 OCR）· 其它 App 手动「截屏识别一次」</td>
      <td>微信 Windows 4.x</td>
      <td>微信 macOS</td>
    </tr>
    <tr>
      <td><b>采集方式</b></td>
      <td>无障碍服务读节点；读不到正文时截屏 + ML Kit 中文离线 OCR</td>
      <td>WGC 截自己的微信窗口 + 本地离线 OCR（RapidOCR）</td>
      <td>看屏 + 本地小模型判断意图 / 风险</td>
    </tr>
    <tr>
      <td><b>最新版本</b></td>
      <td>v1.4（2026-09-23）</td>
      <td>v0.1.6（2026-09-22）</td>
      <td>v0.5.0</td>
    </tr>
    <tr>
      <td><b>下载</b></td>
      <td><a href="https://github.com/jev-chat/jev-chat-jarvis/raw/main/apk/jev-assistant-v1.4-release.apk">jev-assistant-v1.4-release.apk</a>（约 25 MB）</td>
      <td><a href="https://github.com/jev-chat/jev-chat-windows/releases">jev-chat-windows-v0.1.6.zip</a>（约 146 MB，解压双击 exe，未签名需选「仍要运行」）</td>
      <td><a href="https://github.com/jev-chat/jev-chat-jarvis-mac/releases/latest/download/jev-jarvis-macos-latest.zip">jev-jarvis-macos-v0.5.0.zip</a>（未公证，首次需右键打开）</td>
    </tr>
    <tr>
      <td><b>仓库</b></td>
      <td><a href="https://github.com/jev-chat/jev-chat-jarvis">jev-chat/jev-chat-jarvis</a></td>
      <td><a href="https://github.com/jev-chat/jev-chat-windows">jev-chat/jev-chat-windows</a></td>
      <td><a href="https://github.com/jev-chat/jev-chat-jarvis-mac">jev-chat/jev-chat-jarvis-mac</a></td>
    </tr>
  </tbody>
</table>

<p align="center">
  <img src="https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/docs/images/overlay.png" width="240" alt="Jev 悬浮窗：聊天上方的分析面板" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/docs/images/settings.png" width="240" alt="设置页" />
</p>
<p align="center"><sub>Android 端：左为悬浮窗——危险等级、对方真实意图、排好序的候选回复；右为设置页。</sub></p>

## 它解决什么问题

聊天里最费神的不是打字，是判断：对方到底想要什么？这句话有没有风险？现在该不该回？回什么最合适？

Jev 把这一步交给一个专门做判断的模型。不管你是在手机上用 App，还是在电脑前开着微信，它都贴在聊天旁边，读懂对方刚发的消息，告诉你意图和危险等级，再给出排好序的候选回复。你只需要点一下填进输入框，看一眼，自己按发送。

## 一套内核，三种采集

三端共用同一套流程——判断 → 起草 → 排序 → 填入，区别只在"怎么拿到屏幕上的对话内容"：

| 环节 | 说明 | Android | Windows | macOS |
|---|---|---|---|---|
| **采集** | 拿到当前对话内容 | 无障碍服务读节点；读不到正文时截屏 + ML Kit 中文离线 OCR | WGC 截自己的微信窗口 + 本地离线 OCR（RapidOCR） | 看屏截图，交给本地小模型 |
| **判断** | 真实意图、危险等级、该怎么办 | Jev 判断模型（判断/回复/视觉三路接口可配） | Jev 判断模型 | 本地小模型：8 类意图零样本 86.4%，风险 0–9 分级 + 行动建议；也可配 TypeSafe Jev / 兼容网关走云端 |
| **起草** | 生成候选回复 | 生成模型起草，按合适度排序 | 生成候选并给出胜出概率 | 按内置话术库（10 种）生成，本地模型排序 |
| **填入** | 一键落到输入框 | 无障碍 `ACTION_SET_TEXT`，失败则剪贴板 | 一键填入微信输入框 | 走系统辅助功能接口 |

新增一个采集渠道，只需要换掉"采集"这一层，判断、起草、排序、填入全部复用。

## 隐私与边界

三端口径一致：

- **只读你自己设备上、你自己有权查看的聊天。**
- **发送永远由你点。** 三端都只把候选回复填进输入框，不自动发送，不碰转账、红包、收款。
- **密钥只存本机**，不进仓库、不进日志。
- **Android 端**聊天历史默认不落盘；打开后也只存本机，不上传。
- **Windows / macOS 端** OCR 全程离线（RapidOCR / 本地模型），不上传截图。

完整的 Android 端隐私政策见 [PRIVACY.md](https://github.com/jev-chat/jev-chat-jarvis/blob/main/PRIVACY.md) 与官网 [chatjevs.com/privacy.html](https://chatjevs.com/privacy.html)。

## 组织内仓库

| 仓库 | 说明 |
|---|---|
| [jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | Android 主项目，1225 stars，MIT。最新 v1.4 |
| [jev-chat-windows](https://github.com/jev-chat/jev-chat-windows) | Windows 端：微信 Windows 旁挂，WGC 截图 + 离线 OCR。最新 v0.1.6 |
| [jev-chat-jarvis-mac](https://github.com/jev-chat/jev-chat-jarvis-mac) | macOS 端：微信 macOS，本地/云端判断意图与风险。最新 v0.5.0 |
| [jev-chat.github.io](https://github.com/jev-chat/jev-chat.github.io) | 官网源码，对应 chatjevs.com（GitHub Pages） |

## 路线图

- 覆盖更多即时通讯 App。
- 桌面端与网页端进一步整合，减少专属适配成本。
- 三端体验对齐：知识库、联系人档案、话术风格逐步互通。

## 联系

合作、反馈、进群，请**公众号私信**。交流群二维码在 [Android 仓库 README 底部](https://github.com/jev-chat/jev-chat-jarvis#readme)（7 天有效，过期了公众号私信要新码）。

<p align="center"><img src="https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/docs/images/wechat-mp.png" width="160" alt="公众号二维码" /></p>

<p align="center"><sub>© 2026 Finderchangchang 与 jev-chat 贡献者 · <a href="https://github.com/jev-chat/jev-chat-jarvis/blob/main/LICENSE">MIT</a> 开源 · 可商用，须注明出处（见 <a href="https://github.com/jev-chat/jev-chat-jarvis/blob/main/NOTICE">NOTICE</a>）。只处理你自己有权查看的聊天，请遵守各软件的许可协议与当地法律法规。</sub></p>
