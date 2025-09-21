# Step 1: Topic Planning & Confirmation (The first instruction to send to the AI)

Please copy and send the following content as your first instruction:

```
Your first task is to act as a topic planning expert. Please strictly follow the steps below:

1.  In-depth Reading: Carefully read and understand all the materials I provide.

2.  Information Integration & Hierarchy Division: Logically integrate all scattered information. Plan a topic and a sub-topic for each core knowledge point.
    *   Topics should be the highest-level categories (e.g., General Principles of Fractures, Upper Limb Fractures).
    *   Sub-topics should be specific knowledge points under a topic (e.g., Definition of Fracture, AO Classification, Compartment Syndrome).

3.  Topic Filtering & Grading: Based on the following criteria, suggest a mastery level for each "sub-topic".
    *   [Mastery]: ... (content unchanged)
    *   [Familiarity]: ... (content unchanged)
    *   [Awareness]: ... (content unchanged)

4.  Output Format:
    *   Your output must be only a list.
    *   Strictly follow the format: "Topic || Sub-topic - [Suggested Level]".
    *   Absolutely do not generate any card content or HTML code in this step.

5.  Await Confirmation: After outputting the list, stop working and wait for my confirmation or modification instructions.

Task begins. Please analyze the materials I provided and output your topic plan list.
```

---

# Step 2: Card Generation Instruction (The second instruction to send after you confirm or modify the AI's list)

After the AI provides the topic list, you can reply with "Agreed, please proceed" or "Change the level of the XX topic to [Familiarity], then proceed." After the AI confirms, you can then send the following final generation instruction.

Confirmation complete. Now, please strictly follow the template below and the topic/level list we have confirmed to generate the content for an Anki card file for me.

---

### I. Basic Settings

- File Format: .txt (UTF-8 encoding)
    
- Language: Chinese
    
- Content Source: Limited to the provided text and the topic list we have confirmed.
    

### II. Card Structure & Metadata

- Format: `Topic || Sub-topic || Question <code>Number of points</code> <span style="color:color">[Mastery Level]</span> Minimalist Structured Answer`
    
- Separator: A single `tab` character must be used to separate the question and answer.
    
- Mastery Level Markers:
    
    - `[Mastery]` - `color:red`
        
    - `[Familiarity]` - `color:orange`
        
    - `[Awareness]` - `color:blue`
        
- Question Design: Questions should be short, clear, and designed to trigger recall. Avoid including answer information in the question. Frequently use phrases like "What is...?", "What are the types of...?", "What are the principles of...?".
    

### III. Content & Character Count Limits

|Mastery Level|Total Character Limit|Per-Point Limit|Optimization Strategy|
|---|---|---|---|
|Mastery|120-150 characters|30-40 characters|Subheadings + Symbolization|
|Familiarity|60-80 characters|20-25 characters|Concise list|
|Awareness|20-30 characters|10-15 characters|Single-line statement|

### IV. Minimalist Structure HTML Templates

A. Mastery Level - Subheading Structure  
B. Mastery Level - Compact Table  
C. Familiarity Level - Concise List  
D. Awareness Level - Single-line Statement

#### A. Mastery Level - Subheading Structure (Uniform format, regardless of content complexity)

```html
<h3>Point 1</h3>
<ol>
  <li>Core content 1</li>
  <li>Core content 2</li>
  <li>Core content 3→Result</li>
</ol>
<h3>Point 2</h3>
<ol>
  <li>Core content→Result</li>
  <li>Supplementary content</li>
</ol>
```

#### B. Mastery Level - Compact Table (Suitable for: comparative analysis, classification)

```html
<table>
  <thead>
    <tr><th>Attribute/Feature</th><th>Category A</th><th>Category B</th><th>Category C</th></tr>
  </thead>
  <tbody>
    <tr><td><b>Attribute 1</b></td><td>Feature 1+Feature 2</td><td>Feature 1+Feature 2</td><td>Feature 1+Feature 2</td></tr>
    <tr><td><b>Attribute 2</b></td><td>Feature 1→Feature 2</td><td>Feature 1→Feature 2</td><td>Feature 1→Feature 2</td></tr>
  </tbody>
</table>
```

#### C. Familiarity Level - Concise List

```html
<ol>
  <li><b>Point 1:</b> Core content→Result</li>
  <li><b>Point 2:</b> Core content→Result</li>
</ol>
```

#### D. Awareness Level - Single-line Statement

```html
<p><b>Etiology→Symptom→Treatment</b></p>
```

### V. Symbolization & Optimization Rules

1. Standard Symbols (→, ↑↓, +, /, ±)
    
2. Medical Abbreviations
    
3. Redundancy Removal Principle
    
4. Keyword Density & Quality Control
    

### VI. Final Output Command

"Please strictly follow the template for your output. You must:"

1. Strictly adhere to the topic list and mastery levels we confirmed in the first step during generation.
    
2. Place all generated card content within a single ``` code block.
    
3. Each card must occupy a single line, with the question and answer separated by a tab.
    
4. There must be no blank lines between cards.
    
5. All HTML tags must be correctly closed, and color tags must be accurate.
    

Output Example:

```
Surgical Nutrition || Nutritional Assessment || Key indicators for nutritional assessment?<code>4</code> <span style="color:red">[Mastery]</span>	<h3>Plasma Proteins</h3><ol><li>Albumin: 20-day half-life</li><li>Prealbumin: 2-day half-life, sensitive short-term indicator</li><li>Transferrin</li></ol><h3>BMI Calculation</h3><ol><li>BMI = weight(kg)/height²(m²)</li><li>Obesity standard: Western ≥30, Asian ≥27.5</li></ol><h3>GLIM Criteria</h3><ol><li>Weight loss >10% or >5% in 3 months</li><li>BMI <18.5 or <22 for age >70</li></ol><h3>Composition Measurement</h3><ol><li>BIA: Bioelectrical Impedance Analysis</li><li>DEXA: Dual-energy X-ray Absorptiometry</li><li>CT/MRI: Precise assessment</li></ol>
Ocular Tumors & Orbital Diseases || Ocular Tumors || Clinical manifestations and management of Retinoblastoma?<code>3</code> <span style="color:red">[Mastery]</span>	<h3>Clinical Manifestations</h3><ol><li>Leukocoria</li><li>Strabismus</li><li>Glaucoma, globe enlargement</li></ol><h3>Classification</h3><ol><li>Intraocular, extraocular, metastatic types</li><li>Bilateral (hereditary), unilateral (sporadic)</li></ol><h3>Management</h3><ol><li>Early stage: globe-sparing; Late stage: enucleation</li><li>Chemotherapy, radiotherapy, laser, cryotherapy</li><li>Genetic counseling</li></ol>
```

Task begins. Please generate the final card content.