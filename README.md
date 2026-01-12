# Anki-cards-generator-prompt

一套帮助你高效学习和记忆的 Prompt 工具集，覆盖学习、整理、测试的完整学习闭环。

---

## 项目简介

本项目包含三个核心 Prompt：

| Prompt          | 用途               |
| :-------------- | :--------------- |
| ladder-practice | 阶梯式练习，系统学习知识     |
| anki-card       | 将知识整理为 Anki 记忆卡片 |
| quiz-card       | 制作选择题形式的测试卡片     |

---

## 推荐使用顺序

```
1. ladder-practice  →  2. anki-card  →  3. quiz-card
   （系统学习）          （整理卡片）       （巩固测试）
```

**为什么是这个顺序？**

1. 先学后记：通过阶梯练习建立完整的知识框架，再制作卡片效率更高
2. 先记后测：有了 Anki 卡片的基础记忆，再做选择题能更好地检验掌握程度
3. 循环迭代：测试中发现薄弱点，可返回前两步针对性强化

---

## 使用步骤

### 第一步：阶梯式练习（ladder-practice）

1. 将 `ladder-practice.md` 的内容复制到 AI 对话框
2. 告诉 AI 你想学什么（可以上传讲义或描述知识点）
3. AI 会询问你的基础水平和薄弱点
4. 确认学习模块框架后，逐模块完成练习
5. 每个模块包含：开篇联系 → 知识阶梯 → 综合练习 → 助记汇总 → 小结图示

### 第二步：Anki 制卡（anki-card）

1. 将 `anki-card.md` 的内容复制到 AI 对话框
2. 上传你的讲义或笔记（MD 格式最佳）
3. AI 会生成制表符分隔的卡片代码
4. 复制代码块内容，保存为 `.txt` 文件
5. 导入 Anki（见下方导入说明）

### 第三步：选择题制卡（quiz-card）

1. 将 `quiz-card.md` 的内容复制到 AI 对话框（医学专业可用 `quiz-card-med.md`）
2. 上传你的讲义或笔记
3. AI 会生成带详细解析的选择题卡片
4. 复制代码块内容，保存为 `.txt` 文件
5. 导入 Anki

### Anki 导入说明

项目提供了 `Template.apkg` 卡片模板，建议先导入模板再导入卡片。

选择题部分的模板基于 [选择题模板（单/多选自动适应）](https://ankiweb.net/shared/info/1485837001) 修改而来。

**导入步骤：**

1. 打开 Anki，点击 文件 → 导入
2. 选择保存的 `.txt` 文件
3. 字段分隔符选择 制表符（Tab）
4. 确认字段映射正确
5. 点击 导入 完成

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

最初版本的 anki-card.md 是 2024 年 5 月准备的，2026 年 1 月复习内外妇儿的时候做了 quiz-card-med.md，最后 2026 年寒假为了弥补从 0 到 1 的理解困难配套研发了 ladder-practice.md。

我对 Anki 的理解是：Anki 如果只记忆原子化的知识点，和医学其实不太搭，反而和医学生刷题的用法比较配对。反思鉴于从 0 到 1 的理解不能在 Anki 中完成的问题，仿照 Anki 和中学经验性的教学思路设计了阶梯化练习让 AI 引导。

---

## 关于作者

尝试使用 Anki 的医学生，练习时长两年半，不是很擅长背书，但是对学习技巧比较上心。

---

## 使用技巧

1. 先整体后细节：使用 ladder-practice 时，先确认模块框架再开始练习
2. 及时制卡：学完一个模块后立即使用 anki-card 制卡，趁热打铁
3. 定期测试：用 quiz-card 生成的选择题定期自测，发现薄弱点
4. 迭代优化：根据测试结果，返回补充相关知识点的卡片

---

## License

MIT

# Anki-cards-generator-prompt

A collection of prompts designed to help you learn and memorize efficiently, covering the complete learning cycle: Learn, Organize, and Test.

---

## Overview

This project contains three core prompts:

| Prompt | Purpose |
|:---|:---|
| ladder-practice | Progressive exercises for systematic learning |
| anki-card | Convert knowledge into Anki flashcards |
| quiz-card | Create quiz-style test cards |

---

## Recommended Workflow

```
1. ladder-practice  →  2. anki-card  →  3. quiz-card
   (Learn)              (Organize)       (Test)
```

**Why this order?**

1. Learn before memorize: Build a complete knowledge framework through progressive exercises, then create cards more efficiently
2. Memorize before test: With Anki cards as foundation, quizzes better assess your mastery
3. Iterate: Identify weak points through testing, return to previous steps for targeted reinforcement

---

## How to Use

### Step 1: Progressive Exercises (ladder-practice)

1. Copy the content of `ladder-practice.md` into an AI chat
2. Tell the AI what you want to learn (upload lecture notes or describe the topic)
3. The AI will ask about your current level and weak points
4. Confirm the module framework, then complete exercises module by module
5. Each module includes: Opening connection → Knowledge ladder → Comprehensive practice → Mnemonics summary → Summary diagram

### Step 2: Anki Card Creation (anki-card)

1. Copy the content of `anki-card.md` into an AI chat
2. Upload your lecture notes (MD format works best)
3. The AI will generate tab-separated card code
4. Copy the code block content and save as a `.txt` file
5. Import into Anki (see import instructions below)

### Step 3: Quiz Card Creation (quiz-card)

1. Copy the content of `quiz-card.md` into an AI chat (use `quiz-card-med.md` for medical topics)
2. Upload your lecture notes
3. The AI will generate quiz cards with detailed explanations
4. Copy the code block content and save as a `.txt` file
5. Import into Anki

### Anki Import Instructions

The project includes a `Template.apkg` card template. It's recommended to import the template before importing cards.

The quiz card template is modified from [Multiple Choice Template (Single/Multi Auto-adapt)](https://ankiweb.net/shared/info/1485837001).

**Import steps:**

1. Open Anki, click File → Import
2. Select the saved `.txt` file
3. Set field separator to Tab
4. Confirm field mapping is correct
5. Click Import to finish

---

## File Description

| File | Description |
|:---|:---|
| ladder-practice.md | Progressive exercises prompt |
| anki-card.md | Anki card creation prompt |
| quiz-card.md | Quiz card creation prompt (general) |
| quiz-card-med.md | Quiz card creation prompt (medical) |
| Template.apkg | Anki card template |
| 3-steps-demo.md | Three-step workflow demo |

---

## About This Project

The original anki-card.md was created in May 2024. In January 2026, while reviewing internal medicine, surgery, obstetrics, and pediatrics, I developed quiz-card-med.md. Finally, during the 2026 winter break, I created ladder-practice.md to address the difficulty of understanding concepts from scratch.

My understanding of Anki: If Anki only memorizes atomized knowledge points, it doesn't really fit well with medical studies. Instead, it pairs better with the quiz-based approach that medical students use. Reflecting on the problem that zero-to-one understanding cannot be achieved in Anki, I designed the progressive exercises following Anki's principles and traditional teaching methods to let AI guide the learning process.

---

## About the Author

A medical student trying to use Anki, with two and a half years of practice. Not great at rote memorization, but passionate about learning techniques.

---

## Tips

1. Big picture first: When using ladder-practice, confirm the module framework before starting exercises
2. Create cards promptly: Make anki-cards immediately after completing a module while the knowledge is fresh
3. Test regularly: Use quiz-card generated questions for regular self-testing to identify weak points
4. Iterate and improve: Based on test results, go back to supplement cards for weak areas

---

## License

MIT

