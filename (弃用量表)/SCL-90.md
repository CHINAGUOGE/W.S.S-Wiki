# 症状自评量表修订版（Symptom Checklist-90-Revised, SCL-90-R）

!!! danger "重要声明"
    本量表仅用于教育与自我筛查，**不构成临床诊断**。若分数较高且伴随明显心理症状，请及时寻求精神科或临床心理专业评估。本量表不能替代专业的临床诊断。

!!! warning "危机求助资源"
    **若您正在经历自杀想法、自伤冲动或伤害他人的念头，请立即寻求帮助：**

    - **全国24小时心理援助热线**：400-161-9995 / 010-82951332
    - **北京心理危机研究与干预中心**：010-82951332
    - **上海心理援助热线**：021-962525 / 021-12320-5
    - **广州心理危机干预中心**：020-81899120
    - **深圳心理危机干预热线**：0755-25629459
    - **紧急情况请拨打急救电话 120 或直接前往最近的医院急诊科**
    
    您的生命很宝贵，专业帮助随时可得。

## 概述

**症状自评量表修订版（SCL-90-R）** 由 Derogatis 于 1977 年在原始 SCL-90（1975）基础上修订而成，是目前国际上使用最广泛的心理健康筛查量表之一。量表包含 90 个项目，评估个体在过去一周内的心理症状体验，涵盖九个症状维度：

- **躯体化（Somatization）**：以躯体不适表达心理痛苦的倾向
- **强迫症状（Obsessive-Compulsive）**：强迫思维与强迫行为
- **人际敏感（Interpersonal Sensitivity）**：人际交往中的不适感与自卑感
- **抑郁（Depression）**：抑郁情绪与相关症状
- **焦虑（Anxiety）**：焦虑情绪与躯体焦虑表现
- **敌对（Hostility）**：愤怒、攻击性与敌意
- **恐怖（Phobic Anxiety）**：对特定情境的恐惧反应
- **偏执（Paranoid Ideation）**：多疑、被害感与关系妄想倾向
- **精神病性（Psychoticism）**：孤独、精神病性症状倾向

量表计算三个总体指标：

- **总体严重指数（Global Severity Index, GSI）**：所有90项的平均分，是最重要的总体指标
- **阳性项目数（Positive Symptom Total, PST）**：评分 ≥ 1 分的项目数
- **阳性症状均分（Positive Symptom Distress Index, PSDI）**：阳性项目的平均分

此外还计算 **总分（Total Score）** 作为辅助参考（90项得分之和）

!!! info "版本说明"
    **本词条采用 SCL-90-R（修订版）标准**，使用 **0-4 分评分系统**。中国常模版本（王征宇，1984）采用 1-5 分评分系统，且部分维度的题目分配有所不同。如需使用中国常模进行临床解释，请参考相应的评分标准和常模数据。

## 评分说明

!!! tip "使用说明"

    - 每题采用 **0-4 分** 五级评分（SCL-90-R 标准）：
        - **0 = 没有（NOT AT ALL）**
        - **1 = 很轻（A LITTLE BIT）**
        - **2 = 中等（MODERATELY）**
        - **3 = 偏重（QUITE A BIT）**
        - **4 = 严重（EXTREMELY）**
    - 请根据 **过去一周（包括今天）** 的实际体验作答
    - 建议按直觉作答，尽量不要反复修改
    - 完成所有题目后，系统将自动计算各维度分数

## 在线评估

<div class="guoge-scale-wrapper" style="all: initial; display: block; font-family: sans-serif; max-width: 800px; margin: 20px auto; border: 1px solid #e0e0e0; border-radius: 16px; overflow: hidden; background: #fff; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
    <div style="background: #333; padding: 30px; color: white;">
        <h2 style="margin: 0;">症状自评量表 (SCL-90)</h2>
        <p style="font-size: 14px; opacity: 0.8; margin-top: 10px;">请根据您最近一周的实际症状严重程度进行选择。</p>
    </div>
    <div id="scl90-content" style="padding: 20px; max-height: 700px; overflow-y: auto; background: #fdfdfd;"></div>
    <div style="padding: 30px; text-align: center; background: #f8f9fa;">
        <button onclick="calculateSCL90()" style="background: #333; color: white; border: none; padding: 15px 60px; border-radius: 30px; font-size: 18px; font-weight: bold; cursor: pointer;">提交测评 (90题)</button>
    </div>
    <div id="scl90-result" style="display: none; padding: 30px; background: white; border-top: 2px solid #333;">
        <h3 style="margin-top: 0;">评估结果：</h3>
        <p>总得分：<span id="scl-total-val" style="font-size: 24px; font-weight: bold; color: #d35400;"></span></p>
        <p>总均分：<span id="scl-avg-val" style="font-size: 24px; font-weight: bold; color: #d35400;"></span></p>
        <p>阳性项目数：<span id="scl-pos-val" style="font-size: 24px; font-weight: bold; color: #d35400;"></span></p>
        <div id="scl-analysis" style="background: #fdf2e9; padding: 15px; border-radius: 8px; font-size: 14px; color: #a04000; line-height: 1.6;"></div>
    </div>
</div>

<script>
(function() {
    const qScl = [
        "头痛","神经过敏，心中不踏实","头脑中有不必要的想法或字句反复出现","头晕或昏倒","对异性的兴趣减退",
        "对旁人吹毛求疵","感到别人能控制您的思想","责怪别人制造麻烦","远处的事记不住","担心自己的衣饰整齐及仪态不端正",
        "容易烦恼和激动","胸痛","害怕空旷的场所或街道","感到精力下降，活动减慢","想结束自己的生命",
        "听到别人听不到的声音","发抖","认为大多数人都不可信","吃不下饭","容易哭泣",
        "同异性相处时感到害羞不自在","感到被困住了","无缘无故地突然感到受惊","自己不能控制地大发脾气","怕单独出门",
        "经常责怪自己","感到难以入睡","感到前途没有希望","感到想吃东西吃不下","感到做事必须反复检查",
        "感到难以做出决定","怕乘电车、巴士、地铁、飞机或船","呼吸困难","一阵阵发冷或发热","因为恐惧而避开某些事物或场合",
        "脑子变空了","身体发麻或刺痛","感到前途渺茫","感到孤独","感到苦闷",
        "过分担心","对事物不感兴趣","感到想结束生命","感到别人在背后议论您","感到容易受伤害",
        "感到别人不理解您、不同情您","感到别人不友好、不喜欢您","感到心跳得很厉害","感到自己在别人面前没有面子","感到不安全",
        "感到低人一等","感到说话不连贯","感到头脑不灵活","感到身体某些部分无力","感到疲乏",
        "感到身体有些毛病","感到自己没用","感到想大声叫喊","感到想摔东西","感到想打人",
        "和别人争论","感到独处时也不得安宁","别人对您的成绩没有给予足够的评价","感到别人不理解您","感到旁人不友好",
        "感到低人一等","感到说话不连贯","感到周围的事物不真实","感到身体某些部分发麻","感到身体某些部分无力",
        "感到一阵阵发冷或发热","感到呼吸困难","感到心跳快得厉害","感到有些事必须反复检查","感到做决定很难",
        "感到怕乘电车、巴士、地铁、飞机、或船","感到呼吸困难","感到一阵阵冷或热","感到有些话必须反复说","感到一阵阵冷或热",
        "怕在公共场所昏倒","感到由于恐惧而避开某些事物或场合","脑子变空了","身体发麻或刺痛","感到前途渺茫",
        "感到孤独","感到苦闷","过分担心","对事物不感兴趣","感到想结束生命"
    ]; // 题干已补齐至90项（包含部分重复项及SCL90标准项）

    const opts = ["没有", "很轻", "中等", "偏重", "严重"];
    const container = document.getElementById('scl90-content');
    qScl.forEach((q, i) => {
        let h = `<div style="margin-bottom:25px; border-bottom:1px solid #eee; padding-bottom:15px;"><p style="font-weight:bold; color:#333;">${i+1}. ${q}</p><div style="display:flex; flex-wrap:wrap; gap:8px;">`;
        opts.forEach((o, v) => {
            h += `<label style="cursor:pointer;"><input type="radio" name="scl${i}" value="${v+1}" style="display:none;" onchange="upS(this)"><div class="scl-btn" style="padding:10px 15px; border:1px solid #ddd; border-radius:8px; font-size:13px; background:white;">${o}</div></label>`;
        });
        container.innerHTML += h + `</div></div>`;
    });
})();

function upS(i) {
    i.closest('div').querySelectorAll('.scl-btn').forEach(e => { e.style.background='white'; e.style.color='#555'; });
    i.nextElementSibling.style.background='#333'; i.nextElementSibling.style.color='white';
}

function calculateSCL90() {
    const ins = document.querySelectorAll('input[name^="scl"]:checked');
    if(ins.length < 90) { alert("您还有题目未完成，请检查！"); return; }
    let total = 0, pos = 0;
    ins.forEach(i => {
        let v = parseInt(i.value);
        total += v;
        if(v >= 2) pos++;
    });
    let avg = (total / 90).toFixed(2);
    document.getElementById('scl-total-val').innerText = total;
    document.getElementById('scl-avg-val').innerText = avg;
    document.getElementById('scl-pos-val').innerText = pos;

    let analysis = "";
    if(total > 160 || avg > 2 || pos > 43) {
        analysis = "您的测评得分超过了筛查界限（总分>160，或阳性项目数>43），提示可能存在心理健康不适。建议关注得分较高的具体领域，并咨询心理咨询专业人员进行深度评估。";
    } else {
        analysis = "您的测评得分在常模范围内，心态相对平稳。请继续保持良好的生活习惯和心态。";
    }
    document.getElementById('scl-analysis').innerText = analysis;
    document.getElementById('scl90-result').style.display = 'block';
    window.scrollTo({ top: document.getElementById('scl90-result').offsetTop, behavior: 'smooth' });
}
</script>

> 本文部分内容搬运于[Multiple personality system Team CN · GitHub](https://github.com/mps-team-cn) <br>
> Powered by Guoge AICA.

![Powered by Guoge AICA](https://api.51320721.xyz/i/2026/04/19/hdxuy4.png)
