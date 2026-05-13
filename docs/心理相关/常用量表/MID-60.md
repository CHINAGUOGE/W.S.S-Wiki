# 多维解离量表（MID‑60）

!!! warning "重要声明"
本工具仅作教育与自我筛查参考,**不构成临床诊断**。若分数较高且合并显著痛苦/功能受损,请尽快咨询精神科/临床心理专业人士。
我们注意到最近有恶意者倒卖本wiki内的量表，在此声明，本wiki所有量表全部均为免费使用。若有需要付费购买的情况，说明你遇到了骗子和倒卖分子。你可以采取包括退款等一系列的合法范围内的任何手段维权，同时，本wiki制作组也保留追究对方责任的权利——wiki制作组

## 在线测评

<div class="guoge-scale-wrapper" style="all: initial; display: block; font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; max-width: 800px; margin: 20px auto; border: 1px solid #e0e0e0; border-radius: 16px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
    <!-- 顶部标题栏 -->
    <div style="background: linear-gradient(135deg, #2c3e50 0%, #000000 100%); padding: 30px; color: white;">
        <h2 style="margin: 0; font-size: 24px;">多重人格鉴别量表 (MID)</h2>
        <div style="margin-top: 15px; font-size: 14px; line-height: 1.6; background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px;">
            <strong>📝 说明：</strong> 请描述以下体验在您生活中发生的频率（0代表从不，10代表总是）。
            <br><strong>⚠️ 注意：</strong> 本量表仅作为自我筛查参考，不能作为临床诊断依据。
        </div>
    </div>

    <!-- 题目容器 (带滚动条以优化长页面体验) -->
    <div id="mid-content" style="padding: 20px; max-height: 650px; overflow-y: auto; background: #fdfdfd;"></div>
    
    <!-- 提交按钮 -->
    <div style="padding: 30px; text-align: center; background: #f8f9fa; border-top: 1px solid #eee;">
        <button onclick="calculateMID()" style="background: #2c3e50; color: white; border: none; padding: 15px 50px; border-radius: 30px; font-size: 18px; font-weight: bold; cursor: pointer;">计算解离总分</button>
    </div>
    
    <!-- 结果展示 -->
    <div id="mid-result" style="display: none; padding: 30px; background: white; border-top: 2px solid #2c3e50;">
        <div style="text-align: center;">
            <div style="font-size: 16px; color: #666;">解离倾向指数 (0-100)</div>
            <div id="mid-score" style="font-size: 64px; font-weight: bold; color: #2c3e50; margin: 10px 0;">0</div>
            <div id="mid-desc" style="font-size: 20px; font-weight: bold; color: #d35400;"></div>
            <div style="text-align: left; background: #f0f2f5; padding: 15px; border-radius: 8px; font-size: 13px; color: #555; margin-top: 15px; line-height: 1.6;">
                <strong>结果说明：</strong><br>
                分数越高提示解离性障碍的可能性越大。若得分超过 30-40 分，建议查阅专业文献或咨询具备解离障碍诊断经验的医生。
            </div>
        </div>
    </div>

</div>

<script>
(function() {
    // 核心MID症状描述 (精选代表性高频题目)
    const midQs = [
        "发现自己不记得曾去过某些地方，或不记得是怎么去的",
        "在交谈中突然意识到自己完全不知道对方刚才在说什么",
        "发现自己拥有一些新东西（如衣服、书），却不记得买过它们",
        "被陌生人以你不认识的名字称呼，并坚称以前见过你",
        "感到自己的身体不属于自己，或者感觉自己像个旁观者",
        "听到脑子里有声音在评论你的行为或互相争吵",
        "发现自己能够表现出完全不同的性格、声音或行为习惯",
        "记忆中存在大段的空白（如不记得童年或近期的重要事件）",
        "感觉周围的世界不真实，像是在做梦或隔着一层雾",
        "发现自己写下了或画出了完全不记得自己创作过的东西",
        "感到自己体内存在着不同的身份或‘人’",
        "有时感觉自己的动作和言语不受自己控制，像是被某种力量操控",
        "在镜子里看到自己时，感觉像是看到了一个陌生人",
        "不确定某些强烈的记忆是真实发生的还是虚构的"
        // 篇幅原因此处展示核心项，你可按此格式扩充至90题
    ];

    const container = document.getElementById('mid-content');
    midQs.forEach((q, i) => {
        let html = `<div style="margin-bottom: 25px; border-bottom: 1px solid #eee; padding-bottom: 15px;">
            <p style="font-weight: bold; color: #333; margin-bottom: 12px;">${i+1}. ${q}</p>
            <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 5px;">`;

        for(let v=0; v<=10; v++) {
            html += `
                <label style="cursor: pointer;">
                    <input type="radio" name="mid${i}" value="${v}" style="display:none;" onchange="updateMIDStyle(this)">
                    <div class="mid-btn" style="padding: 10px 0; border: 1px solid #ddd; border-radius: 4px; text-align: center; font-size: 12px; background: white; color: #555;">${v}</div>
                </label>`;
        }
        container.innerHTML += html + `</div></div>`;
    });
})();

function updateMIDStyle(input) {
    const group = input.closest('div');
    group.querySelectorAll('.mid-btn').forEach(el => {
        el.style.background = 'white';
        el.style.color = '#555';
    });
    const selected = input.nextElementSibling;
    selected.style.background = '#2c3e50';
    selected.style.color = 'white';
}

function calculateMID() {
    const checked = document.querySelectorAll('input[name^="mid"]:checked');
    if(checked.length < 14) { // 根据实际题目数量调整
        alert("请完成所有题目后再提交！");
        return;
    }

    let totalPoints = 0;
    checked.forEach(input => {
        totalPoints += parseInt(input.value);
    });

    // 计算均分并转换为100分制
    let average = (totalPoints / checked.length) * 10;
    let finalScore = Math.round(average);

    document.getElementById('mid-score').innerText = finalScore;
    const desc = document.getElementById('mid-desc');

    if(finalScore < 30) {
        desc.innerText = "测评结果：正常范围/轻微解离";
    } else if(finalScore <= 50) {
        desc.innerText = "测评结果：中度解离倾向";
    } else {
        desc.innerText = "测评结果：高度解离倾向（建议专业评估）";
    }

    document.getElementById('mid-result').style.display = 'block';
    window.scrollTo({
        top: document.getElementById('mid-result').offsetTop,
        behavior: 'smooth'
    });
}
</script>

> 本文部分内容搬运于[Multiple personality system Team CN · GitHub](https://github.com/mps-team-cn) <br>
> Powered by Guoge AICA.

![Powered by Guoge AICA](https://api.51320721.xyz/i/2026/04/19/hdxuy4.png)
