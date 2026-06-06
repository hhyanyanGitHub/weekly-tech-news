# 🚀 Weekly Tech News Digest

全球前沿科技进展周刊 - 军事与信息技术应用方向

## 📋 功能介绍

每周四下午15:00自动收集并发送全球前沿科技新闻摘要到您的邮箱，重点关注：
- 🔐 **网络与信息技术**：网络安全、密码学、零信任架构等
- 🤖 **指挥自动化技术**：AI指挥系统、自主决策、实时协调等
- 🛰️ **摄影测量与遥感技术**：卫星遥感、实时影像识别、3D重建等
- ⚔️ **军事应用突破**：新装备、战术创新、跨域融合等

## 📄 日报格式

每期日报包含不超过10条新闻，按重要性排序，内容包括：

```
┌─────────────────────────────────────────┐
│ 📌 类目：[技术分类]                      │
│                                         │
│ 标题 (Title)                            │
│ [中文标题] | [English Title]            │
│                                         │
│ 提要：                                  │
│ [核心信息摘要 150字以内]                │
│                                         │
│ 📰 信息源：[来源网站]                    │
│ 🔗 原文：[完整链接]                     │
└─────────────────────────────────────────┘
```

## 🏗️ 项目结构

```
weekly-tech-news/
├── README.md                            # 项目文档
├── requirements.txt                     # Python依赖
├── config/
│   ├── sources.yaml                     # 数据源配置（RSS、API等）
│   ├── keywords.yaml                    # 关键词和分类配置
│   └── email_template.html              # 邮件模板
├── src/
│   ├── __init__.py
│   ├── main.py                          # 主程序入口
│   ├── collector.py                     # 多源新闻收集器
│   ├── processor.py                     # 内容分析和排序
│   ├── translator.py                    # 中英文翻译
│   ├── summarizer.py                    # 内容摘要生成
│   └── emailer.py                       # 邮件发送模块
├── .github/
│   └── workflows/
│       └── weekly-digest.yml            # GitHub Actions定时任务
└── data/
    ├── samples/                         # 样本数据
    └── archives/                        # 历史日报存档
```

## 🔧 快速开始

### 1. 本地开发环境

```bash
# 克隆仓库
git clone https://github.com/hhyanyanGitHub/weekly-tech-news.git
cd weekly-tech-news

# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置环境变量

在项目根目录创建 `.env` 文件（本地开发用）：

```env
# Gmail配置
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
RECIPIENT_EMAIL=hhyanyan@gmail.com

# API密钥（可选）
NEWSAPI_KEY=your-newsapi-key
ARXIV_API_KEY=your-arxiv-key
TWITTER_BEARER_TOKEN=your-twitter-token

# 翻译服务（可选）
TRANSLATE_API_KEY=your-translate-key
```

**⚠️ 安全提示**：
- `.env` 文件已在 `.gitignore` 中，不会上传到GitHub
- Gmail用户需启用"应用专用密码"：[设置链接](https://myaccount.google.com/apppasswords)
- GitHub Actions使用Secrets存储敏感信息

### 3. 本地测试

```bash
# 测试新闻收集
python src/main.py --test

# 生成样本日报
python src/main.py --sample

# 完整运行（生成并发送日报）
python src/main.py --run
```

### 4. GitHub Actions自动化

日报将通过GitHub Actions在每周四15:00 UTC自动执行：

```yaml
# .github/workflows/weekly-digest.yml
name: Weekly Tech News Digest

on:
  schedule:
    # 每周四 15:00 UTC (GMT+0)
    # 如需调整时区，请修改此表达式
    - cron: '0 15 * * 4'
```

**时区转换参考**：
- 15:00 UTC = 23:00 CST (中国标准时) = 16:00 BST (英国) = 11:00 EDT (美国东部)

## 📰 数据源

### RSS源
- **Hacker News** - 科技社区热点
- **ArXiv** - 计算机科学论文预印本
- **CyberScoop** - 网络安全专业资讯
- **Defense News** - 防务科技动态
- **IEEE Spectrum** - 工程技术前沿
- **Ars Technica** - 科技深度报道

### 网络API
- **NewsAPI** - 多源新闻聚合
- **Twitter/X API** - 实时技术信息
- **GitHub Trending** - 热门开源项目

### 专业网站爬虫
- NATO Strategic Communications Centre
- DARPA官方发布
- 各国国防部技术公报

## 🎯 关键词分类

系统会根据以下关键词自动分类和排序：

### 网络与信息技术
- 密码学、零信任、端到端加密、blockchain
- DDoS防护、漏洞挖掘、APT、CTF竞赛
- 量子计算威胁、后量子密码

### 指挥自动化技术
- AI决策系统、机器学习指挥
- 实时数据融合、自主作战系统
- 边缘计算、5G/6G军事应用

### 摄影测量与遥感技术
- 卫星遥感、SAR成像
- 无人机影像处理、实时目标识别
- 3D重建、地形测绘

## 📊 重要性评分算法

系统通过以下因素综合评分：
1. **信息新鲜度** - 发布时间
2. **来源权威性** - 官方/一级来源权重高
3. **关键词匹配度** - 核心技术领域匹配
4. **传播热度** - 分享、引用、讨论量
5. **跨学科影响** - 多领域应用潜力

## 🔐 隐私与安全

- ✅ 邮箱密码使用GitHub Secrets加密存储
- ✅ 不存储用户数据或邮件记录
- ✅ 所有数据传输使用HTTPS/TLS加密
- ✅ 定期检查依赖包安全更新

## 📧 邮件示例

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    🚀 全球前沿科技周刊 | Weekly Digest
    2026年 第23周 | Week 23, 2026
    发布时间：周四 15:00 CST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【本期热点】TOP 10 Highlights

1️⃣ 🛰️ 摄影测量与遥感
   实时卫星遥感识别突破下视角300米精度
   Real-time Satellite Remote Sensing Achieves 300m Resolution
   
   提要：美国国防高级研究计划局(DARPA)宣布新型SAR卫星成功进行田野测试...
   
   📰 来源：DARPA Official Release
   🔗 阅读原文：https://example.com/article-1

2️⃣ 🔐 网络与信息技术
   ...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 提示：点击"阅读原文"链接查看完整报道
💬 反馈：在GitHub仓库提Issue告诉我们改进建议
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 🚀 部署到云端（可选）

### 使用GitHub Actions（推荐，免费）
✅ 已配置，无需额外部署

### 使用AWS Lambda
见 `docs/deployment/aws-lambda.md`

### 使用阿里云函数计算
见 `docs/deployment/aliyun.md`

## 📝 更新日志

### v0.1.0 (2026-06-06)
- ✨ 项目初始化
- 🏗️ 搭建核心架构
- 📰 配置多源数据采集
- ✉️ 集成邮件发送系统

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

### 如何改进
1. 添加新的数据源 → 编辑 `config/sources.yaml`
2. 改进分类算法 → 修改 `src/processor.py`
3. 调整邮件样式 → 更新 `config/email_template.html`
4. 修复bug或优化性能 → 提交PR

## 📄 许可证

MIT License - 欢迎自由使用和修改

## 📞 联系方式

- 📧 邮件反馈：hhyanyan@gmail.com
- 🐙 GitHub Issues：提交bug和建议
- 💬 讨论区：参与项目讨论

---

**⏰ 下期日报发布**：每周四 15:00 CST

**🔄 最后更新**：2026-06-06
