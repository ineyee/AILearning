---
name: meeting-summary
description: 根据会议内容生成摘要。当用户表达“会议摘要”、“总结会议”等意图时触发。
---

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