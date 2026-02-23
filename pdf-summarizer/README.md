# PDF Summarizer

AI 驱动的命令行工具，快速生成 PDF/Markdown 文件的精简摘要。

## 功能

- 支持 PDF、Markdown 文件读取
- AI 自动生成 <100 字精简摘要
- 模块化架构，易于扩展

## 安装

```bash
pip install openai python-dotenv pypdf
```

## 配置

在项目根目录创建 `.env` 文件：

```
OPENROUTER_API_KEY=你的硅基流动API密钥
```

获取 API：https://cloud.siliconflow.cn/

## 使用

### 基本用法

```bash
python main.py <文件路径>
```

### 指定输出文件

```bash
python main.py <文件路径> -o <输出文件>
```

### 示例

```bash
# 摘要 Markdown 文件，输出到默认文件
python main.py article.md

# 摘要 PDF 文件，输出到指定文件
python main.py document.pdf -o summary.pdf

# 查看帮助信息
python main.py -h
```

### 参数说明

| 参数 | 说明 | 必填 |
|------|------|------|
| `file` | 输入文件路径 | 是 |
| `-o, --output` | 输出文件路径 | 否（默认：summary.md） |

## 项目结构

```
pdf-summarizer/
├── src/
│   ├── config.py        # 配置
│   ├── reader.py        # 文件读取
│   └── summarizer.py    # AI 摘要
├── main.py              # 入口
├── .env                 # API 密钥
└── README.md
```

## 配置

修改 `src/config.py`：

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `DEFAULT_MODEL` | AI 模型 | Qwen/Qwen2-7B-Instruct |
| `DEFAULT_OUTPUT` | 默认输出 | summary.md |

## License

MIT
