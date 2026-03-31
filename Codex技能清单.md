# Codex 技能清单

这份文档用于统一记录当前可用的 `skill`，方便后续查看、追加、修改和整理。

建议维护方式：

- 新增 skill：直接在“技能目录”里追加一行，并按下方模板补充说明。
- 修改 skill：优先更新“技能目录”表格，再同步修改对应的详细说明块。
- 删除 skill：从表格和详细说明中同时移除，并在“更新记录”中记一笔。
- 临时备注：直接写在“备注”列，避免把表格写得过长。

## 技能目录

| Skill 名称 | 主要用途 | 适用场景 | 路径 |
| --- | --- | --- | --- |
| `frontend-design` | 设计并实现高质量前端界面 | 落地网页、组件、页面视觉改造 | `C:/Users/33531/.codex/skills/frontend-design/SKILL.md` |
| `frontend-slides` | 制作动画丰富的 HTML 幻灯片 | 演示稿、网页 slides、视觉化讲稿 | `C:/Users/33531/.codex/skills/frontend-slides/SKILL.md` |
| `interactive-trip-planner` | 通过分阶段问答生成可执行旅行方案 | 周末游、短途旅行、路线收敛、行程报告输出 | `C:/Users/33531/OneDrive/Desktop/ai/旅游/interactive-trip-planner/SKILL.md` |
| `pptx` | 处理 `.pptx` 演示文稿 | 读取、编辑、拆分、合并、导出 PPT | `C:/Users/33531/.codex/skills/pptx/SKILL.md` |
| `wechat-essay-cards` | 生成微信公众号文章排版和图卡 | 长文排版、社媒图卡、截图式内容 | `C:/Users/33531/.codex/skills/wechat-essay-cards/SKILL.md` |
| `imagegen` | 生成或编辑位图图片 | 插画、照片风格图、贴图、素材图 | `C:/Users/33531/.codex/skills/.system/imagegen/SKILL.md` |
| `openai-docs` | 基于官方资料处理 OpenAI 文档类问题 | API 使用、模型选择、官方文档查询 | `C:/Users/33531/.codex/skills/.system/openai-docs/SKILL.md` |
| `plugin-creator` | 创建 Codex 插件脚手架 | 新建插件、补齐插件目录与配置 | `C:/Users/33531/.codex/skills/.system/plugin-creator/SKILL.md` |
| `skill-creator` | 创建或更新自定义 skill | 设计新 skill、维护 skill 说明与流程 | `C:/Users/33531/.codex/skills/.system/skill-creator/SKILL.md` |
| `skill-installer` | 安装新的 skill | 从预置来源或仓库安装 skill | `C:/Users/33531/.codex/skills/.system/skill-installer/SKILL.md` |

## 技能详细说明

### `frontend-design`

- 用途：创建有设计感、可用于生产环境的前端页面和组件。
- 适合任务：品牌页、落地页、功能页、组件重构、视觉升级。
- 备注：更偏“设计+实现一体化”，适合用户明确要做网页界面时使用。

### `frontend-slides`

- 用途：制作视觉表现更强的 HTML 幻灯片。
- 适合任务：演讲稿、提案、产品介绍、动态演示页面。
- 备注：如果目标是“网页式 slides”，优先考虑这个 skill。

### `interactive-trip-planner`

- 用途：把模糊的出游需求收敛成可执行的旅行方案，并在需要时生成 HTML/PDF 行程报告。
- 适合任务：周末游、短途旅行、多方案比较、交通与住宿收敛、可交付行程单输出。
- 备注：适合先讨论约束再逐步收敛路线，而不是一次性给出单一答案的旅行规划任务。
- 路径：`C:/Users/33531/OneDrive/Desktop/ai/旅游/interactive-trip-planner/SKILL.md`

### `pptx`

- 用途：处理所有与 `.pptx` 文件相关的工作。
- 适合任务：读取 PPT、改 PPT、生成 PPT、提取文本、整合多个演示文稿。
- 备注：只要任务里出现“presentation / deck / slides / pptx”，通常都应该启用。

### `wechat-essay-cards`

- 用途：生成适合公众号和社交传播的长文排版与图卡。
- 适合任务：公众号文章、长图、金句卡片、截图式内容编排。
- 备注：适合“内容展示型”而不是“应用交互型”页面。

### `imagegen`

- 用途：创建或编辑位图图像。
- 适合任务：插画、照片风格图、材质图、透明背景素材、视觉变体。
- 备注：如果需求更适合 HTML/CSS/SVG 实现，则不优先使用。

### `openai-docs`

- 用途：基于 OpenAI 官方文档回答或实现相关能力。
- 适合任务：API 接入、模型选择、参数说明、升级路径查询。
- 备注：强调官方来源与时效性，适合文档检索和集成类问题。

### `plugin-creator`

- 用途：创建本地 Codex 插件结构。
- 适合任务：新建插件目录、生成 `.codex-plugin/plugin.json`、补基础模板。
- 备注：适合插件初始化，不等于业务逻辑开发本身。

### `skill-creator`

- 用途：设计、创建或更新 skill。
- 适合任务：沉淀工作流、封装能力、维护技能说明文件。
- 备注：如果你后续要自己扩展 skill，这个会很有用。

### `skill-installer`

- 用途：安装新的 skill 到本地环境。
- 适合任务：导入现有 skill、从仓库安装 skill、扩展可用技能库。
- 备注：适合“引入已有 skill”，不负责定义 skill 内容本身。

## 新增 Skill 模板

复制下面这段，新增时直接填空即可：

```md
### `skill-name`

- 用途：
- 适合任务：
- 备注：
- 路径：
```

如果要同步写入“技能目录”，建议追加一行：

```md
| `skill-name` | 一句话用途 | 一句话场景 | `路径/SKILL.md` |
```

## 维护建议

- 优先保持“技能目录”简洁，详细信息写在后面的说明区。
- 路径尽量写绝对路径，方便直接定位。
- 如果 skill 有版本变化，可在名称后加括号备注版本或来源。
- 如果 skill 失效，不要只删路径，最好写清楚原因。

## 更新记录

- 2026-03-31：初始化文档，录入当前可见的 9 个 skill。
- 2026-03-31：新增 `interactive-trip-planner`，当前文档共记录 10 个 skill。
