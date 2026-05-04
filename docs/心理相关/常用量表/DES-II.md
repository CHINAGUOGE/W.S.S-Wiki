# 解离经验量表（Dissociative Experiences Scale‑II, DES‑II）

!!! danger "重要声明"
本量表仅用于教育与自我筛查，**不构成临床诊断**。若分数较高且伴随明显解离、失忆或人格/现实解体体验，请及时寻求精神科或临床心理专业评估。“部分量表项目可能因主动想象训练而偏高，不代表病理性解离。对于这种情况，应该结合自己日常状况考虑。补充：对于已经确认是多意识体体系（包括但不限于did，osdd等）的用户，该量表会有部分失真 （其中有部分问题就是您的日常体验），需结合自身实际情况进行多方面评估"
!!! infor "警告"
我们注意到最近有恶意者倒卖本wiki内的量表，在此声明，本wiki所有量表全部均为免费使用。若有需要付费购买的情况，说明你遇到了骗子和倒卖分子。你可以采取包括退款等一系列的合法范围内的任何手段维权，同时，本wiki制作组也保留追究对方责任的权利——wiki制作组

## 概述

**解离经验量表（DES‑II）** 由 Bernstein 与 Putnam 于 1986 年编制，是国际常用的解离体验筛查工具。它评估个体在日常生活中出现的三类体验：

* 记忆缺失（Amnesia）：对事件或行为出现片段性遗忘；
* 人格/现实解体（Depersonalization/Derealization, DP/DR）：感觉自己或外界不真实；
* 吸收沉浸（Absorption）：在想象或活动中深度投入。

!!! tip "使用说明"

&#x20;   - 每一道题用滑块选择 0–100%：表示在日常生活中出现该体验的时间比例。
    - 建议按直觉作答；尽量不要反复修改，以首次直觉为准。可在最后点击“计算分数”。

!!! info "分数解释（参考 NovoPsych, 2024；仅作筛查）"

&#x20;   0–11 低 · 12–19 轻度 · 20–29 中度 · 30–45 高 · ≥46（可能提示显著解离倾向）。

    注：分界值用于筛查与研究，部分研究采用不同阈值设定（例如 Carlson \& Putnam, 1993；Ross, 2007）。任何分数均需结合主观痛苦与功能受损综合判断，\*\*不直接等同临床诊断\*\*。\[^carlson1993] \[^ross2007]

!!! note "子量表与算法说明（依据通用做法 / NovoPsych 公示资料）"

&#x20;   - 总分：28 题取平均（0–100）
    - 子量表（各 6 题，均为平均分）：
        - 记忆缺失（Amnesia）：3、4、5、8、25、26
        - 人格/现实解体（DP/DR）：7、11、12、13、27、28
        - 吸收沉浸（Absorption）：2、14、15、17、18、20
    - 注：分数仅作筛查用途，解释需结合情境、痛苦程度与功能受损。

## 在线测试

<div class="guoge-scale-wrapper" style="all: initial; display: block; font-family: sans-serif; max-width: 750px; margin: 20px auto; border: 1px solid #e0e0e0; border-radius: 16px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
    <div style="background: #2d3436; padding: 30px; color: white;">
        <h2 style="margin: 0; font-size: 24px;">解离体验量表 (DES-II)</h2>
        <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">描述这些体验在您生活中发生的频率（0%代表从不，100%代表总是）。</p>
    </div>
    <div id="des-content" style="padding: 20px; max-height: 600px; overflow-y: auto; background: #fdfdfd;"></div>
    <div style="padding: 30px; text-align: center; background: #f8f9fa;">
        <button onclick="calculateDES()" style="background: #2d3436; color: white; border: none; padding: 15px 50px; border-radius: 30px; font-size: 18px; font-weight: bold; cursor: pointer;">计算平均分</button>
    </div>
    <div id="des-result" style="display: none; padding: 30px; background: white; border-top: 2px solid #2d3436;">
        <div style="text-align: center;">
            <div style="font-size: 16px; color: #666;">平均得分 (0-100)</div>
            <div id="des-score-val" style="font-size: 64px; font-weight: bold; color: #2d3436; margin: 10px 0;">0</div>
            <div id="des-desc-text" style="font-size: 18px; color: #d35400; font-weight: bold;"></div>
            <div style="text-align: left; background: #f0f2f5; padding: 15px; border-radius: 8px; font-size: 13px; color: #555; margin-top: 15px;">
                注：一般认为平均分超过 30 分提示存在病理性的解离体验。
            </div>
        </div>
    </div>
</div>

<script>
(function() {
    const qDes = [
        "开车或搭车时，突然发现不记得刚才路过的风景或过程", "听别人说话时，突然发现自己完全没听进去刚才的话",
        "发现自己身处某地，却不知道是怎么去的", "发现自己穿着不记得穿上的衣服", "发现自己拥有一些新东西，却不记得买过",
        "被陌生人认出并叫出名字，且他们坚称以前见过你", "感到自己站在身体旁边看着自己在做事", "别人说你做过某些事，你却完全不记得",
        "不确定某些记忆是真实发生的还是梦境", "在镜中看到自己时，感觉不认识镜子里的人", "感到周围的人、物或世界不真实",
        "感到自己的身体不属于自己", "记忆中某些重要的生活事件突然变得模糊或消失", "无法回忆起生活中某些重要时刻",
        "发现自己能够做一些平时不会做的技能或事情", "在不同的场合感觉自己像是完全不同的人", "在某些时刻感觉像是有两个自己在脑子里争吵",
        "感觉自己的身体里像是住着其他人", "能清楚听到脑子里有声音在说话或争吵", "突然发现自己盯着虚空发呆，意识不到时间流逝",
        "发现自己自言自语，且停不下来", "在不同情况下发现自己的性格发生了剧烈变化", "有时感到疼痛却不觉得自己痛",
        "有时感觉自己像是木头人一样动不了", "有时会写下或画下一些不记得自己创作过的东西", "发现自己不记得曾去过某些地方的记忆",
        "发现自己能够表现得像个孩子一样", "感觉自己活在白日梦中无法自拔"
    ];
    const container = document.getElementById('des-content');
    qDes.forEach((q, i) => {
        let h = `<div style="margin-bottom: 25px;"><p style="font-weight: bold; color: #333;">${i+1}. ${q}</p><div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 5px;">`;
        for(let v=0; v<=100; v+=10) {
            h += `<label style="cursor: pointer;"><input type="radio" name="des${i}" value="${v}" style="display:none;" onchange="upDES(this)"><div class="des-btn" style="padding: 8px 0; border: 1px solid #ddd; border-radius: 4px; text-align: center; font-size: 11px; background: white;">${v}%</div></label>`;
        }
        container.innerHTML += h + `</div></div>`;
    });
})();

function upDES(i) {
    i.closest('div').querySelectorAll('.des-btn').forEach(e => { e.style.background = 'white'; e.style.color = '#333'; });
    i.nextElementSibling.style.background = '#2d3436'; i.nextElementSibling.style.color = 'white';
}

function calculateDES() {
    const ins = document.querySelectorAll('input[name^="des"]:checked');
    if(ins.length < 28) { alert("请完成所有28道题目！"); return; }
    let sum = 0; ins.forEach(i => sum += parseInt(i.value));
    let avg = Math.round(sum / 28);
    document.getElementById('des-score-val').innerText = avg;
    const d = document.getElementById('des-desc-text');
    if(avg >= 30) d.innerText = "测评结果：得分较高，提示存在解离倾向";
    else d.innerText = "测评结果：分值在正常波动范围内";
    document.getElementById('des-result').style.display = 'block';
}
</script>

> 本文部分内容搬运于[Multiple personality system Team CN · GitHub](https://github.com/mps-team-cn) <br>
> Powered by Guoge AICA.

![Powered by Guoge AICA](https://api.51320721.xyz/i/2026/04/19/hdxuy4.png)
