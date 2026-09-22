
<h1 align="center">Jev 聊天助手</h1>

<p align="center"><b>装在手机上的对话副驾：读懂对方、给出候选回复、一键填入输入框，发不发由你。</b></p>

<p align="center">
  <a href="https://github.com/jev-chat/jev-chat-jarvis/stargazers"><img src="https://img.shields.io/github/stars/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=Stars" alt="GitHub stars" /></a>
  <img src="https://img.shields.io/badge/Android-11%2B-3DDC84?logo=android&logoColor=white" alt="Android 11+" />
  <img src="https://img.shields.io/badge/%E7%89%88%E6%9C%AC-v1.2-1f6feb" alt="v1.2" />
  <a href="https://github.com/jev-chat/jev-chat-jarvis/blob/main/LICENSE"><img src="https://img.shields.io/github/license/jev-chat/jev-chat-jarvis" alt="MIT License" /></a>
</p>

<p align="center">
  <a href="https://github.com/jev-chat/jev-chat-jarvis/raw/main/apk/jev-assistant-v1.2-release.apk"><b>⬇ 下载 APK</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/jev-chat/jev-chat-jarvis"><b>源码与文档</b></a>
  &nbsp;·&nbsp;
  <a href="https://chatjevs.com"><b>官网 chatjevs.com</b></a>
</p>

---

## 它解决什么问题

聊天里最费神的不是打字，是判断：对方到底想要什么？这句话有没有风险？现在该不该回？回什么最合适？

Jev 把这一步交给一个专门做判断的模型。你在微信、QQ、X 里正常聊天，它浮在聊天上方，读懂对方刚发的消息，告诉你意图和危险等级，再给出排好序的 3 条回复。你只需要点一下填进输入框，看一眼，自己按发送。

## 它怎么工作

| 步骤 | 做什么 | 怎么做 |
|---|---|---|
| **1. 采集** | 拿到屏幕上正在显示的对话：谁说的、说了什么 | Android 无障碍服务读节点。不 hook、不改包、不走任何 App 的接口或账号、不读数据库 |
| **2. 判断** | 对方真实意图、危险等级（1–9）、对方要什么、该不该马上回、最佳动作 | [TypeSafe Jev](https://typesafe.ai/) 判断模型，一次请求回答 7 道题，约 1 秒，带把握度 |
| **3. 起草** | 3 条口语化候选回复 | 生成模型（默认 DeepSeek）起草，Jev 按「最合适」排序并给出占比 |
| **4. 填入** | 半透明悬浮窗展示，点一下填进输入框 | `ACTION_SET_TEXT`，失败则剪贴板粘贴。**程序从不自动发送** |

一套内核，多平台。新增一个聊天 App 只需要实现一个几十行的适配器，判断、候选、悬浮窗、填入全部复用。

## 支持的聊天 App

| 平台 | 状态 | 采集方式 |
|---|---|---|
| 微信 8.0.78 | ✅ 真机全链路 | 无障碍读气泡（伪装系统服务绕过节点混淆） |
| QQ 9.3.50 | ✅ 真机全链路 | 无障碍读节点，按头像位置判谁说的 |
| X / Twitter 私信 12.25 | ✅ 真机全链路 | 解析 Compose 节点的 content-desc |
| 飞书 / Lark | 🟡 部分 | 标题、气泡位置、输入框可读；正文是自绘控件，待截屏 + OCR |
| 桌面端 / 网页 | ⏳ 规划 | 同一内核，换采集方式 |

<p align="center">
  <img src="https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/docs/images/overlay.png" width="240" alt="Jev 悬浮窗：聊天上方的分析面板" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/docs/images/settings.png" width="240" alt="设置页" />
</p><p align="center"><sub>左：悬浮窗——危险等级、对方真实意图、排好序的 3 条候选回复。右：设置页。</sub></p>

## 隐私与边界

- **只读你自己设备上、你自己有权查看的聊天**，不针对任何单一平台。
- **发送永远由你点。** 程序只把回复填进输入框，不自动发送，不碰转账、红包、收款。
- **密钥在本机。** API Key 只存 App 私有空间，不进仓库、不进日志。
- **聊天内容不落盘。** 只在分析那一刻发给你自己配置的模型接口，不存历史、不上传截图。

## 快速开始

1. **装包**：下载 [`jev-assistant-v1.2-release.apk`](https://github.com/jev-chat/jev-chat-jarvis/raw/main/apk/jev-assistant-v1.2-release.apk)（Android 11+），或 `adb install -r`。
2. **填密钥**：App → 设置 → 填你自己的 [OpenRouter](https://openrouter.ai/) API Key。回复模型默认 `deepseek/deepseek-chat-v3.1`。
3. **开权限**：按主页向导开三项：无障碍（读消息）、悬浮窗（展示分析）、自启动 + 省电无限制（小米 / HyperOS 必做）。

打开微信、QQ 或 X 的任意聊天窗，悬浮球出现即可用。详细说明、已知限制、适配新 App 的方法见 [仓库 README](https://github.com/jev-chat/jev-chat-jarvis#readme)。

## 正在做（v1.3）

- 判断 / 回复 / 视觉三路接口分别可配，内置 OpenRouter、TypeSafe 直连、DeepSeek 官方、通义兼容预设。
- 本地知识库与联系人档案：分析时自动带上命中的知识和这个人的历史，候选回复与你的设定一致。
- 读不到正文时截屏 + ML Kit 中文离线识别，先补飞书。
- 桌面端与网页端。

## 组织内仓库

| 仓库 | 说明 |
|---|---|
| [jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | Android 主项目（本页介绍的就是它） |
| [jev-chat-mac](https://github.com/jev-chat/jev-chat-mac) | macOS 端实现 |
| [jev-chat-windows](https://github.com/jev-chat/jev-chat-windows) | Windows 端实现 |

## 联系

合作、反馈、进群，请**公众号私信**。交流群二维码在 [仓库 README 底部](https://github.com/jev-chat/jev-chat-jarvis#交流群--需求收集)（7 天有效，过期了公众号私信要新码）。

<p align="center"><img src="https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/docs/images/wechat-mp.png" width="160" alt="公众号二维码" /></p>

<p align="center"><sub>仅供个人学习与研究使用。请遵守各软件的许可协议与当地法律法规。代码以 <a href="https://github.com/jev-chat/jev-chat-jarvis/blob/main/LICENSE">MIT</a> 协议开源。</sub></p>