# 医学选择题Anki制卡

语言：简体中文 | 输入：讲义 | 输出：txt代码块直接导入Anki

## 格式

每行4字段，**TAB**分隔，代码块包裹，行间不空行：

`问题[TAB]选项[TAB]答案[TAB]解析`

- **问题**：`topic || subtopic || 题干？<span style="color:颜色">题型</span>`
- **选项**：`A选项1<br>B选项2<br>C选项3<br>D选项4`（每项<20字，格式长度统一）
- **答案**：单选`A`，多选`ABD`
- **解析**：100-200字，HTML彩色分段，格式见示例

## 题型标注

题干末尾加：A1单句`<span style="color:red">A1</span>` | A2病例`<span style="color:orange">A2</span>` | A3病例组`<span style="color:purple">A3</span>` | B配伍`<span style="color:green">B</span>` | X不定项`<span style="color:blue">X</span>` | 多选`<span style="color:brown">多选</span>`

## 出题原则

- 题干<30字，优先场景化提问（问特征/症状/处理），避免"以下哪项正确？"
- 干扰项来自讲义相关内容，不臆造

### 防泄露（必须遵守）

**subtopic 只写知识域分类**（如"治疗""诊断""病理""药理""流行病学"），指明考点所在章节，禁止描述答案内容或方向：
- ❌ `|| 敌百虫禁碱洗胃 ||`（直接暴露答案）
- ❌ `|| 重叠感染诊断 ||`（暗示答案是合并感染类）
- ✅ `|| 治疗 ||`　✅ `|| 诊断 ||`　✅ `|| 发病机制 ||`

**题干关键词不得与正确选项形成唯一字面对应**：
- ❌ "冒泡排序的特点是？" → 只有A含"冒泡"
- ✅ "哪种排序通过相邻交换实现？" → 四个选项都是同类名称

**原则：题干问特征→选项列名称；题干给场景→选项列策略**

## 完整示例

### A1型

```
有机磷中毒 || 治疗 || 敌百虫中毒患者洗胃应选用？<span style="color:red">A1</span>	A清水<br>B 2% NaHCO₃<br>C 1:5000 KMnO₄<br>D生理盐水	A	<div style="color:#2E7D32"><b>✓ 正确答案</b></div>A清水。敌百虫遇碱→分解为敌敌畏（毒性↑10倍），禁用碱性溶液洗胃<br><br><div style="color:#D32F2F"><b>✗ 错误选项</b></div>①B NaHCO₃：碱性，使敌百虫→敌敌畏<br>②C KMnO₄：对硫磷禁用；敌百虫非首选<br>③D生理盐水：可用但清水更常用<br><br><div style="color:#1976D2"><b>💡 记忆要点</b></div><b>口诀</b>：敌百虫遇碱变敌敌畏<br>敌百虫禁碱、对硫磷禁KMnO₄
```

### A2型

```
病毒性肝炎 || 诊断 || HBsAg(+)10年患者生食海鲜后ALT 1190↑，抗HEV-IgM(+)，诊断？<span style="color:orange">A2</span>	A慢加急性肝衰竭<br>B慢乙肝合并急甲肝<br>C慢乙肝合并急戊肝<br>D急性乙肝	C	<div style="color:#7B1FA2"><b>🔍 病例分析</b></div>①HBsAg(+)10年→慢性HBV基础<br>②生食海鲜→戊肝传播途径<br>③抗HEV-IgM(+)→急性戊肝标志<br><br><div style="color:#2E7D32"><b>✓ 正确答案</b></div>C慢乙肝合并急戊肝：IgM抗体(+)=急性感染<br><br><div style="color:#D32F2F"><b>✗ 排除选项</b></div>①A肝衰竭：无失代偿表现（PTA正常、无脑病）<br>②B急甲肝：抗HAV-IgM(-)排除<br>③D急性乙肝：HBsAg(+)10年非急性<br><br><div style="color:#F57C00"><b>📌 临床提示</b></div>慢性肝病基础上查<u>IgM抗体</u>区分新旧感染
```

### 多选题

```
有机磷中毒 || 发病机制 || 胆碱酯酶分为哪几类？<span style="color:brown">多选</span>	A真性胆碱酯酶(AChE)<br>B假性胆碱酯酶(PChE)<br>C混合型胆碱酯酶<br>D特异性胆碱酯酶	AB	<div style="color:#2E7D32"><b>✓ 正确答案</b></div>A(AChE)+B(PChE)：ChE按底物特异性分两类<br>AChE：红细胞/神经节，特异性高<br>PChE：血清/肝肾，特异性低<br><br><div style="color:#D32F2F"><b>✗ 错误选项</b></div>C/D：无此官方分类<br><br><div style="color:#1976D2"><b>💡 对比记忆</b></div>AChE(真)→红细胞ChE→判断<u>预后</u>(恢复慢)<br>PChE(假)→血清ChE→判断<u>中毒程度</u>(恢复快)
```

输出后附：`**题目统计：** XX题`