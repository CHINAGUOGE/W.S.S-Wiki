# 广泛性焦虑量表-7（Generalized Anxiety Disorder-7，GAD-7）

!!! danger "重要声明"
    本量表仅用于教育与自我筛查，**不构成临床诊断**。高分提示焦虑症状值得进一步评估，但不能直接等同于广泛性焦虑障碍诊断。

!!! warning "危机求助资源"
    **若您正在经历持续惊恐、极端痛苦、无法保证自身安全或明显失眠恶化，请尽快联系线下专业帮助：**

    - **全国24小时心理援助热线**：400-161-9995 / 010-82951332
    - **北京心理危机研究与干预中心**：010-82951332
    - **上海心理援助热线**：021-962525 / 021-12320-5
    - **广州心理危机干预中心**：020-81899120
    - **深圳心理危机干预热线**：0755-25629459
    - **紧急情况请拨打 120，或直接前往最近的医院急诊科**

## 概述

**GAD-7** 是一个 7 题的焦虑筛查与严重度评估工具，用于评估 **过去两周** 的担忧、紧张、放松困难与烦躁程度。虽然它最初是为广泛性焦虑障碍开发的，但在临床中也常用来初步观察惊恐、社交焦虑与创伤相关焦虑线索。

GAD-7 每题按 `0-3` 分计分，总分范围 `0-21`。`PHQ and GAD-7 Instructions` 说明 PHQ 家族量表（含 GAD-7）处于 **public domain**，可复制、翻译、展示与分发。

## 评分说明

!!! tip "使用说明"

    - 请根据 **过去两周** 的实际体验作答
    - 每题按 `0-3` 分评分：
        - `0 = 完全没有`
        - `1 = 几天`
        - `2 = 一半以上天数`
        - `3 = 几乎天天`
    - 总分 `0-21`
    - 常见分界：`5 / 10 / 15`
    - **总分 ≥ 10** 常被视作值得进一步评估的阈值

## 在线测评

<div class="guoge-scale-wrapper" style="all: initial; display: block; font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; max-width: 700px; margin: 20px auto; border: 1px solid #e0e0e0; border-radius: 16px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
    <div style="background: linear-gradient(135deg, #f6d365 0%, #fda085 100%); padding: 30px; color: white;">
        <h2 style="margin: 0; font-size: 24px;">广泛性焦虑量表 (GAD-7)</h2>
        <div style="margin-top: 15px; font-size: 14px; line-height: 1.6; background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px;">
            <strong>📝 说明：</strong> 过去两周内，你有多大程度受到以下问题的困扰？
        </div>
    </div>
    <div id="gad7-content" style="padding: 20px; background: #fdfdfd;"></div>
    <div style="padding: 30px; text-align: center; background: #f8f9fa;">
        <button onclick="calculateGAD7()" style="background: #fda085; color: white; border: none; padding: 15px 50px; border-radius: 30px; font-size: 18px; font-weight: bold; cursor: pointer;">提交评估</button>
    </div>
    <div id="gad7-result" style="display: none; padding: 30px; background: white; border-top: 2px solid #fda085;">
        <div style="text-align: center;">
            <div style="font-size: 16px; color: #666;">评估得分</div>
            <div id="gad7-score" style="font-size: 64px; font-weight: bold; color: #fda085; margin: 10px 0;">0</div>
            <div id="gad7-desc" style="font-size: 20px; font-weight: bold; color: #333;"></div>
            <div style="text-align: left; background: #f0f2f5; padding: 15px; border-radius: 8px; font-size: 13px; color: #555; margin-top: 15px;">
                <strong>参考标准：</strong><br>
                0-4分：没有焦虑；5-9分：轻度焦虑；10-14分：中度焦虑；15-21分：重度焦虑。
            </div>
        </div>
    </div>
</div>

<script>
(function() {
    const questions = [
        "感到紧张、不安或烦躁", "不能停止或无法控制担心", "对各种各样的事都过分担心",
        "很难放松下来", "由于不安而无法静坐", "变得容易烦恼或急躁", "感到似乎有什么可怕的事会发生"
    ];
    const opts = ["完全没有", "有几天", "一半以上时间", "几乎天天"];
    const container = document.getElementById('gad7-content');
    questions.forEach((q, i) => {
        let html = `<div style="margin-bottom: 25px;"><p style="font-weight: bold; color: #333;">${i+1}. ${q}</p><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">`;
        opts.forEach((opt, v) => {
            html += `<label style="cursor: pointer;"><input type="radio" name="gad${i}" value="${v}" style="display:none;" onchange="updateGADStyle(this)"><div class="gad-btn" style="padding: 12px; border: 1px solid #ddd; border-radius: 8px; text-align: center; font-size: 14px; background: white;">${opt}</div></label>`;
        });
        container.innerHTML += html + `</div></div>`;
    });
})();

function updateGADStyle(input) {
    input.closest('div').querySelectorAll('.gad-btn').forEach(el => { el.style.background = 'white'; el.style.color = '#555'; });
    input.nextElementSibling.style.background = '#fda085';
    input.nextElementSibling.style.color = 'white';
}

function calculateGAD7() {
    const ins = document.querySelectorAll('input[name^="gad"]:checked');
    if(ins.length < 7) { alert("请完成所有题目！"); return; }
    let s = 0; ins.forEach(i => s += parseInt(i.value));
    document.getElementById('gad7-score').innerText = s;
    const d = document.getElementById('gad7-desc');
    if(s <= 4) d.innerText = "无焦虑症状";
    else if(s <= 9) d.innerText = "轻度焦虑";
    else if(s <= 14) d.innerText = "中度焦虑";
    else d.innerText = "重度焦虑";
    document.getElementById('gad7-result').style.display = 'block';
}
</script>

> 本文部分内容搬运于[Multiple personality system Team CN · GitHub](https://github.com/mps-team-cn) <br>
> Powered by Guoge AICA.

![Powered by Guoge AICA](https://api.51320721.xyz/i/2026/04/19/hdxuy4.png)
