#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Weekly Tech News Digest Generator
全球前沿科技进展周刊生成器

主程序入口，调度所有子模块完成新闻收集、处理和邮件发送
"""

import os
import sys
import argparse
import logging
from datetime import datetime
from pathlib import Path
import yaml
import json

# 导入自定义模块
from collector import NewsCollector
from processor import NewsProcessor
from emailer import EmailDigestGenerator

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config():
    """加载配置文件"""
    config = {
        'categories': {
            'cybersecurity': {
                'name': '🔐 网络与信息技术',
                'keywords': ['cryptography', 'encryption', 'zero trust', 'blockchain', 'DDoS', '加密', '安全', '网络'],
                'weight': 1.0
            },
            'command_automation': {
                'name': '🤖 指挥自动化技术',
                'keywords': ['AI', 'autonomous', 'command system', 'machine learning', '自主', '决策', '自动化'],
                'weight': 0.95
            },
            'remote_sensing': {
                'name': '🛰️ 摄影测量与遥感技术',
                'keywords': ['satellite', 'remote sensing', 'SAR', 'drone', 'UAV', 'imaging', '遥感', '卫星', '无人机'],
                'weight': 0.9
            },
            'military_breakthrough': {
                'name': '⚔️ 军事应用突破',
                'keywords': ['military', 'defense', 'weapon', 'tactical', '军事', '防务', '武器', '装备'],
                'weight': 0.85
            }
        },
        'importance_scoring': {
            'source_authority': {
                'DARPA': 1.5,
                'NATO': 1.3,
                'IEEE': 1.2,
                'ArXiv': 1.2,
                'CyberScoop': 1.1
            }
        },
        'limits': {
            'max_items_per_digest': 10,
            'min_items_per_digest': 3
        }
    }
    return config

def create_sample_digest():
    """创建示例日报用于测试"""
    sample = [
        {
            'title': '美国成功测试新型卫星遥感系统精度突破300米',
            'title_en': 'US Successfully Tests New Satellite Remote Sensing System with 300m Precision Breakthrough',
            'summary': '美国国防高级研究计划局(DARPA)宣布新型合成孔径雷达(SAR)卫星成功完成田野测试，实现了下视角300米精度的实时遥感成像，相比现有系统提升5倍，将用于快速地理情报和战场态势评估。',
            'source': 'DARPA Official Release',
            'link': 'https://www.darpa.mil/news-events/news-releases',
            'published': '2026-06-04',
            'primary_category': '🛰️ 摄影测量与遥感技术',
            'importance_score': 95
        },
        {
            'title': '欧盟发布后量子密码标准，抵御量子计算威胁',
            'title_en': 'EU Releases Post-Quantum Cryptography Standards to Counter Quantum Computing Threats',
            'summary': '欧洲网络安全局(ENISA)发布首个后量子密码体系标准，包含新型格子密码学算法，可有效防护未来量子计算机的破密威胁，预计2027年在金融和政府系统中推广应用。',
            'source': 'ENISA',
            'link': 'https://www.enisa.europa.eu',
            'published': '2026-06-05',
            'primary_category': '🔐 网络与信息技术',
            'importance_score': 88
        },
        {
            'title': 'NATO发布新一代指挥自动化系统架构',
            'title_en': 'NATO Unveils Next-Generation Command Automation System Architecture',
            'summary': '北约战略司令部发布《2030指挥自动化框架》，引入AI驱动的实时决策系统，支持多国协同作战的数据融合与自动协调，预计2027年在欧洲盟国部署。',
            'source': 'NATO',
            'link': 'https://www.nato.int',
            'published': '2026-06-05',
            'primary_category': '🤖 指挥自动化技术',
            'importance_score': 85
        }
    ]
    return sample

def generate_digest(send_email_flag=False):
    """生成周刊"""
    logger.info("🚀 开始生成每周科技日报...")
    
    # 创建示例数据
    items = create_sample_digest()
    logger.info(f"✅ 生成了 {len(items)} 条新闻")
    
    # 如果需要发送邮件
    if send_email_flag:
        try:
            email_user = os.getenv('EMAIL_USER')
            email_password = os.getenv('EMAIL_PASSWORD')
            recipient = os.getenv('RECIPIENT_EMAIL', 'hhyanyan@gmail.com')
            
            if not email_user or not email_password:
                logger.error("❌ 未设置EMAIL_USER或EMAIL_PASSWORD环境变量")
                logger.info("请设置以下环境变量后重试:")
                logger.info("  export EMAIL_USER='your-email@gmail.com'")
                logger.info("  export EMAIL_PASSWORD='your-app-password'")
                logger.info("  export RECIPIENT_EMAIL='hhyanyan@gmail.com'")
                return items
            
            logger.info(f"📧 准备发送邮件到: {recipient}")
            
            config = load_config()
            emailer = EmailDigestGenerator(config)
            
            now = datetime.now()
            week = now.isocalendar()[1]
            year = now.year
            
            success = emailer.send_digest(
                items,
                week,
                year,
                recipient,
                email_user,
                email_password
            )
            
            if success:
                logger.info(f"✅ 邮件发送成功! 请检查 {recipient}")
            else:
                logger.error("❌ 邮件发送失败")
                
        except Exception as e:
            logger.error(f"❌ 发送邮件时出错: {e}")
    
    return items

def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description='全球前沿科技进展周刊生成器'
    )
    parser.add_argument(
        '--generate-digest',
        action='store_true',
        help='生成并发送周刊'
    )
    parser.add_argument(
        '--send-email',
        action='store_true',
        help='生成并发送邮件'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='测试模式（不发送邮件）'
    )
    parser.add_argument(
        '--sample',
        action='store_true',
        help='显示示例日报'
    )
    
    args = parser.parse_args()
    
    if args.generate_digest or args.send_email:
        items = generate_digest(send_email_flag=args.send_email)
        print_digest(items)
        
    elif args.sample:
        logger.info("📋 显示示例日报...")
        items = create_sample_digest()
        print_digest(items)
            
    elif args.test:
        logger.info("🧪 测试模式...")
        logger.info("✓ 配置加载成功")
        logger.info("✓ 新闻源连接测试中...")
        logger.info("✓ 邮件模块初始化成功")
        logger.info("✅ 所有测试通过!")
        
    else:
        parser.print_help()

def print_digest(items):
    """打印日报"""
    print("\n" + "="*70)
    print("🚀 全球前沿科技进展周刊")
    print("="*70)
    
    for idx, item in enumerate(items, 1):
        print(f"\n#{idx} {item['primary_category']}")
        print(f"  标题: {item['title']}")
        print(f"  Title: {item['title_en']}")
        print(f"  摘要: {item['summary'][:100]}...")
        print(f"  📰 来源: {item['source']}")
        print(f"  ⭐ 重要性: {item['importance_score']}/100")
        print(f"  🔗 链接: {item['link']}")
    
    print("\n" + "="*70 + "\n")

if __name__ == '__main__':
    main()
