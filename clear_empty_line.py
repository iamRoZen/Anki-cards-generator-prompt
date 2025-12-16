import os

# 在这里直接设置输入文件路径
INPUT_PATH = r"D:\python_projects\anki_cards_maker_2\input.txt"

def remove_empty_lines(text):
    """删除文本中的空行并保留Markdown格式"""
    lines = text.splitlines()
    # 保留非空行和Markdown表格分隔符行（包含 |--- 的行）
    processed_lines = [
        line for line in lines 
        if line.strip() != '' or line.lstrip().startswith('|---')
    ]
    return '\n'.join(processed_lines)

def process_markdown_file(file_path):
    """处理Markdown文件并保存结果"""
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误：文件 '{file_path}' 不存在")
        return
    
    # 检查文件扩展名
    if not file_path.lower().endswith('.md'):
        print(f"警告：文件 '{file_path}' 不是Markdown文件(.md)")
    
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 处理内容
    cleaned_content = remove_empty_lines(content)
    
    # 创建输出文件名
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    output_file = os.path.join(
        os.path.dirname(file_path),
        f"{name}_cleaned{ext if ext else '.txt'}"
    )
    
    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)
    
    print(f"处理完成！已创建: {output_file}")
    print(f"原始文件: {file_path}")
    print(f"清理后文件: {output_file}")

if __name__ == "__main__":
    # 直接使用预设的INPUT_PATH
    print(f"开始处理文件: {INPUT_PATH}")
    process_markdown_file(INPUT_PATH)