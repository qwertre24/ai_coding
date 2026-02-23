import argparse
from src import config, reader, summarizer


def main():
    parser = argparse.ArgumentParser(description="PDF/MD文档摘要生成器")
    parser.add_argument("file", help="要处理的文件路径")
    parser.add_argument("--output", "-o", help="输出文件路径", default=config.DEFAULT_OUTPUT)
    
    args = parser.parse_args()
    
    print(f"准备处理文件: {args.file}")
    print(f"输出到: {args.output}")
    
    if not config.API_KEY:
        print("错误：未找到API密钥")
        print("请在.env文件中设置OPENROUTER_API_KEY")
        return 1
    
    try:
        print("正在读取文件...")
        content = reader.read_file(args.file)
        print(f"文件读取成功，共 {len(content)} 个字符")
        
        print("正在生成摘要...")
        summary = summarizer.summarize(content)
        
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(summary)
        
        print(f"摘要已保存到: {args.output}")
        return 0
        
    except FileNotFoundError:
        print(f"错误：文件不存在: {args.file}")
        return 1
    except ValueError as e:
        print(f"错误：{e}")
        return 1
    except Exception as e:
        print(f"发生错误: {e}")
        return 1


if __name__ == "__main__":
    exit(main())
