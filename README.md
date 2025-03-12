# Capstone_project_Bank_Stability_Analysis
![Screenshot 2024-12-26 170501](https://github.com/user-attachments/assets/ff0c81f9-68fe-44f3-8074-6df2c23ca5ef)
![Screenshot 2025-03-08 201511](https://github.com/user-attachments/assets/41d5252a-40f8-4083-97dc-7f04ce6bc82f)
![Screenshot 2025-03-08 201612](https://github.com/user-attachments/assets/ca5ebc0e-0247-4c66-a44a-059bf460f9cc)
![Screenshot 2024-12-26 152412](https://github.com/user-attachments/assets/7d8329e8-19e0-4f61-9a73-5a7d845467b1)

### **Basic Idea About the Project - Bank Stability Analysis**

This project focuses on **predicting bank stability** using machine learning models. It involves analyzing financial metrics to determine which factors contribute to a bank's stability or potential failure.

### **Key Objectives:**
1. **Develop a Predictive Model**  
   - Build a machine learning model to assess bank stability.
   - Improve accuracy using advanced algorithms.

2. **Identify Key Stability Factors**  
   - Analyze financial indicators like **Capital Adequacy Ratio (CAR)**, **Non-Performing Loans (NPL)**, **Liquidity Ratio**, and **Return on Assets (ROA)**.
   - Discover which factors most influence a bank’s stability.

### **Dataset Summary:**
- **Size:** 5,000 rows, 11 columns.
- **Key Features:**
  - **CAR (<10%)** → Higher risk of bank failure.
  - **NPL (>15%)** → Indicates unstable banks.
  - **Liquidity Ratio (<20%)** → Suggests financial distress.
  - **LDR (>90%)** → Signals liquidity stress.
  - **ROA & NIM** → Higher values indicate better profitability.

### **Machine Learning Approach:**
- **Exploratory Data Analysis (EDA)**
  - Used Python (Pandas, Matplotlib, Seaborn) for data visualization.
  - Analyzed feature correlations using heatmaps and scatterplots.

- **Data Preprocessing**
  - Addressed missing values and outliers.
  - Encoded categorical variables and scaled numerical data.

- **Modeling & Comparison**
  - **Decision Tree (99% accuracy)** – Easy to interpret but prone to overfitting.
  - **Random Forest (98%-99% accuracy)** – More robust, reduces overfitting, provides feature importance.

### **Business Impact:**
- Can be used for **early warning systems** to detect financially unstable banks.
- Helps **regulatory bodies** and **banking institutions** in risk assessment.
- Allows for better decision-making in banking regulations and financial monitoring.


