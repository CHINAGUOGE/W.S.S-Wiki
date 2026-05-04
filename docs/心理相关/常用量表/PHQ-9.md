# 患者健康问卷-9（Patient Health Questionnaire-9，PHQ-9）

!!! danger "重要声明"
本量表仅用于教育与自我筛查，**不构成临床诊断**。若分数较高，或第 9 题涉及“不如死掉/伤害自己”的想法出现阳性反应，请尽快联系精神科或临床心理专业人员。

!!! warning "危机求助资源"
**若您正在经历强烈绝望、自伤冲动或自杀想法，请立即寻求线下帮助：**

&#x20;   - \*\*全国24小时心理援助热线\*\*：400-161-9995 / 010-82951332
    - \*\*北京心理危机研究与干预中心\*\*：010-82951332
    - \*\*上海心理援助热线\*\*：021-962525 / 021-12320-5
    - \*\*广州心理危机干预中心\*\*：020-81899120
    - \*\*深圳心理危机干预热线\*\*：0755-25629459
    - \*\*紧急情况请拨打 120，或直接前往最近的医院急诊科\*\*

## 概述

**PHQ-9** 是目前国际上最常用的抑郁自评工具之一，用于评估 **过去两周** 内的抑郁症状频率与严重程度。它既可作为初步筛查工具，也常用于治疗过程中的症状追踪。

PHQ-9 共 9 题，每题按 `0-3` 分计分，总分范围 `0-27`。根据 `PHQ and GAD-7 Instructions`，PHQ 家族量表（包括 PHQ-9、GAD-7）已处于 **public domain**，可用于复制、翻译、展示与分发。

## 评分说明

!!! tip "使用说明"

&#x20;   - 请根据 \*\*过去两周\*\* 的实际体验作答
    - 每题按 `0-3` 分评分：
        - `0 = 完全没有`
        - `1 = 几天`
        - `2 = 一半以上天数`
        - `3 = 几乎天天`
    - 总分 `0-27`
    - 常见分界：`5 / 10 / 15 / 20`
    - \*\*第 9 题不论总分高低，只要大于 0 都值得认真对待\*\*

## 在线评估

<div class="guoge-scale-wrapper" style="all: initial; display: block; font-family: sans-serif; max-width: 700px; margin: 20px auto; border: 1px solid #e0e0e0; border-radius: 16px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
    <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 30px; color: white;">
        <h2 style="margin: 0; font-size: 24px;">病人健康问卷 (PHQ-9)</h2>
        <p style="font-size: 14px; opacity: 0.9; margin-top: 10px;">在过去的两周里，你有多大程度受到以下问题的困扰？</p>
    </div>
    <div id="phq-content" style="padding: 20px; background: #fdfdfd;"></div>
    <div style="padding: 30px; text-align: center; background: #f8f9fa;">
        <button onclick="calculatePHQ()" style="background: #00c6ff; color: white; border: none; padding: 15px 50px; border-radius: 30px; font-size: 18px; font-weight: bold; cursor: pointer;">提交评估</button>
    </div>
    <div id="phq-result" style="display: none; padding: 30px; background: white; border-top: 2px solid #00f2fe;">
        <div style="text-align: center;">
            <div style="font-size: 16px; color: #666;">评估总分</div>
            <div id="phq-score-val" style="font-size: 64px; font-weight: bold; color: #00c6ff; margin: 10px 0;">0</div>
            <div id="phq-desc-text" style="font-size: 20px; font-weight: bold; color: #333;"></div>
            <div style="text-align: left; background: #f0f2f5; padding: 15px; border-radius: 8px; font-size: 13px; color: #555; margin-top: 15px;">
                <strong>参考标准：</strong><br>
                0-4分：没有抑郁；5-9分：轻度；10-14分：中度；15-19分：中重度；20-27分：重度。
            </div>
        </div>
    </div>
</div>

<script>
(function() {
    const qs = [
        "做事提不起劲，或没有乐趣", "感到沉沦、抑郁或绝望", "入睡困难、睡得不稳或睡得太多",
        "感到疲倦或没有活力", "胃口不好或吃得太多", "觉得自己很糟，或觉得自己很失败，让自己或家人失望",
        "对事物难以集中注意力，例如看报纸或看电视", "动作或说话速度缓慢到别人都能察觉？或相反地变得烦躁不安，动来动去",
        "有不如死掉或想伤害自己的念头"
    ];
    const container = document.getElementById('phq-content');
    qs.forEach((q, i) => {
        let h = `<div style="margin-bottom: 25px;"><p style="font-weight: bold; color: #333;">${i+1}. ${q}</p><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">`;
        ["完全没有", "有几天", "一半以上", "几乎天天"].forEach((o, v) => {
            h += `<label style="cursor: pointer;"><input type="radio" name="phq${i}" value="${v}" style="display:none;" onchange="upPHQ(this)"><div class="phq-btn" style="padding: 12px; border: 1px solid #ddd; border-radius: 8px; text-align: center; font-size: 14px;">${o}</div></label>`;
        });
        container.innerHTML += h + `</div></div>`;
    });
})();

function upPHQ(i) {
    i.closest('div').querySelectorAll('.phq-btn').forEach(e => { e.style.background = 'white'; e.style.color = '#555'; });
    i.nextElementSibling.style.background = '#00c6ff';
    i.nextElementSibling.style.color = 'white';
}

function calculatePHQ() {
    const ins = document.querySelectorAll('input[name^="phq"]:checked');
    if(ins.length < 9) { alert("请完成所有题目！"); return; }
    let s = 0; ins.forEach(i => s += parseInt(i.value));
    document.getElementById('phq-score-val').innerText = s;
    const d = document.getElementById('phq-desc-text');
    if(s <= 4) d.innerText = "无抑郁症状";
    else if(s <= 9) d.innerText = "轻度抑郁";
    else if(s <= 14) d.innerText = "中度抑郁";
    else if(s <= 19) d.innerText = "中重度抑郁";
    else d.innerText = "重度抑郁";
    document.getElementById('phq-result').style.display = 'block';
}
</script>

> 本文部分内容搬运于[Multiple personality system Team CN · GitHub](https://github.com/mps-team-cn) <br>
> Powered by Guoge AICA.

![Powered by Guoge AICA](https://api.51320721.xyz/i/2026/04/19/hdxuy4.png)
