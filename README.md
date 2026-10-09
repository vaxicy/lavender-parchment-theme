<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/lavender-parchment-theme/main/assets/icon.png" alt="Lavender Parchment Theme logo" width="128">
</p>

<h1 align="center">Lavender Parchment Theme</h1>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=lilinhuang.lavender-parchment-theme"><img src="https://img.shields.io/badge/VS%20Code-Theme-826F95?logo=visual-studio-code" alt="VS Code Theme"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-514A52?logo=visual-studio-code" alt="version 1.0.0">
  <img src="https://img.shields.io/badge/Variants-Light%20%26%20Dark-CCC2D1?logo=visual-studio-code" alt="Light and Dark variants">
  <a href="https://github.com/vaxicy/lavender-parchment-theme/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Non--Commercial-lightgrey" alt="License: Non-Commercial"></a>
</p>

A letter on an old desk for VS Code: **warm parchment** paper, **quiet lavender-grey** ink, **soft beige** panels and **deep wisteria** accents. The light variant reads like an old letter in daylight, the dark one like the same letter under a lamp — both cut from one palette, so switching changes the light level rather than the character of the workspace.

一张书桌上旧信纸配色的 VS Code 主题：**暖羊皮纸**的纸面、**沉静灰紫**的墨迹、**柔和米棕**的面板与**深紫罗兰**的点缀。浅色版像日光下的旧信，深色版像同一封信在灯下；两套变体共享同一套色板，切换时改变的是明暗而非气质。

## Preview / 预览

| Light 浅色 | Dark 深色 |
| --- | --- |
| ![Lavender Parchment Theme Light](https://raw.githubusercontent.com/vaxicy/lavender-parchment-theme/main/store-assets/screenshots/en/screenshot-light.png) | ![Lavender Parchment Theme Dark](https://raw.githubusercontent.com/vaxicy/lavender-parchment-theme/main/store-assets/screenshots/en/screenshot-dark.png) |

> Both previews are captured from a real VS Code window running the theme — no mockups.
>
> 上方预览图取自真实运行该主题的 VS Code 窗口截图，非模拟图。

## Palette / 色板

| Role | Light | Dark |
| --- | --- | --- |
| Editor background | `#F6F1E5` warm parchment | `#302A34` charcoal violet |
| Foreground | `#514A52` muted ink | `#EAE3D7` warm paper |
| Muted text / placeholders | `#827288` | `#947F9B` |
| Side bar | `#EEE7E2` with `#65564F` text | `#2C2528` with `#CDBDB4` text |
| Panel / terminal | `#F0EADF` | `#29242D` |
| Title bar | `#EAE3E9` with `#574B60` text | `#25212A` with `#D2C7D7` text |
| Tab bar / inactive tab | `#E8E0E6` | `#26212C` |
| Active tab indicator | `#826F95` | `#B29CC5` |
| Activity bar | `#DED5E2` with `#78628B` icons | `#211D27` with `#CCC2D1` icons |
| Status bar | `#DCD1E1` with `#614D73` text | `#46384F` with `#E5D9EC` text |
| Selection | `#DCD1E2` lavender wash | `#5A4766` deep violet |
| Current line | `#EEE7DC` | `#3A313E` |
| Borders / indent guides | `#D8CDD5` / `#E0D8CD` | `#4B3E50` / `#463A4B` |
| Button | `#826F95` with white text (hover `#725E86`) | `#CCC2D1` with `#3F314A` text (hover `#DED1E5`) |
| Badge | `#826F95` with white text | `#CCC2D1` with `#3F314A` text |
| Cursor | `#826F95` | `#F6F1E5` |
| Links | `#87479D` | `#D8B7E3` |
| Errors / warnings | `#AF5E69` / `#98743C` | `#E3A0AC` / `#DDC18D` |
| Git added / modified / deleted | `#74885E` / `#A0845C` / `#AE7780` | `#B6CCA2` / `#D9BF98` / `#D9A3AE` |

Brand palette: lavender grey `#CCC2D1`, parchment `#F6F1E5`, warm beige `#D6BEB3`, wisteria violet `#826F95`.

品牌色板：薰衣草灰紫 `#CCC2D1`、羊皮纸奶油 `#F6F1E5`、暖米棕 `#D6BEB3`、深紫罗兰 `#826F95`。

## Syntax mapping / 语法映射

| Syntax | Light | Dark |
| --- | --- | --- |
| Comments | `#9A9185` italic | `#A39785` italic |
| Keywords / storage | `#82608F` muted violet | `#C5A7D7` pale lilac |
| Strings | `#687955` sage | `#BECCA9` soft sage |
| Regexp | `#936AA2` | `#DABBE5` |
| Escapes | `#9B7954` | `#E8C79B` |
| Numbers / constants | `#9B7357` clay | `#D6BEB3` beige |
| Types / classes / interfaces | `#946C88` | `#D7B5CC` |
| Functions / methods | `#6C7397` dusty blue | `#BDC4E2` pale periwinkle |
| Properties | `#587D7B` | `#B1CFCA` |
| Variables | `#514A52` | `#EAE3D7` |
| Parameters | `#837461` | `#D1C2AE` |
| Operators | `#84708D` | `#C3AFCB` |
| Punctuation | `#978A98` | `#AD9AAF` |
| Tags | `#82608F` | `#CCC2D1` |
| Attributes | `#9B7357` | `#DECAAB` |
| Headings / bold / italic | `#54395D` | `#EFE2F4` |
| Invalid | `#B65353` | `#E99B91` |

Keywords stay violet in both variants, strings stay a muted sage and numbers keep their clay-to-beige warmth, so the syntax reads the same whichever variant you use.

关键字在两套变体中都是紫色系，字符串始终是柔和的鼠尾草绿，数字保持陶土到米棕的暖调，因此换变体不会换掉语法的读感。

## Coverage / 覆盖范围

Every surface below is themed in both variants (144 UI colors each):

- **Editor** — background, foreground, selection and inactive selection, current-line highlight, word and selection highlights, find match and find highlight, bracket-match background and border, cursor, line numbers (plus the active line number), indent guides, whitespace, ruler, errors, warnings and info.
- **Workbench chrome** — activity bar, badge and active border, title bar (active and inactive), side bar with section headers and border, status bar (normal, no-folder and debugging states), editor group header and tabs (active, inactive, hover, modified border and active top border).
- **Panels and overlays** — panel, editor widgets, hover widget, suggest widget, dropdowns, inputs and placeholder text, notifications, quick input, and the focus border.
- **Lists** — active, inactive and hover selection backgrounds, plus the highlight and focus-highlight colors, and tree indent guides.
- **Terminal** — background, foreground and the full 16-color ANSI palette, matched to the theme.
- **Details** — workbench borders, scrollbar sliders, git decoration colors (added / modified / deleted) with their gutter markers, buttons, badges, diff editor backgrounds, and semantic token colors for variable, parameter, property, function, method, type, class and interface.

以下区域在两套变体中均已配色（每套 144 个 UI 颜色）：编辑器本体（选区与失焦选区、当前行、词/选区高亮、查找匹配与高亮、括号匹配、光标、行号、标尺、缩进线、空白符、错误/警告/提示）；活动栏与角标、标题栏、侧边栏（含分节标题）、状态栏（含无文件夹与调试态）、标签栏；面板与各类浮窗（悬停、建议、通知、快速输入）、下拉与输入框、列表选中/悬停/高亮、树缩进线；终端 ANSI 全色；全部边框与滚动条、Git 装饰色与 gutter 标记、按钮与角标、差异编辑器底色，以及变量/参数/属性/函数/方法/类型/类/接口的语义高亮。完整的颜色清单见 `COLOR-SPEC.md`。

## Features / 功能

- **Two coordinated variants** — `Lavender Parchment Theme Light` and `Lavender Parchment Theme Dark` ship in one extension.
- **One parchment palette** — warm cream and charcoal-violet surfaces with quiet lavender, beige and wisteria accents.
- **Readable syntax colors** — muted-violet keywords, sage strings and clay numbers, tuned for contrast on both backgrounds.
- **Semantic highlighting** enabled, so language-aware tokens are colored beyond the classic TextMate scopes.
- **Terminal ANSI colors** taken from the same palette, so the integrated terminal sits inside the theme.

- **明暗两套协调变体**——同一扩展内含 `Lavender Parchment Theme Light` 与 `Lavender Parchment Theme Dark`。
- **一套羊皮纸色板**——暖奶油与炭紫底色，配沉静灰紫、暖米棕与紫罗兰点缀。
- **可读的语法配色**——灰紫关键字、鼠尾草绿字符串、陶土色数字，在明暗底色上均保持对比。
- **启用语义高亮**，在传统 TextMate scope 之外为语言感知的 token 着色。
- **终端 ANSI 配色**取自同一色板，集成终端与主题融为一体。

## Installation / 安装

Requires VS Code 1.80 or newer.

1. Search for **Lavender Parchment Theme** in the Extensions view (`Ctrl+Shift+X` / `Cmd+Shift+X`), or open the [Marketplace page](https://marketplace.visualstudio.com/items?itemName=lilinhuang.lavender-parchment-theme).
2. Or install from a VSIX: download `lavender-parchment-theme-1.0.0.vsix`, open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run **Extensions: Install from VSIX...**.

需要 VS Code 1.80 或更高版本。

1. 在扩展面板（`Ctrl+Shift+X` / `Cmd+Shift+X`）搜索 **Lavender Parchment Theme**，或打开 [Marketplace 页面](https://marketplace.visualstudio.com/items?itemName=lilinhuang.lavender-parchment-theme)。
2. 也可以从 VSIX 安装：下载 `lavender-parchment-theme-1.0.0.vsix`，打开命令面板（`Ctrl+Shift+P` / `Cmd+Shift+P`），运行 **Extensions: Install from VSIX...** 并选择该文件。

Or from the command line:

或使用命令行：

```
ext install lilinhuang.lavender-parchment-theme
```

## Activation / 启用

Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`), run **Preferences: Color Theme**, and choose **Lavender Parchment Theme Light** or **Lavender Parchment Theme Dark**.

To switch between the two variants quickly, use the keyboard shortcut `Ctrl+K Ctrl+T` at any time.

打开命令面板（`Ctrl+Shift+P` / `Cmd+Shift+P`），运行 **Preferences: Color Theme**，选择 **Lavender Parchment Theme Light** 或 **Lavender Parchment Theme Dark**。

随时可用快捷键 `Ctrl+K Ctrl+T` 在两套变体之间快速切换。

## Development / 开发

Open this folder in VS Code and press `F5` to launch an Extension Development Host with the theme loaded. Regenerate the real-window preview screenshots with:

在 VS Code 中打开本文件夹并按 `F5`，在扩展开发宿主中预览主题。重新生成真实窗口预览图：

```bash
python3 scripts/capture-real-screenshots.py
```

The script builds a throwaway VS Code profile, installs this theme into it, opens the sample project under `scripts/demo-project` and captures the window for both variants into `store-assets/screenshots/en/`.

脚本会临时创建一个独立的 VS Code 配置目录，把本主题装进去，打开 `scripts/demo-project` 示例工程，并把两套变体的窗口截图输出到 `store-assets/screenshots/en/`。

Check a build before publishing:

发布前自查：

```bash
python3 scripts/validate.py
```

It refreshes `COLOR-SPEC.md` from the theme JSON files, verifies that every color value is a valid hex code, checks that the screenshot edges match `titleBar.activeBackground`, and — when a `.vsix` is present — verifies the manifest publisher, version and theme entries.

脚本会依据主题 JSON 重新生成 `COLOR-SPEC.md`，校验所有颜色值均为合法十六进制，检查截图首行/首列与 `titleBar.activeBackground` 一致，并在存在 `.vsix` 时校验清单里的发布者、版本与主题条目。

Package the extension with:

打包扩展：

```bash
vsce package
```

## License / 许可

Released under the **Non-Commercial License** — licensed for personal, educational and non-commercial use. See [LICENSE](LICENSE) for details.

基于 **Non-Commercial License（非商业使用许可）** 发布，可用于个人、教育及非商业用途，详见 [LICENSE](LICENSE)。

## Feedback / 反馈

Found an unthemed area or want a tweak? Open an issue at [github.com/vaxicy/lavender-parchment-theme/issues](https://github.com/vaxicy/lavender-parchment-theme/issues).

发现没有配色的区域或想调整某处颜色，欢迎在 [GitHub Issues](https://github.com/vaxicy/lavender-parchment-theme/issues) 反馈。

## Publisher / 发布者

Published by **lilinhuang** on the Visual Studio Code Marketplace.

由 **lilinhuang** 发布于 Visual Studio Code Marketplace。
