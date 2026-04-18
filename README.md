# HR Behavioral Analytics: Decoding Turnover & Burnout
### Project by Lorenzo Di Salvatore
Work and Organizational Psychology | HR Data Analytics Specialist
 
![Focus](https://img.shields.io/badge/Focus-People%20Analytics-blue)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Power%20BI-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
 
---
 
## Project Overview: The Organizational "Biopsy"
 
Why do employees really leave? In traditional HR, attrition is often treated as a turnover statistic — a number to report, not a signal to decode. Through the lens of Work & Organizational Psychology, attrition is a symptom of systemic friction: broken psychological contracts, leadership failures, and invisible burnout accumulating beneath the surface of performance data.
 
This project analyzes the HR Dataset v14 (**311 employee records**) to move beyond descriptive reporting and perform **Organizational Diagnostics** — identifying the behavioral and structural drivers that raw numbers consistently hide.
 
**Dataset:** HR Dataset v14 (Kaggle — rhuebner/human-resources-data-set)
**Tools:** Python (Pandas, Seaborn, Matplotlib) · Power BI (DAX, Power Query)
**Overall attrition rate:** 33% (one in three employees has left the organization)
 
---
 
## Executive Summary: Diagnostic Findings
 
Attrition is rarely about pay alone. The data reveals a complex interplay of leadership quality, workload, and emotional exhaustion converging into three organizational paradoxes:
 
| # | Paradox | Finding |
|---|---------|---------|
| 1 | The Absence Paradox | Top performers ("Exceeds") have *higher* absence rates (10.5 days) than low performers (8.3 days) |
| 2 | Micro-Climate Toxicity | Two managers drive ~62% attrition within their teams; company average sits below 33% |
| 3 | Culture over Cash | "Unhappy" (14 exits) outranks "More Money" (11 exits) as a reason for leaving |
 
---
 
## Core Organizational Paradoxes
 
### 1. The Absence Paradox (Burnout Detection)
 
- **What the data shows:** Employees rated "Exceeds" in performance average **10.5 absence days**, compared to 8.3 days for low performers. High engagement does not protect against absenteeism — it accelerates it.
- **Psychologist's Take:** This is a **leading indicator of burnout**, not disengagement. Highly committed employees over-extend themselves, absorbing organizational slack until the psychological cost becomes unsustainable. Absenteeism becomes a coping mechanism — a pressure valve — before the inevitable resignation. These employees are "walking wounded": productive on paper, exhausted in reality, and at the highest risk of sudden departure precisely because no one is watching for the warning signs.
### 2. Micro-Climate Toxicity vs. Company Culture
 
- **What the data shows:** Two managers (Amy Dunn and Webster Butler) exceed **62% attrition** within their teams, while most managers sit below 30%. This is not a company-wide problem — it is geographically precise.
- **Psychologist's Take:** "People don't leave companies; they leave managers." Localized leadership behavior creates **organizational micro-climates** that can anchor or repel talent entirely independent of company-wide benefits, culture programs, or pay levels. A retention strategy applied at the organizational level will have near-zero effect on teams experiencing managerial toxicity. The intervention must be surgical, not systemic.
### 3. The Hygiene Factor Gap: Culture over Cash
 
- **What the data shows:** "Unhappy" ranks as the second most common exit reason (14 cases), ahead of "More Money" (11 cases). "Another Position" leads at 20 cases — but critically, the decision to accept another position is often triggered by pre-existing dissatisfaction, not the offer itself.
- **Psychologist's Take:** Herzberg's Two-Factor Theory draws a clear line: adequate salary prevents dissatisfaction but does not create loyalty. When "Unhappy" outranks "More Money" as an exit driver, the organization is facing a **breakdown in emotional fulfillment** — a breach of the psychological contract between employee and employer. A pay raise applied to a cultural problem is not a solution; it is a delay.
---
 
## Visual Analysis and Organizational Diagnostics
 
---
 
### Executive Workforce Snapshot
 
![Dashboard Overview](Dashboard.png)
 
**What the data shows**
- Attrition Rate: **33%** — one in three employees has left
- Avg Engagement Score: **4.09** (scale 1–5)
- Average Salary: **$69K**
- Gender Pay Gap Index: **0.04** — low at company level, but uneven across departments
**Business Meaning**
The headline numbers mask the real story. A 33% attrition rate distributed unevenly across managers means a blanket retention program would waste budget protecting teams that don't need it, while leaving the highest-risk micro-climates untouched. The diagnostic imperative is to move from company-level averages to manager-level accountability.
 
---
 
### Managerial Risk Concentration
 
*(Contained in Dashboard Overview)*
 
**What the data shows**
- Amy Dunn and Webster Butler: **>60% attrition** within their teams
- Majority of managers: below 30%
- The distribution is sharply right-skewed — this is not statistical noise
**Business Meaning**
Attrition is not a company-wide disease. It is a localized infection under two specific leaders. This finding reframes the entire retention strategy: before launching engagement surveys, salary benchmarking, or culture programs, the organization must ask a more targeted question — *what is happening inside those two teams?*
 
**Action**
Initiate a structured leadership review for high-attrition managers before deploying any global retention investment.
 
---
 
### Recruitment Channel Distribution
 
*(Contained in Dashboard Overview)*
 
**What the data shows**
- Indeed: **27.97%** of hires
- LinkedIn: **24.44%**
- Google Search and Employee Referral follow
**Business Meaning**
Over 50% of recruitment volume is concentrated in two external platforms. This is an operational risk: any algorithm change, pricing shift, or platform disruption directly impacts talent pipeline continuity. Diversifying toward Employee Referral — which typically produces higher retention rates and faster time-to-productivity — should be a strategic priority.
 
---
 
### Workforce Composition and DEI Context
 
![DEI Overview](DE&I.png)
 
**What the data shows**
- Majority White workforce, followed by Black or African American and Asian employees
- Recruitment sources show meaningful Diversity Job Fair representation (9.32%)
- Marital status distribution: Single and Married groups are largest by headcount
**Business Meaning**
Population structure is the prerequisite to any equitable analysis. Attrition or pay variance interpreted without demographic baseline creates misleading conclusions. This overview establishes the compositional context against which all downstream findings must be validated — ensuring that patterns reflect structural dynamics, not population size artifacts.
 
---
 
### Gender Pay Gap by Department
 
*(Contained in DEI Overview)*
 
**What the data shows**
- IT/IS: pay gap favors male salary levels
- Admin Offices: pay gap favors male salary levels
- Sales: pay gap favors female salary levels
- Production and Software Engineering: near parity
**Business Meaning**
The pay gap is not a company-level phenomenon — it is department-specific, which is the analytically significant finding. A company-wide Gender Pay Gap Index of 0.04 would normally signal equity. But department-level disaggregation reveals structural inequality hidden inside the average.
 
**Root Driver**
Salary correlates **0.51 with `SpecialProjectsCount`**. The IT/IS gap is most likely not a product of direct salary bias — it is a product of unequal access to high-visibility, career-accelerating projects. Closing the gap at the base pay level treats the symptom; auditing project assignment processes treats the cause.
 
---
 
### Termination Reasons: Culture vs. Market
 
![Termination Reasons](hr_termination_reasons.png)
 
**What the data shows**
- Another Position: **20 exits** — the leading reason
- Unhappy: **14 exits** — second place
- More Money: **11 exits** — third place
- Hours, Career Change, Attendance follow
**Business Meaning**
The ranking of "Unhappy" above "More Money" is the most diagnostically important finding in this dataset. It tells us that cultural dissatisfaction is a stronger and more prevalent exit driver than compensation inadequacy — which directly contradicts the instinct to respond to attrition with salary adjustments.
 
**Analysis**
"Another Position" often gets misread as a market-driven exit. In reality, employees who are genuinely fulfilled rarely accept competing offers. The decision to *look* is made weeks or months before the offer arrives. "Another Position" is frequently the vehicle; "Unhappy" is the fuel. Treating them as separate causes understates cultural dissatisfaction as a driver by nearly 50%.
 
---
 
### Burnout Risk Detection
 
![Engagement vs Absences](hr_engagement_vs_absences.png)
 
**What the data shows**
- "Exceeds" performers: average **10.5 absence days**
- "Fully Meets" performers: broadly distributed across absence levels
- "Needs Improvement" and "PIP" employees: concentrated at lower absence ranges
- High engagement scores do not predict low absenteeism — if anything, the reverse is visible in the top performer cluster
**Business Meaning**
This chart inverts the conventional assumption. Absenteeism is typically treated as a disengagement signal — a marker of low commitment. Here it functions as the opposite: a **burnout coping mechanism** deployed by the organization's most committed people.
 
**Analysis**
The "Exceeds" cluster at high absence rates represents the highest-value, highest-risk segment in the workforce. These employees are not checked out — they are overextended. They are absorbing organizational demand beyond sustainable limits and using sick days as a pressure valve. Without early intervention, the trajectory is predictable: psychological withdrawal, then resignation. The critical error is waiting for performance to drop before acting, because by that point the decision to leave has already been made.
 
---
 
### Structural Pay Equity Pattern
 
![Gender Pay Equity](hr_gender_pay_equity.png)
 
**What the data shows**
- Production: near salary parity between M and F
- IT/IS: wider male salary distribution, with several high-salary male outliers
- Software Engineering: female median slightly higher
- Admin Offices: broader female salary range
- Sales: broadly equitable with some female-side outliers
**Business Meaning**
Pay variance is real but structurally localized — it is not evidence of company-wide systemic bias. The IT/IS department drives the observed gap, and the **0.51 correlation between salary and `SpecialProjectsCount`** offers a structurally coherent explanation: access to high-visibility projects determines long-term compensation trajectory. Those who receive more projects accumulate more experience, more visibility, and more leverage in salary negotiations. If the assignment of those projects is informally biased — even unconsciously — the pay gap becomes self-reinforcing over time.
 
**Action**
An audit of Special Project assignment criteria and decision-making in IT/IS is more likely to close the gap durably than a targeted salary adjustment.
 
---
 
## Strategic Actions: The A.B.E. Framework
 
### A — Accountability: Targeted Leadership Coaching
 
**The Issue:** Attrition is not a company-wide problem — it is concentrated under two specific managers at rates exceeding 60%. Investing in broad culture programs while leaving this dynamic unaddressed is organizationally equivalent to patching a roof while the foundation is cracked.
 
**The Intervention:** Launch a structured behavioral coaching program targeting high-attrition managers, grounded in 360° feedback and supported by monthly team pulse surveys. The goal is not performance management — it is leadership development, addressing the specific behaviors that create toxic micro-climates.
 
**Why this works:** Localized problems require localized interventions. Resolving two manager-level dynamics has a direct, measurable impact on the 62%+ attrition clusters — without requiring company-wide budget or restructuring.
 
---
 
### B — Burnout Shield: Early Warning Protocol
 
**The Issue:** Top performers are using sick days as a coping mechanism before eventual resignation. By the time performance declines or resignation arrives, the window for intervention has already closed.
 
**The Intervention:** Implement an automated early-warning flag in the HR system. The trigger condition: `PerformanceScore = "Exceeds"` AND `Absences > 10`. When both conditions are met, the system prompts a **Stay Interview** — a structured one-on-one focused on workload, recognition, and psychological safety, not performance.
 
**Why this works:** The intervention targets the right segment (high performers) at the right moment (before disengagement sets in), using the data signal that actually predicts burnout (absence rate) rather than the one that typically gets monitored (performance score).
 
---
 
### E — Equity: The Project Access Audit
 
**The Issue:** The gender pay gap in IT/IS is structurally driven by differential access to Special Projects (correlation: 0.51), not direct salary discrimination. Adjusting base pay without addressing the upstream access inequality will not close the gap — it will temporarily mask it.
 
**The Intervention:** Standardize the assignment process for high-visibility projects in IT/IS through transparent eligibility criteria and documented selection decisions. Equitable access to career-accelerating projects closes the pay gap at its structural source — career progression — rather than through compensatory salary corrections.
 
**Why this works:** Treating the root cause (access inequality) is more durable and organizationally credible than treating the outcome (pay disparity). It also signals an equity-first culture to current and prospective employees.
 
---
 
## Business Impact & ROI
 
Framing HR data as a financial asset is what shifts HR from a support function to a strategic partner.
 
**Cost Avoidance:** Replacing a mid-level employee costs approximately 1.5× their annual salary. With two "Red Zone" managers driving 60%+ attrition in their teams, resolving these two micro-climates alone protects the organization from a disproportionate share of preventable replacement costs.
 
**Productivity Protection:** Flagging the Burnout Paradox (High Performance + High Absence) allows targeted intervention before the organization loses its highest contributors. These are not replaceable employees — they are the ones absorbing the most organizational demand.
 
**Strategic Credibility:** This analysis moves the HR function from reactive incident response to evidence-based risk stratification. The shift is not rhetorical — it is methodological: from counting exits to predicting them.
 
---
 
## Technical Architecture
 
---
 
### Data Engineering Layer (Python)
 
**Tools:** kagglehub · pandas · seaborn · matplotlib
 
**Work Completed**
- Automated dataset ingestion via Kaggle API
- Removed trailing whitespace in all categorical columns (`Sex`, `Department`, `TermReason`)
- Created binary attrition variable from `EmploymentStatus`
- Built correlation models between workload (`Absences`), compensation (`Salary`, `SpecialProjectsCount`), and engagement (`EngagementSurvey`, `PerformanceScore`)
- Exported cleaned dataset for Power BI consumption
```python
import kagglehub
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
 
path = kagglehub.dataset_download("rhuebner/human-resources-data-set")
df = pd.read_csv(os.path.join(path, "HRDataset_v14.csv"))
 
# Clean string columns
df['Sex'] = df['Sex'].str.strip()
df['Department'] = df['Department'].str.strip()
 
sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300
 
# Termination Reasons
plt.figure(figsize=(10, 8))
terminated = df[df['TermReason'] != 'N/A-StillEmployed']
sns.countplot(data=terminated, y='TermReason',
              order=terminated['TermReason'].value_counts().index,
              palette='magma')
plt.title('Deep Dive: Why are employees leaving the company?', fontsize=14)
plt.tight_layout()
plt.savefig('hr_termination_reasons.png')
 
# Gender Pay Equity
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Department', y='Salary', hue='Sex', palette='Set2')
plt.xticks(rotation=45)
plt.title('Salary Equity Analysis by Department & Gender', fontsize=14)
plt.tight_layout()
plt.savefig('hr_gender_pay_equity.png')
 
# Engagement vs Absences (Burnout Signal)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='EngagementSurvey', y='Absences',
                hue='PerformanceScore', s=100)
plt.title('Correlation: Engagement Score vs. Absenteeism', fontsize=14)
plt.tight_layout()
plt.savefig('hr_engagement_vs_absences.png')
 
df.to_csv('data_cleaned.csv', index=False)
```
 
---
 
### Business Intelligence Layer (Power BI)
 
**Goal:** Convert statistical output into an operational decision interface structured across three diagnostic layers.
 
#### Core DAX Measures
 
```dax
Attrition Rate =
DIVIDE(
    CALCULATE(COUNTROWS('HR_Data'),
    'HR_Data'[EmploymentStatus] = "Voluntarily Terminated"),
    COUNTROWS('HR_Data'),
    0
)
 
Gender Pay Gap Index =
DIVIDE(
    CALCULATE(AVERAGE('HR_Data'[Salary]), 'HR_Data'[Sex] = "M") -
    CALCULATE(AVERAGE('HR_Data'[Salary]), 'HR_Data'[Sex] = "F"),
    CALCULATE(AVERAGE('HR_Data'[Salary]), 'HR_Data'[Sex] = "M"),
    0
)
```
 
**Additional Measures**
- Manager Attrition Risk Ranking
- Workforce Engagement Index
- Burnout Risk Flag (Performance + Absence composite)
---
 
### Dashboard Decision Flow
 
**Executive Layer**
Attrition KPI · Engagement KPI · Salary KPI · Gender Pay Gap Index
 
**Diagnostic Layer**
Manager Attrition Ranking · Recruitment Channel Distribution · Termination Reason Breakdown
 
**Root Cause Layer**
Burnout Risk Scatter (Engagement vs. Absences) · Department Pay Equity · DEI Population Structure
 
---
 
## Future Scope: The Next Phase
 
While this analysis diagnoses *where* and *why* attrition happens, the next phase would focus on *predicting* it before it occurs:
 
**Predictive Flight Risk Modeling (Machine Learning):** A Logistic Regression or Random Forest classifier trained on absence patterns, engagement scores, manager assignment, and tenure would produce an individual-level "Probability of Exit" score — enabling pre-emptive retention conversations before the resignation letter arrives.
 
**NLP on Exit Interviews:** Applying Sentiment Analysis and topic modeling to open-text exit survey responses would quantify the "Unhappy" driver with semantic precision — revealing whether dissatisfaction is rooted in direct management, peer relationships, workload, or organizational values.
 
**ONA (Organizational Network Analysis):** Mapping internal communication and collaboration patterns would identify structurally isolated employees — those operating at the edges of organizational networks — who are significantly more likely to leave due to weak social anchoring, even when engagement scores appear normal.
 
---
 
## Author
 
Lorenzo Di Salvatore
HR Analytics | Organizational Psychology | People Data Strategy
 
- LinkedIn: [Lorenzo Di Salvatore](https://www.linkedin.com/in/lorenzo-di-salvatore-psico)
- Portfolio: [GitHub Repositories](https://github.com/LoreBear)
