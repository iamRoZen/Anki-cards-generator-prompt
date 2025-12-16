import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def add_same_columns_to_tsv(input_file, output_file, obsidian_url, tag):
    # 读取原文件
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 打开输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            line = line.rstrip('\n')  # 移除换行符
            
            # 按tab分割每一行
            columns = line.split('\t')
            
            # 如果有至少2列，将第二列（答案）用cloze格式包围
            if len(columns) >= 2:
                columns[1] = f"{{{{c1::{columns[1]}}}}}"
            
            # 重新拼接这一行
            modified_line = '\t'.join(columns)
            
            # 添加相同的obsidian_url和tag列
            new_line = f"{modified_line}\t{obsidian_url}\t\t{tag}\n"
            f.write(new_line)

# 示例使用
if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"
    
    # 所有行使用相同的URL和标签
    obsidian_url = ""
    tag = ""
    
    add_same_columns_to_tsv(input_file, output_file, obsidian_url, tag)
    print("处理完成！")

