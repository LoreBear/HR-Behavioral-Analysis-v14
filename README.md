# HR Behavioral Analytics: Decoding Turnover & Burnout
### Project by Lorenzo Di Salvatore  
Work and Organizational Psychology | HR Data Analytics Specialist

![Focus](https://img.shields.io/badge/Focus-People%20Analytics-blue)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Power%20BI-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Project Overview: The Organizational "Biopsy"

Why do employees really leave? In traditional HR, attrition is often treated as a simple turnover statistic. Through the lens of Work & Organizational Psychology, attrition is a symptom of systemic friction.

This project analyzes the HR Dataset v14 (1,470 records) to move beyond descriptive reporting. The goal was to perform **Organizational Diagnostics**, identifying invisible psychological drivers such as breaches of the **Psychological Contract** and high-performer burnout that raw numbers often hide.

---

## Executive Summary: Diagnostic Findings

Attrition is rarely about pay alone. The data reveals a complex interplay of leadership quality, workload, and emotional exhaustion.

---

## Core Organizational Paradoxes

### 1. The Absence Paradox (Burnout Detection)

- **What the data shows:** Highest performers ("Exceeds") have higher absence rates (10.5 days) than low performers (8.3 days).  
- **Psychologist's Take:** This is a **Leading Indicator of Burnout**. Highly engaged employees over-extend themselves, using absenteeism as a coping mechanism. They are "walking wounded"—productive but exhausted—and at high risk for sudden resignation.

### 2. Micro-Climate Toxicity vs. Company Culture

- **What the data shows:** Two managers drive ~62% of their teams' attrition, while the company average remains below 20%.  
- **Psychologist's Take:** "People don't leave companies; they leave managers." Localized leadership behavior creates micro-climates that can anchor or repel talent, independent of company-wide perks.

### 3. The Hygiene Factor Gap: Culture over Cash

- **What the data shows:** "Unhappiness" (culture) outranks "More Money" (salary) as a reason for leaving.  
- **Psychologist's Take:** Based on Herzberg’s Two-Factor Theory, adequate salary prevents dissatisfaction but does not drive loyalty. Cultural dissatisfaction signals a breakdown in emotional fulfillment that pay alone cannot fix.
  

## Visual Analysis and Organizational Diagnostics

---

### Executive Workforce Snapshot

![Dashboard Overview](Dashboard.png)
(Dashboard Overview)

**What data shows**  
• Attrition Rate: 33%  
• Avg Engagement: 4.09  
• Avg Salary: 69K  
• Gender Pay Gap Index: 0.04  

**Business Meaning**  
Attrition concentration appears at manager level, not company level.

---

### Managerial Risk Concentration

(Contained in dashboard overview)

**Observation**  
Two managers exceed 60% attrition while most stay below 20%.

**Business Meaning**  
Turnover links strongly to leadership quality.

**Action**  
Target leadership coaching before launching global retention programs.

---

### Recruitment Channel Distribution

(Contained in dashboard overview)

**Observation**  
Indeed and LinkedIn generate most hires.

**Risk**  
High dependency on few external talent pipelines.

---

### Workforce Composition and DEI Context

![DEI Overview](DE&I.png)
(DEI Overview)

**Population Distribution**  
Majority White workforce, followed by Black or African American and Asian employees.

**Why This Matters**  
Population structure must be evaluated before interpreting pay gap or attrition variance.

---

### Gender Pay Gap by Department

(Contained in DEI overview)

**Observation**  
• Sales favors female salary levels  
• IT/IS favors male salary levels  

**Root Driver**  
Salary correlates 0.51 with SpecialProjectsCount.  
Unequal access to high-visibility projects likely influences pay distribution.

---

### Attrition by Life Context

(Contained in DEI overview)

**Observation**  
Higher termination counts in Single and Married groups reflect workforce composition.

**Use Case**  
Validates attrition models against demographic distribution.

---

### Termination Reasons: Culture vs Market

![Termination Reasons](hr_termination_reasons.png)

**What data shows**  
• Another Position ranks first  
• Unhappy ranks second  
• More Money ranks third  

**Business Meaning**  
Cultural dissatisfaction drives exits more than compensation alone.

**Analysis**  
"Unhappy" (14 cases) is a stronger exit driver than "More Money" (11 cases). This signals a breakdown in the organizational climate and requires cultural intervention rather than broad pay adjustments.

---

### Burnout Risk Detection

![Engagement vs Absences](hr_engagement_vs_absences.png)

**What data shows**  
High performers record highest absence averages.

**Business Meaning**  
Early burnout indicator, not disengagement.

**Analysis**  
Top performers ("Exceeds") have higher absence rates (10.5 days) than low performers (8.3 days). These employees are over-extending themselves, using absences to cope before potential resignation. This is a **Leading Indicator of Burnout**.

---

### Structural Pay Equity Pattern

![Gender Pay Equity](hr_gender_pay_equity.png)

**What data shows**  
Pay variance exists at department level, not company level.

**Analysis**  
The IT/IS pay gap correlates 0.51 with `SpecialProjectsCount`. This suggests unequal access to high-visibility projects drives the variance rather than direct salary bias.

---

### Data Engineering Layer (Python)

Tools  
• kagglehub  
• pandas  
• seaborn  
• matplotlib  

Work Completed  
• Automated dataset ingestion  
• Removed trailing whitespace in categorical columns  
• Created binary Attrition variable  
• Built correlation models between workload, salary, and absence  

---

### Business Intelligence Layer (Power BI)

Goal: Convert statistical output into decision interface.

#### Core DAX Measure

```dax
Attrition Rate =
DIVIDE(
    CALCULATE(COUNTROWS('HR_Data'),
    'HR_Data'[Status] = "Terminated"),
    COUNTROWS('HR_Data'),
    0
)
```

Other Measures  
• Gender Pay Gap Index  
• Manager Attrition Risk Ranking  
• Workforce Engagement Index  

---

### Dashboard Decision Flow

Executive Layer  
• Attrition KPI  
• Engagement KPI  
• Salary KPI  

Diagnostic Layer  
• Burnout Signals  
• Termination Drivers  

Root Cause Layer  
• Manager Attrition Ranking  
• Department Pay Equity  

---

## Strategic Actions

### Leadership Intervention
Focus on highest attrition managers first.

### Burnout Early Warning
Flag employees with:
Performance > 4  
Absences > 10  

Treat as retention risk group.

### Project Allocation Audit
Review Special Project assignment distribution inside IT.

---

## Business Value

Python identifies statistical relationships.  
Power BI translates results into operational decisions.

Outcome: shift from reactive hiring to predictive retention strategy.

---

## Author

Lorenzo Di Salvatore  
HR Analytics | Organizational Psychology | People Data Strategy
* LinkedIn: [Lorenzo Di Salvatore](https://www.linkedin.com/in/lorenzo-di-salvatore-psico)
* Portfolio: [GitHub Repositories](https://github.com/LoreBear)

