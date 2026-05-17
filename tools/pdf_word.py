import os
import re
import pypandoc
import fitz  # PyMuPDF
from pathlib import Path

INPUT_DIR = r"D:\project\wiki\docs\心理相关\文献与资料\documents"
OUTPUT_DIR = r"D:\project\wiki\docs\心理相关\文献与资料\output"

os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.replace(" ", "-")

def convert_docx_to_md(docx_path, output_md_path):
    try:
        output = pypandoc.convert_file(str(docx_path), 'gfm', format='docx')
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"成功转换 Word: {docx_path.name}")
    except Exception as e:
        print(f"转换 Word 失败 {docx_path.name}: {str(e)}")

def convert_pdf_to_md(pdf_path, output_md_path):
    try:
        doc = fitz.open(pdf_path)
        md_content = []
        
        # 写入前端 Meta 抬头信息（让 MkDocs 页面更美观）
        md_content.append(f"# {pdf_path.stem}\n")
        
        for page in doc:
            # 使用 blocks 模式保留基本的段落结构
            blocks = page.get_text("blocks")
            for b in blocks:
                text = b[4].strip()
                if text:
                    # 简单的多行文本换行处理
                    md_content.append(text + "\n")
                    
        with open(output_md_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(md_content))
        print(f"成功转换 PDF: {pdf_path.name}")
    except Exception as e:
        print(f"转换 PDF 失败 {pdf_path.name}: {str(e)}")

def main():
    print("🚀 开始使用轻量化引擎批量转换文档...")
    input_path = Path(INPUT_DIR)
    
    for file_path in input_path.rglob("*"):
        if file_path.is_dir():
            continue
            
        file_ext = file_path.suffix.lower()
        clean_title = sanitize_filename(file_path.stem)
        output_md_path = Path(OUTPUT_DIR) / f"{clean_title}.md"
        
        if file_ext == ".docx":
            convert_docx_to_md(file_path, output_md_path)
        elif file_ext == ".pdf":
            convert_pdf_to_md(file_path, output_md_path)

if __name__ == "__main__":
    main()