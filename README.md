# Anki-cards-generator-prompt

一套帮助你高效学习和记忆的 Prompt 工具集, 覆盖学习、整理、测试的完整学习闭环

---

## 项目简介

本项目包含三个核心 Prompt：

| Prompt          | 用途               |
| :-------------- | :--------------- |
| ladder-practice-cited | 新版, 带原文引用, 推荐第一次学习使用     |
| ladder-practice | 旧版, 阶梯式练习, 系统学习知识     |
| anki-card       | 将知识整理为 Anki 记忆卡片 |
| quiz-card/quiz-card-med       | 制作选择题形式的测试卡片,带med后缀适配医学专业     |

---

## 推荐使用顺序

ladder-practice-cited  →  2. anki-card  →  3. quiz-card
  （系统学习）          （整理卡片）        （巩固测试）
`ladder-practice-cited` 和 `anki-card` 在进入学习之前就直接贴给AI, 具体文本根据所需要精度复制原文, 我的习惯是逐段检阅

**为什么是这个顺序？**

1. 先学后记：通过阶梯练习建立完整的知识框架, 先学习再刷卡符合认知过程
2. 先记后测：有了 Anki 卡片的基础记忆, 再做选择题能更好地检验掌握程度
3. 循环迭代：测试中发现薄弱点, 可返回前两步针对性强化

---

## 使用步骤

### 第一步：阶梯式练习（ladder-practice）

1. 将 `ladder-practice-cited.md` 和 `anki-card.md` 的内容复制到 AI 对话框
2. 告诉 AI 你想学什么（可以上传讲义或描述知识点）
3. AI 会询问你的基础水平和薄弱点
4. 确认学习模块框架后, 逐模块完成练习或制卡
5. 每个模块包含：开篇联系 → 知识阶梯 → 综合练习 → 助记汇总 → 小结图示

### 第二步：Anki 制卡（anki-card）

1. 根据 `anki-card.md` 中的制卡规范, AI 会生成制表符分隔的卡片代码
4. 复制代码块内容, 保存为 `.txt` 文件
5. 导入 Anki（见下方导入说明）

### 第三步：选择题制卡（quiz-card）

1. 将 `quiz-card.md` 的内容复制到 AI 对话框（医学专业可用 `quiz-card-med.md`）
2. 上传你的讲义或笔记
3. AI 会生成带详细解析的选择题卡片
4. 复制代码块内容, 保存为 `.txt` 文件
5. 导入 Anki

### Anki 导入说明

项目提供了 `Template.apkg` 卡片模板, 建议先导入模板再导入卡片卡片模板名称为 `Basic-Mnemonic`, 选择题部分的模板基于 [选择题模板（单/多选自动适应）](https://ankiweb.net/shared/info/1485837001) 修改而来

**导入步骤：**

1. 打开 Anki, 点击 文件 → 导入
2. 选择保存的 `.txt` 文件
3. 字段分隔符选择 制表符（Tab）
4. 卡片模板名称选择 `Basic-Mnemonic`/ `选择题模板-copy`
5. 确认字段映射正确
6. 点击 导入 完成

---

## 文件说明

| 文件 | 说明 |
|:---|:---|
| ladder-practice.md | 阶梯式练习 Prompt |
| anki-card.md | Anki 制卡 Prompt |
| quiz-card.md | 选择题制卡 Prompt（通用版） |
| quiz-card-med.md | 选择题制卡 Prompt（医学专用版） |
| Template.apkg | Anki 卡片模板 |
| 3-steps-demo.md | 三步工作流演示示例 |

---

## 关于这个项目

最初版本的 anki-card.md 是 2024 年 5 月准备的, 2026 年 1 月复习内外妇儿的时候做了 quiz-card-med.md, 2026 年寒假为了弥补从 0 到 1 的理解困难配套研发了 ladder-practice.md, 2026年3月学期初更新了 ladder-practice-cited.md 以期启动更丝滑

我对 Anki 的理解是：Anki 如果只记忆原子化的知识点, 和医学其实不太搭, 反而和医学生刷题的用法比较配对反思鉴于从 0 到 1 的理解不能在 Anki 中完成的问题, 仿照 Anki 和中学经验性的教学思路设计了阶梯化练习让 AI 引导

---

## 关于作者

尝试使用 Anki 的医学生, 练习时长两年半, 不是很擅长背书, 但是对学习技巧比较上心

---

## 使用技巧

1. 先整体后细节：使用 ladder-practice-cited 时, 先确认模块框架再开始练习
2. 及时制卡：学完一个模块后立即使用 anki-card 制卡, 趁热打铁
3. 定期测试：用 quiz-card 生成的选择题定期自测, 发现薄弱点
4. 迭代优化：根据测试结果, 返回补充相关知识点的卡片

---

# Anki-cards-generator-prompt

A collection of prompts designed to help you learn and memorize efficiently, covering the complete learning cycle: **Learn → Organize → Test**.

---

## Overview

This project contains the following prompts:

| Prompt                        | Purpose                                                                                                              |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------- |
| **ladder-practice-cited**     | **New version (recommended for first-time learning)**. Ladder-style learning with **citations to the original text** |
| **ladder-practice**           | Older version. Ladder-style progressive exercises for systematic learning                                            |
| **anki-card**                 | Convert knowledge into Anki flashcards                                                                               |
| **quiz-card / quiz-card-med** | Create quiz-style test cards. The `-med` version is optimized for medical studies                                    |

---

## Recommended Workflow

ladder-practice-cited  →  2. anki-card  →  3. quiz-card
(Learn systematically)     (Organize)       (Test & reinforce)

> `ladder-practice-cited` and `anki-card` are designed to be pasted into the AI chat **before** you start studying.
> Paste the relevant source text based on the precision you need. My personal workflow is to review the material **paragraph by paragraph**.

### Why this order?

1. **Learn before memorize**
   Build a complete knowledge framework through ladder-style progressive exercises, then generate cards more accurately and efficiently.

2. **Memorize before test**
   With Anki cards as the baseline memory layer, quizzes can better assess true mastery.

3. **Iterate**
   Identify weak points through testing, then return to earlier steps for targeted reinforcement.

---

## How to Use

### Step 1: Ladder Practice (ladder-practice / ladder-practice-cited)

1. Copy the content of **`ladder-practice-cited.md`** (recommended) into an AI chat
   (you can also use the older `ladder-practice.md`).
2. Tell the AI what you want to learn (upload lecture notes or describe the topic).
3. The AI will ask about your current level and weak points.
4. Confirm the module framework, then complete exercises module by module.
5. Each module includes:
   **Opening connection → Knowledge ladder → Comprehensive practice → Mnemonics summary → Summary diagram**

---

### Step 2: Anki Card Creation (anki-card)

1. Copy the content of **`anki-card.md`** into an AI chat.
2. Upload your lecture notes (Markdown works best).
3. The AI will generate **tab-separated** card code.
4. Copy the code block content and save as a **`.txt`** file.
5. Import into Anki (see instructions below).

---

### Step 3: Quiz Card Creation (quiz-card / quiz-card-med)

1. Copy the content of **`quiz-card.md`** into an AI chat.
   For medical topics, use **`quiz-card-med.md`**.
2. Upload your lecture notes.
3. The AI will generate quiz cards with **detailed explanations**.
4. Copy the code block content and save as a **`.txt`** file.
5. Import into Anki.

---

## Anki Import Instructions

This project provides a card template package **`Template.apkg`**.
It is recommended to **import the template first**, then import the generated `.txt` cards.

### Template names

* Flashcards: **`Basic-Mnemonic`**
* Quiz cards: **`选择题模板-copy`**
  (modified from: Multiple Choice Template (Single/Multi Auto-adapt) — [https://ankiweb.net/shared/info/1485837001](https://ankiweb.net/shared/info/1485837001))

### Import steps

1. Open Anki → **File → Import**
2. Select the saved **`.txt`** file
3. Set **Field Separator** to **Tab**
4. Choose the correct **Note Type / Template**:

   * `Basic-Mnemonic` (for anki-card output)
   * `选择题模板-copy` (for quiz-card output)
5. Confirm the field mapping is correct
6. Click **Import**

---

## File Description

| File                     | Description                                        |
| :----------------------- | :------------------------------------------------- |
| ladder-practice-cited.md | Ladder-style learning prompt (new; with citations) |
| ladder-practice.md       | Ladder-style learning prompt (older version)       |
| anki-card.md             | Anki card creation prompt                          |
| quiz-card.md             | Quiz card creation prompt (general)                |
| quiz-card-med.md         | Quiz card creation prompt (medical)                |
| Template.apkg            | Anki card templates                                |
| 3-steps-demo.md          | Three-step workflow demo                           |

---

## About This Project

* The original **`anki-card.md`** was created in **May 2024**.
* In **January 2026**, while reviewing **internal medicine, surgery, obstetrics, and pediatrics**, I developed **`quiz-card-med.md`**.
* During the **2026 winter break**, I created **`ladder-practice.md`** to address the difficulty of building understanding **from 0 to 1**.
* In **March 2026** (early spring semester), I updated it into **`ladder-practice-cited.md`** to make the learning experience smoother, with citations to the original text.

### My view on Anki

If Anki is used only to memorize atomized facts, it doesn’t fit medical learning very well.
Medical study often matches better with a **question-driven** approach.

Since **zero-to-one understanding** cannot be achieved inside Anki alone, I designed ladder-style progressive exercises inspired by both Anki principles and traditional teaching methods, so AI can guide the learning process from comprehension to retention.

---

## About the Author

A medical student who has tried using Anki for **two and a half years**. Not great at rote memorization, but very passionate about learning techniques.

---

## Tips

1. **Big picture first**: When using `ladder-practice-cited`, confirm the module framework before starting exercises.
2. **Create cards promptly**: Generate Anki cards immediately after finishing a module, while it’s still fresh.
3. **Test regularly**: Use `quiz-card` / `quiz-card-med` for periodic self-testing.
4. **Iterate and improve**: Based on test results, go back and supplement cards for weak areas.

---

## License

MIT