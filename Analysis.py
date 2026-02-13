import kagglehub
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. SCARICAMENTO AUTOMATICO DA KAGGLE
# Scarica l'ultima versione del dataset rhuebner/human-resources-data-set
path = kagglehub.dataset_download("rhuebner/human-resources-data-set")
print(f"Dataset scaricato in: {path}")

# Trova il file CSV nella cartella scaricata
csv_path = os.path.join(path, "HRDataset_v14.csv")
df = pd.read_csv(csv_path)

# 2. DEFINIAMO IL PERCORSO DI USCITA (La tua cartella sul desktop)
output_folder = r"C:\Users\Lorenzo\Desktop\hr-analytics-project\HR-Behavioral-Analysis-v14"

# Impostazioni grafiche professionali
sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300

# --- ANALISI A: MOTIVI DI DIMISSIONE (Psicologia del Lavoro) ---
plt.figure(figsize=(10, 8))
terminated = df[df['TermReason'] != 'N/A-StillEmployed']
sns.countplot(data=terminated, y='TermReason', order=terminated['TermReason'].value_counts().index, palette='magma')
plt.title('Deep Dive: Perché i dipendenti lasciano l\'azienda?', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'hr_termination_reasons.png'))

# --- ANALISI B: EQUITÀ SALARIALE PER GENERE ---
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Department', y='Salary', hue='Sex', palette='Set2')
plt.xticks(rotation=45)
plt.title('Analisi Equità Salariale (DEI)', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'hr_gender_pay_equity.png'))

# --- ANALISI C: ENGAGEMENT VS ASSENZE ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='EngagementSurvey', y='Absences', hue='PerformanceScore', s=100)
plt.title('Relazione tra Engagement e Assenteismo', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'hr_engagement_vs_absences.png'))

print(f"\n✅ Analisi completata! I grafici sono stati salvati in: {output_folder}")