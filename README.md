# ✍️ AI Writing

AI写作工具，支持文章、小说、剧本、文案生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 文章生成
- 📖 故事生成
- 🎬 剧本生成
- 📢 文案生成
- 📝 诗歌生成
- 🔄 内容改写
- 📋 大纲生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_writing import create_tools

tools = create_tools()

# 文章
article = tools.generate_article("AI发展趋势", "专业", "1000字")

# 故事
story = tools.generate_story("科幻", "时间旅行", ["科学家", "AI"])

# 剧本
script = tools.generate_script("喜剧", 5, ["主角", "配角"])

# 文案
copy = tools.generate_copywriting("智能手表", "年轻人", "时尚")

# 诗歌
poem = tools.generate_poem("春天", "现代诗", "短诗")

# 改写
rewritten = tools.rewrite_content(text, "casual")

# 大纲
outline = tools.generate_outline("Python教程", 10)
```

## 📁 项目结构

```
ai-writing/
├── tools.py       # 写作工具核心
└── README.md
```

## 📄 许可证

MIT License
