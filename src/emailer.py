#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Email Module
邮件模块

生成并发送格式化的邮件日报
"""

import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict
from datetime import datetime

logger = logging.getLogger(__name__)

class EmailDigestGenerator:
    """邮件日报生成器"""
    
    def __init__(self, config: Dict):
        """初始化生成器
        
        Args:
            config: 配置字典
        """
        self.config = config
    
    def generate_html(self, items: List[Dict], week: int, year: int) -> str:
        """生成HTML邮件内容
        
        Args:
            items: 新闻列表
            week: 第几周
            year: 年份
            
        Returns:
            HTML字符串
        """
        html = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
                .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; text-align: center; }}
                .digest-item {{ border-left: 4px solid #667eea; padding: 20px; margin: 15px 0; background: #f8f9fa; }}
                .rank {{ font-size: 24px; font-weight: bold; color: #667eea; }}
                .category {{ color: #667eea; font-weight: bold; font-size: 14px; }}
                .title {{ font-size: 18px; font-weight: bold; margin: 10px 0; }}
                .title_en {{ color: #666; font-size: 14px; margin-bottom: 10px; }}
                .summary {{ color: #333; line-height: 1.6; margin: 10px 0; }}
                .meta {{ color: #999; font-size: 12px; margin-top: 10px; }}
                .source-link {{ color: #667eea; text-decoration: none; font-weight: bold; }}
                .footer {{ background: #f0f0f0; padding: 20px; text-align: center; color: #666; font-size: 12px; margin-top: 30px; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🚀 全球前沿科技进展周刊</h1>
                <h2>Week {week} {year}</h2>
                <p>每周四发布 | 聚焦网络、指挥自动化、遥感等前沿技术</p>
            </div>
            
            <div style="max-width: 800px; margin: 0 auto; padding: 20px;">
                <h2 style="color: #333;">📰 本周TOP {len(items)}</h2>
        """
        
        for idx, item in enumerate(items, 1):
            html += f"""
                <div class="digest-item">
                    <div class="rank">#{idx}</div>
                    <div class="category">{item.get('primary_category', '技术')}</div>
                    <div class="title">{item.get('title', '')}</div>
                    <div class="title_en">{item.get('title_en', item.get('title', ''))}</div>
                    <div class="summary">{item.get('summary', '')}</div>
                    <div class="meta">
                        📰 来源: {item.get('source', 'Unknown')}<br>
                        ⭐ 重要性: {item.get('importance_score', 0)}/100<br>
                        <a href="{item.get('link', '#')}" class="source-link">🔗 阅读原文 →</a>
                    </div>
                </div>
            """
        
        html += """
            </div>
            
            <div class="footer">
                <p>💡 提示：点击"阅读原文"查看完整报道</p>
                <p>📧 如有改进建议，欢迎反馈至 hhyanyan@gmail.com</p>
                <p>© 2026 Weekly Tech News Digest</p>
            </div>
        </body>
        </html>
        """
        
        return html
    
    def send_email(self, recipient: str, subject: str, html_content: str, 
                   sender_email: str, sender_password: str) -> bool:
        """发送邮件
        
        Args:
            recipient: 收件人邮箱
            subject: 邮件主题
            html_content: HTML内容
            sender_email: 发送者邮箱
            sender_password: 发送者密码（Gmail应用专用密码）
            
        Returns:
            是否发送成功
        """
        try:
            logger.info(f"准备发送邮件到 {recipient}...")
            
            # 创建邮件
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = sender_email
            msg['To'] = recipient
            
            # 添加HTML内容
            part = MIMEText(html_content, 'html', 'utf-8')
            msg.attach(part)
            
            # 发送邮件（Gmail SMTP）
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, sender_password)
                server.send_message(msg)
            
            logger.info(f"✅ 邮件发送成功")
            return True
            
        except Exception as e:
            logger.error(f"❌ 邮件发送失败: {e}")
            return False
    
    def send_digest(self, items: List[Dict], week: int, year: int,
                    recipient: str, sender_email: str, sender_password: str) -> bool:
        """发送完整日报
        
        Args:
            items: 新闻列表
            week: 周数
            year: 年份
            recipient: 收件人
            sender_email: 发送者邮箱
            sender_password: 发送者密码
            
        Returns:
            是否成功
        """
        # 生成主题
        now = datetime.now()
        subject = f"🚀 全球前沿科技周刊 - 第{week}周 {year}年 ({now.strftime('%Y-%m-%d')})"
        
        # 生成HTML
        html = self.generate_html(items, week, year)
        
        # 发送邮件
        return self.send_email(recipient, subject, html, sender_email, sender_password)
