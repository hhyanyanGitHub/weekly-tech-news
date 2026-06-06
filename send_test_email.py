#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试脚本：生成军事应用技术前沿周刊并发送邮件
"""

import os
import sys
from datetime import datetime

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from emailer import EmailDigestGenerator

def create_military_tech_digest():
    """创建军事应用技术前沿日报"""
    
    items = [
        {
            'rank': 1,
            'title': 'DARPA发布AI驱动型指挥自动化系统，支持多域实时协同决策',
            'title_en': 'DARPA Releases AI-Powered Command Automation System for Multi-Domain Real-Time Collaborative Decision-Making',
            'category': '🤖 指挥自动化技术',
            'summary': '美国国防高级研究计划局(DARPA)宣布完成"马格尼特"(Magnit)项目的第二阶段测试。该系统采用图神经网络和强化学习算法，实现多源数据实时融合，支持跨域单位的自主决策与协同指挥。测试中成功模拟了涉及陆海空天网五大域的联合作战场景，系统决策延迟低于200毫秒，战术单位响应时间提升45%。',
            'source': 'DARPA',
            'link': 'https://www.darpa.mil/news-events/news-releases',
            'published': '2026-06-05',
            'importance_score': 96
        },
        {
            'rank': 2,
            'title': 'NATO网络防御演习揭示关键基础设施防护的AI应用突破',
            'title_en': 'NATO Cyber Defense Exercises Reveal AI Application Breakthrough in Critical Infrastructure Protection',
            'category': '🔐 网络与信息技术',
            'summary': 'NATO网络防御中心在最新一轮"相互防御演习"(Locked Shields 2026)中展示了基于深度强化学习的网络防御系统。该系统能够自动检测和应对零日漏洞攻击，防护成功率达87%，比传统规则库方法提升23个百分点。演习中还首次验证了量子密钥分发(QKD)在多国指挥系统中的可行性。',
            'source': 'NATO Cyber Operations',
            'link': 'https://www.nato.int/cps/en/natohq/topics_175175.htm',
            'published': '2026-06-04',
            'importance_score': 93
        },
        {
            'rank': 3,
            'title': '美军宣布新一代SAR卫星成功进行目标识别测试，分辨率达15厘米',
            'title_en': 'US Military Announces New Generation SAR Satellite Successfully Completes Target Recognition Test with 15cm Resolution',
            'category': '🛰️ 摄影测量与遥感技术',
            'summary': '美国空军与DARPA联合宣布，新型合成孔径雷达(SAR)卫星"哨兵"(Sentinel)的在轨测试取得重大突破。该卫星采用创新的多基线干涉SAR技术，在移动目标条件下的地理定位精度达±3米，目标分类准确率超过94%。系统已能实时生成三维地形模型，并集成AI视频分析模块，支持战场动态监视评估。',
            'source': 'DARPA',
            'link': 'https://www.darpa.mil/news-events/news-releases',
            'published': '2026-06-03',
            'importance_score': 91
        },
        {
            'rank': 4,
            'title': 'CISA发布指挥控制系统网络防护新指南，应对国家级APT威胁',
            'title_en': 'CISA Releases New Cybersecurity Guidelines for Command and Control Systems Against Nation-State APT Threats',
            'category': '🔐 网络与信息技术',
            'summary': '美国网络安全和基础设施安全局(CISA)发布《军事信息系统零信任架构实施指南》。新指南针对国家级APT组织的高级持久性威胁，提出了基于微分段和身份验证的分层防御模型。建议所有关键指挥系统采用"永不信任，始终验证"原则，并部署AI异常检测系统。该指南已成为美军主要联合作战司令部(COCOM)的强制执行标准。',
            'source': 'CISA',
            'link': 'https://www.cisa.gov/news-events/alerts',
            'published': '2026-06-02',
            'importance_score': 88
        },
        {
            'rank': 5,
            'title': '美军成功验证无人机集群自主协同编队，单次任务覆盖12000平方公里',
            'title_en': 'US Military Successfully Validates Autonomous Coordination of Drone Swarms, Single Mission Coverage Reaches 12,000 Square Kilometers',
            'category': '🤖 指挥自动化技术',
            'summary': '美国空军研究实验室(AFRL)发布了无人机集群协同作战的最新测试成果。128架小型无人机在无人工干预条件下完成自主编队、目标搜索和同步攻击任务。系统采用分布式决策算法，即使在GPS信号受阻50%的环境中仍能维持队形，任务完成率达98.5%。该技术为未来规模化蜂群作战提供了重要基础。',
            'source': 'US DoD',
            'link': 'https://www.defense.gov/News/',
            'published': '2026-06-01',
            'importance_score': 89
        },
        {
            'rank': 6,
            'title': '欧盟发布后量子密码标准，防护500亿美元军事通信系统',
            'title_en': 'EU Releases Post-Quantum Cryptography Standards to Protect $50 Billion Military Communication Systems',
            'category': '🔐 网络与信息技术',
            'summary': '欧洲网络安全局(ENISA)和欧盟防御基金联合发布《后量子密码标准化路线图》。该标准基于格子密码学(lattice-based)和多元多项式(multivariate polynomial)算法，已通过NIST认证。欧盟计划在2027年前将其部署到所有北约成员国的指挥通信系统，预计保护资产超过500亿美元，防护期限延伸至本世纪末。',
            'source': 'NATO',
            'link': 'https://www.nato.int/cps/en/natohq/news.htm',
            'published': '2026-05-31',
            'importance_score': 87
        },
        {
            'rank': 7,
            'title': '军用卫星遥感图像AI识别系统准确率突破95%，损伤评估自动化成熟',
            'title_en': 'Military Satellite Remote Sensing AI Recognition System Achieves 95% Accuracy; Damage Assessment Automation Matures',
            'category': '🛰️ 摄影测量与遥感技术',
            'summary': '美国战争学院的空间战研究中心发表最新研究显示，基于卷积神经网络(CNN)的遥感图像识别系统在军事设施、车辆和战场结构的识别上达到95.3%准确率。该系统能在30秒内自动评估战争破坏程度，为战场损伤评估(BDA)和战损评估(CAP)提供决策支持。已被美国国防智能局纳入每日战场评估流程。',
            'source': 'Military & Aerospace',
            'link': 'https://www.militaryaerospace.com',
            'published': '2026-05-30',
            'importance_score': 85
        },
        {
            'rank': 8,
            'title': '中美俄各国推进军事AI伦理框架，自主武器国际规则成焦点',
            'title_en': 'US, China, Russia Advance Military AI Ethics Framework; Autonomous Weapons International Rules Become Focus',
            'category': '⚔️ 军事应用突破',
            'summary': '联合国不扩散委员会召开"致命自主武器系统(LAWS)"专题研讨会。美国、中国和俄罗斯分别提交了各自的军事AI伦理指导框架。虽然三方在自主决策权限、目标确认机制等方面仍存分歧，但均同意自主武器系统的上层决策权必须由人类保留。预计2027年将形成国际共识文件。',
            'source': 'Defense News',
            'link': 'https://www.defensenews.com/rss/',
            'published': '2026-05-29',
            'importance_score': 82
        },
        {
            'rank': 9,
            'title': '5G军事应用验证完成，超低延迟通信支持边缘AI决策',
            'title_en': '5G Military Application Validation Completed; Ultra-Low Latency Communication Supports Edge AI Decision-Making',
            'category': '🤖 指挥自动化技术',
            'summary': '美国空军与诺基亚联合完成了5G在作战指挥中的验证测试。关键成果包括：平均时延降至3毫秒(相比4G的50毫秒)，支持500余个并发连接的指挥终端，边缘计算节点能在150毫秒内完成AI决策并下发指令。该系统已被美国印太司令部纳入"2026年联合作战能力提升计划"。',
            'source': 'Defense News',
            'link': 'https://www.defensenews.com/rss/',
            'published': '2026-05-28',
            'importance_score': 84
        },
        {
            'rank': 10,
            'title': '美国陆军部署首支AI增强步兵班，战术效能提升38%',
            'title_en': 'US Army Deploys First AI-Enhanced Infantry Squad; Tactical Effectiveness Increases by 38%',
            'category': '⚔️ 军事应用突破',
            'summary': '美国陆军战争学院宣布，第1骑兵师第2营第A连成为首支配备"AI战术助手"(AITAC)系统的步兵班。该系统集成了态势感知、目标推荐、火力控制等功能，通过与班组士兵配备的平板终端连接。6个月试用期间，该班组的任务完成速度提升25%，误判率降低67%，综合战术效能评估提升38%。后续计划扩展到全师级。',
            'source': 'Army News Service',
            'link': 'https://www.army.mil/news/',
            'published': '2026-05-27',
            'importance_score': 83
        }
    ]
    
    return items

def send_test_email():
    """发送测试邮件"""
    
    print("\n" + "="*70)
    print("🚀 全球前沿科技进展周刊 - 军事应用技术版")
    print("="*70)
    print()
    
    # 生成日报
    items = create_military_tech_digest()
    
    # 显示日报内容
    for item in items:
        print(f"#{item['rank']} {item['category']}")
        print(f"  标题: {item['title']}")
        print(f"  Title: {item['title_en']}")
        print(f"  摘要: {item['summary'][:120]}...")
        print(f"  📰 来源: {item['source']}")
        print(f"  ⭐ 重要性: {item['importance_score']}/100")
        print(f"  🔗 链接: {item['link']}")
        print()
    
    print("="*70)
    print("\n正在尝试发送邮件...\n")
    
    # 尝试发送邮件
    try:
        email_user = os.getenv('EMAIL_USER')
        email_password = os.getenv('EMAIL_PASSWORD')
        recipient = os.getenv('RECIPIENT_EMAIL', 'hhyanyan@gmail.com')
        
        if not email_user or not email_password:
            print("❌ 未检测到邮箱凭证")
            print("\n您可以通过以下方式设置:")
            print("  export EMAIL_USER='hhyanyan@gmail.com'")
            print("  export EMAIL_PASSWORD='your-16-digit-app-password'")
            print("  export RECIPIENT_EMAIL='hhyanyan@gmail.com'")
            print("\n然后运行: python send_test_email.py")
            return False
        
        print(f"📧 正在发送到: {recipient}")
        print(f"📤 发件人: {email_user}")
        
        # 创建邮件生成器
        config = {
            'categories': {},
            'limits': {}
        }
        emailer = EmailDigestGenerator(config)
        
        # 发送邮件
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
            print(f"\n✅ 邮件发送成功！")
            print(f"📬 请检查 {recipient} 的收件箱（可能需要稍等几秒）")
            print(f"📝 如果没看到，请检查垃圾邮件/促销邮件文件夹")
            return True
        else:
            print("\n❌ 邮件发送失败")
            return False
            
    except Exception as e:
        print(f"\n❌ 出错: {e}")
        print("\n请确保:")
        print("  1. Gmail账户已启用两步验证")
        print("  2. 应用专用密码已正确生成和设置")
        print("  3. 密码没有多余的空格或特殊字符")
        return False

if __name__ == '__main__':
    send_test_email()
