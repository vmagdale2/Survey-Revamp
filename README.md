# **Survey Project: Modernizing Survey Processes**

---

## **Project Description**
This project focuses on enhancing the survey process for conference participants. The traditional paper-based survey system was transitioned to a virtual format using open-source tools and AI-driven insights. The revamped process aims to improve **efficiency**, **response rates**, and **real-time analytics** while enabling actionable feedback to shape future conferences.

---

## **Objectives**
- Transition from paper-based to virtual surveys.
- Leverage open-source tools to modernize the data collection process.
- Utilize AI-driven insights to provide **actionable feedback**.
- Enable **real-time analytics** for immediate insights during conferences.
- Achieve higher participant **response rates**.
- Assist the company in attaining a presentation rating of **"Excellent"**.

---

## **Data**
### **Dataset Description**
The datasets provided by the company include:
- **Survey Results**: Feedback collected from participants.
- **Historical Data**: Previous survey metrics for benchmarking.

> **Note**: Data includes sensitive information; ensure compliance with company data privacy guidelines.

## Data Folder Structure

This folder contains the data used for the project, organized as follows:

### Raw Data (`/raw`)
- **original_data.xlsx**: The original dataset received on [date]. This file has not been modified.

### Processed Data (`/processed`)
- **cleaned_data.xlsx**: The cleaned version of the dataset. This includes:
  - Removal of duplicates
  - Handling of missing values
  - Standardization of column names

### Notes
- Always start with the raw data for any new analysis.
- Document all cleaning steps in a `data_preprocessing_script.py` or equivalent file.


---

## **Tools Used**
### **Python Libraries**
1. **Pandas**:
   - Data cleaning, wrangling, and preparation.
   - Exploratory Data Analysis (EDA).
2. **Matplotlib**:
   - Visualizing trends in survey responses.
   - Highlighting key metrics for actionable insights.
3. **Scikit-learn**:
   - Predictive analysis on survey completion rates.
   - Clustering and segmentation of participant feedback.
### **Apps** 
Python, PyCharm, R (Tidyverse, ggplot), RStudio, SQL (PostgreSQL, MySQL)

Tableau, LucidChart, Jupyter Notebooks, GitHub

Microsoft Products: Excel, Visual Studio Code

Google Apps: BigQuery, Drive, Cloud Storage, Colab 

---

## **Results**
The revamped survey system has achieved:
- **Higher response rates** compared to the paper-based process.
- **Faster data collection** with real-time analysis capabilities.
- **Key Insight**: The company is still striving to achieve an **"Excellent"** rating in their conferences.

---

## **How to Run the Analysis**
### **Instructions**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/survey-project-modernization.git

2. **Navigate to the Project Directory**:
   ```bash
   cd survey-project-modernization
3. **Install Required Libraries**
   ```bash
   pip install -r requirements.txt
4. **Run the Analysis** 
   ```bash
   python analysis.py

> **Note**: **Detailed instructions for reproducing the analysis, including dataset preprocessing, will be added soon. Stay tuned!**

---

## EDA
### **Word Cloud Generation**
| Item | Location| 
|---|---|
| Code | Notebooks/word_cloud.ipynb |
| Standalone Script | Scripts/visualization/word_cloud.py |
|Output | Results/Figures/ 
| Images | Images/WC.img |

---

## **Acknowledgments**
* Special thanks to the conference participants for their valuable feedback.
* Gratitude to the company for providing datasets and resources.

**Author**: Veronica Magdaleno
