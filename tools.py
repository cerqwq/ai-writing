"""
AI Writing - AI写作工具
支持文章、小说、剧本、文案生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIWritingTools:
    """
    AI写作工具
    支持：文章、小说、剧本、文案
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_article(self, topic: str, style: str, length: str) -> str:
        """生成文章"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请写一篇关于"{topic}"的文章：

风格：{style}
字数：{length}

要求：
1. 结构清晰
2. 内容充实
3. 语言流畅"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def generate_story(self, genre: str, theme: str, characters: List[str]) -> str:
        """生成故事"""
        if not self.client:
            return "LLM客户端未配置"

        characters_text = ", ".join(characters)

        prompt = f"""请写一个{genre}故事：

主题：{theme}
角色：{characters_text}

要求：
1. 引人入胜的开头
2. 起承转合
3. 生动的人物描写
4. 出人意料的结局"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5000
        )

        return response.choices[0].message.content

    def generate_script(self, genre: str, scenes: int, characters: List[str]) -> str:
        """生成剧本"""
        if not self.client:
            return "LLM客户端未配置"

        characters_text = ", ".join(characters)

        prompt = f"""请写一个{genre}剧本：

场景数：{scenes}
角色：{characters_text}

要求：
1. 标准剧本格式
2. 场景描述
3. 对话生动
4. 舞台指示"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=5000
        )

        return response.choices[0].message.content

    def generate_copywriting(self, product: str, audience: str, style: str) -> Dict:
        """生成文案"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{product}生成{style}风格的文案：

目标人群：{audience}

请返回JSON格式：
{{
    "headline": "标题",
    "subheadline": "副标题",
    "body": "正文",
    "cta": "行动号召",
    "slogans": ["口号1", "口号2"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"copywriting": content}

    def generate_poem(self, theme: str, style: str, length: str) -> str:
        """生成诗歌"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请写一首关于"{theme}"的{style}风格诗歌：

长度：{length}

要求：
1. 意境优美
2. 押韵
3. 富有意境"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def rewrite_content(self, content: str, style: str) -> str:
        """改写内容"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请将以下内容改写为{style}风格：

{content}

要求：
1. 保持原意
2. 改善表达
3. 符合目标风格"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_outline(self, topic: str, sections: int) -> str:
        """生成大纲"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为"{topic}"生成{sections}个章节的大纲：

要求：
1. 逻辑清晰
2. 层次分明
3. 包含要点"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content


def create_tools(**kwargs) -> AIWritingTools:
    """创建写作工具"""
    return AIWritingTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Writing Tools")
    print()

    # 测试
    article = tools.generate_article("人工智能发展趋势", "专业", "1000字")
    print(article[:300] + "...")
