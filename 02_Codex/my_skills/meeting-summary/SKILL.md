---
name: meeting-summary
description: 根据会议内容生成摘要。当用户表达“会议摘要”、“总结会议”等意图时触发。
---

## 输入预处理
如果用户传入的会议内容包含时间戳（格式如 `[00:00:01.000 --> 00:00:05.000]`），说明这是 ASR 原始转写文本，需要先清洗：
1、将内容保存到系统临时文件 `/tmp/asr_input.txt`
2、执行脚本：`python3 ./scripts/asr_postprocess.py /tmp/asr_input.txt -o /tmp/asr_clean.txt`
3、读取 `/tmp/asr_clean.txt` 的内容，作为后续生成摘要的输入
如果输入不含时间戳，跳过此步骤，直接使用原始输入

## 路由
#### 人事会议
触发条件：
- 出现招聘、入职、离职、培训、绩效、考勤等内容
- 出现 HR、人事、招聘主管 等角色
- 重点讨论人员安排与时间节点

读取并使用：
@references/hr_meeting.md

## 财务会议
触发条件：
- 出现预算、报销、成本、利润、ROI、审批等内容
- 出现财务、出纳、CFO 等角色
- 重点讨论金额、成本控制、财务风险

读取并使用：
@references/finance_meeting.md

## 通用会议
如果无法明确会议类型，读取并使用：
@references/general_meeting.md

## 约束
会议摘要的每一项都只用一句话来表述，不要写多条