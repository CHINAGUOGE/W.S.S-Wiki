# 焦虑自评量表（Self-Rating Anxiety Scale, SAS）

!!! danger "重要声明"
本量表仅用于教育与自我筛查，**不构成临床诊断**。若分数较高且伴随明显焦虑症状，请及时寻求精神科或临床心理专业评估。本量表不能替代专业的临床诊断。

!!! warning "危机求助资源"
**若您正在经历严重焦虑、惊恐发作或其他急性心理危机，请立即寻求帮助：**

&#x20;   - \*\*全国24小时心理援助热线\*\*：400-161-9995 / 010-82951332
    - \*\*北京心理危机研究与干预中心\*\*：010-82951332
    - \*\*上海心理援助热线\*\*：021-962525 / 021-12320-5
    - \*\*广州心理危机干预中心\*\*：020-81899120
    - \*\*深圳心理危机干预热线\*\*：0755-25629459
    - \*\*紧急情况请拨打急救电话 120 或直接前往最近的医院急诊科\*\*

    您的健康很重要，专业帮助随时可得。

## 概述

**焦虑自评量表（SAS）** 由华裔心理学家 William W. K. Zung 于 1971 年编制，是目前临床上广泛使用的焦虑症状评估工具之一。量表包含 20 个项目，评估个体在过去一周内的焦虑症状体验，涵盖心理焦虑和躯体焦虑两大维度。

量表采用四级评分系统（1-4分），通过粗分和标准分（粗分×1.25）来评估焦虑程度，适用于焦虑症状的初步筛查、治疗效果监测和症状变化追踪。

## 评分说明

!!! tip "使用说明"

&#x20;   - 每题采用 \*\*1-4 分\*\* 四级评分：
        - \*\*1 = 没有或很少时间\*\*
        - \*\*2 = 小部分时间\*\*
        - \*\*3 = 相当多时间\*\*
        - \*\*4 = 绝大部分或全部时间\*\*
    - 请根据 \*\*过去一周（包括今天）\*\* 的实际体验作答
    - 建议按直觉作答，尽量不要反复修改
    - 完成所有题目后，系统将自动计算粗分和标准分

## 在线评估

<div class="guoge-scale-wrapper" style="all: initial; display: block; font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; max-width: 700px; margin: 20px auto; border: 1px solid #e0e0e0; border-radius: 16px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
    <!-- 顶部标题栏 -->
    <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 30px; color: white;">
        <h2 style="margin: 0; font-size: 24px;">自评焦虑量表 (SAS)</h2>
        <div style="margin-top: 15px; font-size: 14px; line-height: 1.6; background: rgba(255,255,255,0.2); padding: 15px; border-radius: 8px;">
            <strong>📝 说明：</strong> 请根据您最近一周的实际感受进行选择。
            <br><strong>⚠️ 注意：</strong> 最终分数为“标准分”（原始总分 × 1.25）。
        </div>
    </div>

    <!-- 题目容器 -->
    <div id="sas-full-content" style="padding: 20px; background: #fdfdfd;"></div>
    
    <!-- 提交按钮 -->
    <div style="padding: 30px; text-align: center; background: #f8f9fa;">
        <button onclick="calculateSASFull()" style="background: #f5576c; color: white; border: none; padding: 15px 50px; border-radius: 30px; font-size: 18px; font-weight: bold; cursor: pointer; transition: transform 0.2s;">查看评估报告</button>
    </div>
    
    <!-- 结果展示 -->
    <div id="sas-full-result" style="display: none; padding: 30px; background: white; border-top: 2px solid #f5576c;">
        <div style="text-align: center;">
            <div style="font-size: 16px; color: #666;">标准分 (Index Score)</div>
            <div id="sas-full-score" style="font-size: 64px; font-weight: bold; color: #f5576c; margin: 10px 0;">0</div>
            <div id="sas-full-desc" style="font-size: 20px; font-weight: bold; color: #333;"></div>
            <div style="text-align: left; background: #f0f2f5; padding: 15px; border-radius: 8px; font-size: 13px; color: #555; margin-top: 15px; line-height: 1.5;">
                <strong>参考标准：</strong><br>
                50分以下：正常；50-59分：轻度焦虑；60-69分：中度焦虑；70分以上：重度焦虑。
            </div>
        </div>
    </div>

</div>

<script>
(function() {
    // 完整20题，r: true 代表反向计分题
    const sasQuestions = [
        {t:"我觉得比平常容易紧张和着急", r:false},
        {t:"我无缘无故地感到害怕", r:false},
        {t:"我容易心里烦乱或觉得惊恐", r:false},
        {t:"我觉得我可能将要发疯", r:false},
        {t:"我觉得一切都很好，也不会发生什么不幸", r:true},
        {t:"我手脚发抖打颤", r:false},
        {t:"我为头痛、背痛、颈痛而烦恼", r:false},
        {t:"我觉得容易衰弱和疲乏", r:false},
        {t:"我觉得心平气和，并且容易安静坐着", r:true},
        {t:"我觉得心跳得很快", r:false},
        {t:"我因为阵阵头晕而苦恼", r:false},
        {t:"我有晕倒发作或觉得要晕倒似的", r:false},
        {t:"我呼气吸气都感到很容易", r:true},
        {t:"我手脚麻木和刺痛", r:false},
        {t:"我因为胃痛和消化不良而苦恼", r:false},
        {t:"我常常要小便", r:false},
        {t:"我的手常常是温和而干燥的", r:true},
        {t:"我脸红发热", r:false},
        {t:"我容易入睡，并且一夜睡得很好", r:true},
        {t:"我做噩梦", r:false}
    ];

    const opts = ["没有或很少时间", "小部分时间", "相当多时间", "绝大部分时间"];
    const container = document.getElementById('sas-full-content');

    sasQuestions.forEach((q, i) => {
        let html = `<div style="margin-bottom: 25px;">
            <p style="font-weight: bold; color: #333; margin-bottom: 12px;">${i+1}. ${q.t}</p>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">`;

        opts.forEach((opt, v) => {
            // 原始分1-4，反向计分时：1变4, 2变3, 3变2, 4变1
            let score = q.r ? (4 - v) : (v + 1); 
            html += `
                <label style="cursor: pointer;">
                    <input type="radio" name="sas_f${i}" value="${score}" style="display:none;" onchange="updateSASFullStyle(this)">
                    <div class="sas-f-btn" style="padding: 12px; border: 1px solid #ddd; border-radius: 8px; text-align: center; font-size: 14px; background: white; color: #555; transition: all 0.2s;">${opt}</div>
                </label>`;
        });
        container.innerHTML += html + `</div></div>`;
    });
})();

function updateSASFullStyle(input) {
    const group = input.closest('div');
    group.querySelectorAll('.sas-f-btn').forEach(el => {
        el.style.background = 'white';
        el.style.color = '#555';
        el.style.borderColor = '#ddd';
    });
    const selected = input.nextElementSibling;
    selected.style.background = '#f5576c';
    selected.style.color = 'white';
    selected.style.borderColor = '#f5576c';
}

function calculateSASFull() {
    const checked = document.querySelectorAll('input[name^="sas_f"]:checked');
    if(checked.length < 20) {
        alert("请完成所有 20 道题目后再提交！");
        return;
    }

    let rawScore = 0;
    checked.forEach(input => {
        rawScore += parseInt(input.value);
    });

    // 标准分 = 原始总分 * 1.25，取整数部分
    let standardScore = Math.floor(rawScore * 1.25);

    document.getElementById('sas-full-score').innerText = standardScore;
    const desc = document.getElementById('sas-full-desc');

    if(standardScore < 50) {
        desc.innerText = "测评结果：正常范围";
    } else if(standardScore <= 59) {
        desc.innerText = "测评结果：轻度焦虑";
    } else if(standardScore <= 69) {
        desc.innerText = "测评结果：中度焦虑";
    } else {
        desc.innerText = "测评结果：重度焦虑";
    }

    document.getElementById('sas-full-result').style.display = 'block';

    // 平滑滚动到结果区域
    window.scrollTo({
        top: document.getElementById('sas-full-result').offsetTop - 20,
        behavior: 'smooth'
    });
}
</script>

> 本文部分内容搬运于[Multiple personality system Team CN · GitHub](https://github.com/mps-team-cn) <br>
> Powered by Guoge AICA.

![Powered by Guoge AICA](https://api.51320721.xyz/i/2026/04/19/hdxuy4.png)
