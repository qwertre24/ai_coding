import os
from pypdf import PdfReader
from src.config import SUPPORTED_EXTENSIONS


def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def read_pdf(file_path):
    reader = PdfReader(file_path)
    all_text = ""
    for page in reader.pages:
        text = page.extract_text()
        all_text += text + "\n"
    return all_text


def read_file(file_path):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    
    if ext == '.pdf':
        return read_pdf(file_path)
    elif ext == '.md':
        return read_markdown(file_path)
    else:
        raise ValueError(f"不支持的文件格式: {ext}. 支持: {SUPPORTED_EXTENSIONS}")


def is_supported(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() in SUPPORTED_EXTENSIONS
