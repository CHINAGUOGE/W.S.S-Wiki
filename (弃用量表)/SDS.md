# 抑郁自评量表（Self-Rating Depression Scale, SDS）

!!! danger "重要声明"
本量表仅用于教育与自我筛查，**不构成临床诊断**。若分数较高且伴随明显抑郁症状，请及时寻求精神科或临床心理专业评估。本量表不能替代专业的临床诊断。

!!! warning "危机求助资源"
**若您正在经历严重抑郁、自杀想法或其他急性心理危机，请立即寻求帮助：**

&#x20;   - \*\*全国24小时心理援助热线\*\*：400-161-9995 / 010-82951332
    - \*\*北京心理危机研究与干预中心\*\*：010-82951332
    - \*\*上海心理援助热线\*\*：021-962525 / 021-12320-5
    - \*\*广州心理危机干预中心\*\*：020-81899120
    - \*\*深圳心理危机干预热线\*\*：0755-25629459
    - \*\*紧急情况请拨打急救电话 120 或直接前往最近的医院急诊科\*\*

    您的生命很宝贵，专业帮助随时可得。


## 概述

**抑郁自评量表（SDS）** 由美国杜克大学医学院的 William W. K. Zung 于 1965 年编制，是目前国际上应用最广泛的抑郁症状自评工具之一。量表包含 20 个项目，评估个体在过去一周内的抑郁症状体验，涵盖情感、躯体和心理症状等多个维度。

量表采用四级评分系统（1-4分），通过粗分和标准分（粗分×1.25）来评估抑郁程度，适用于抑郁症状的初步筛查、治疗效果监测和症状变化追踪。

## 评分说明

!!! tip "使用说明"

&#x20;   - 每题采用 \*\*1-4 分\*\* 四级评分：
        - \*\*1 = 没有或很少时间\*\*（过去一周内，出现这类情况的日子不超过一天）
        - \*\*2 = 小部分时间\*\*（过去一周内，有1-2天有过这类情况）
        - \*\*3 = 相当多时间\*\*（过去一周内，3-4天有过这类情况）
        - \*\*4 = 绝大部分或全部时间\*\*（过去一周内，有5-7天有过这类情况）
    - 请根据 \*\*过去一周（包括今天）\*\* 的实际体验作答
    - 建议按直觉作答，尽量不要反复修改
    - 完成所有题目后，系统将自动计算粗分和标准分


## 在线评估

<div class="guoge-scale-wrapper" style="all: initial; display: block; font-family: sans-serif; max-width: 700px; margin: 20px auto; border: 1px solid #e0e0e0; border-radius: 16px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
    <div style="background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); padding: 30px; color: white;">
        <h2 style="margin: 0; font-size: 24px;">自评抑郁量表 (SDS)</h2>
        <div style="margin-top: 15px; font-size: 14px; line-height: 1.6; background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px;">
            <strong>📝 说明：</strong> 请根据您最近一周的实际感受进行选择。
            <br><strong>⚠️ 注意：</strong> 最终分数为标准分（原始分总和 × 1.25）。
        </div>
    </div>
    <div id="sds-content" style="padding: 20px; background: #fdfdfd;"></div>
    <div style="padding: 30px; text-align: center; background: #f8f9fa;">
        <button onclick="calculateSDS()" style="background: #2575fc; color: white; border: none; padding: 15px 50px; border-radius: 30px; font-size: 18px; font-weight: bold; cursor: pointer;">提交评估</button>
    </div>
    <div id="sds-result" style="display: none; padding: 30px; background: white; border-top: 2px solid #2575fc;">
        <div style="text-align: center;">
            <div style="font-size: 16px; color: #666;">标准分 (SDS Index)</div>
            <div id="sds-score-val" style="font-size: 64px; font-weight: bold; color: #2575fc; margin: 10px 0;">0</div>
            <div id="sds-desc-text" style="font-size: 20px; font-weight: bold; color: #333;"></div>
            <div style="text-align: left; background: #f0f2f5; padding: 15px; border-radius: 8px; font-size: 13px; color: #555; margin-top: 15px;">
                <strong>参考标准：</strong><br>
                53分以下：正常；53-62分：轻度抑郁；63-72分：中度抑郁；72分以上：重度抑郁。
            </div>
        </div>
    </div>
</div>

<script>
(function() {
    const questions = [
        {t:"我觉得像往常一样，心境忧郁、沮丧", r:false}, {t:"我觉得早晨好过些", r:true}, {t:"我要哭或想哭", r:false},
        {t:"我夜间睡眠不好", r:false}, {t:"我吃得跟平常一样多", r:true}, {t:"我愿意和异性接触", r:true},
        {t:"我感到体重在减轻", r:false}, {t:"我有便秘的苦恼", r:false}, {t:"我心跳得比平时快", r:false},
        {t:"我无缘无故地感到疲劳", r:false}, {t:"我的头脑跟平常一样清楚", r:true}, {t:"我觉得做任何事都很容易", r:true},
        {t:"我觉得坐立不安，难以静止", r:false}, {t:"我对未来抱有希望", r:true}, {t:"我比平常更容易激怒", r:false},
        {t:"我觉得做决定很容易", r:true}, {t:"我觉得自己是有用的人，有人需要我", r:true}, {t:"我的生活过得很有意思", r:true},
        {t:"我认为如果我死了，别人会生活得更好", r:false}, {t:"我仍旧喜爱我平时喜爱的东西", r:true}
    ];
    const opts = ["没有或很少", "有时有", "大部分时间有", "绝大部分时间"];
    const container = document.getElementById('sds-content');
    questions.forEach((q, i) => {
        let html = `<div style="margin-bottom: 25px;"><p style="font-weight: bold; color: #333;">${i+1}. ${q.t}</p><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">`;
        opts.forEach((opt, v) => {
            let score = q.r ? (4 - v) : (v + 1); 
            html += `<label style="cursor: pointer;"><input type="radio" name="sds${i}" value="${score}" style="display:none;" onchange="updateSDSStyle(this)"><div class="sds-btn" style="padding: 12px; border: 1px solid #ddd; border-radius: 8px; text-align: center; font-size: 14px;">${opt}</div></label>`;
        });
        container.innerHTML += html + `</div></div>`;
    });
})();

function updateSDSStyle(input) {
    input.closest('div').querySelectorAll('.sds-btn').forEach(el => { el.style.background = 'white'; el.style.color = '#555'; });
    input.nextElementSibling.style.background = '#2575fc';
    input.nextElementSibling.style.color = 'white';
}

function calculateSDS() {
    const ins = document.querySelectorAll('input[name^="sds"]:checked');
    if(ins.length < 20) { alert("请完成所有题目！"); return; }
    let raw = 0; ins.forEach(i => raw += parseInt(i.value));
    let standard = Math.floor(raw * 1.25);
    document.getElementById('sds-score-val').innerText = standard;
    const d = document.getElementById('sds-desc-text');
    if(standard < 53) d.innerText = "测评结果：正常";
    else if(standard <= 62) d.innerText = "测评结果：轻度抑郁";
    else if(standard <= 72) d.innerText = "测评结果：中度抑郁";
    else d.innerText = "测评结果：重度抑郁";
    document.getElementById('sds-result').style.display = 'block';
    window.scrollTo({ top: document.getElementById('sds-result').offsetTop, behavior: 'smooth' });
}
</script>

> 本文部分内容搬运于[Multiple personality system Team CN · GitHub](https://github.com/mps-team-cn) <br>
> Powered by Guoge AICA.

![Powered by Guoge AICA](https://api.51320721.xyz/i/2026/04/19/hdxuy4.png)
