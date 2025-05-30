# 🌍 World Happiness Report - Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project presents an Exploratory Data Analysis (EDA) of the **World Happiness Report 2023**. The goal is to uncover patterns and relationships between various social, economic, and psychological factors and a country's happiness score. We analyze which features have the strongest positive and negative influence on happiness and visualize the findings using Python libraries such as Pandas, Seaborn, and Matplotlib.

---

## 📁 Dataset Information

- 📄 **Source**: Kaggle / World Happiness Report (2023 version)
- 📌 **Format**: CSV
- 🧠 **Attributes Used**:
  - Happiness score
  - GDP per capita
  - Social support
  - Healthy life expectancy
  - Freedom to make life choices
  - Generosity
  - Perceptions of corruption
  - Positive affect
  - Negative affect

---

## 🧹 Data Cleaning

- Checked for missing values using `isnull().sum()`.
- Found and filled missing value in the **Perceptions of corruption** column.
- Selected only relevant columns for analysis.
- Sorted data based on the Happiness score for better insights.

---

## 📊 Data Analysis & Visualizations

- **Distribution Plot**: To understand how happiness scores are spread across countries.
- **Box Plots**: Identified outliers in each numeric feature.
- **Heatmap**: Correlation matrix to evaluate how strongly each feature affects the happiness score.

### 🔍 Key Observations

- **Positively Correlated Features**:
  - `Social support`, `GDP per capita`, and `Healthy life expectancy` show strong positive correlation with happiness.
- **Negatively Correlated Features**:
  - `Perceptions of corruption` and `Negative affect` reduce overall happiness.
- **Interesting Insight**:
  - Countries with high positive affect don't always score high on happiness, indicating deeper socio-economic contributors.

---

## 🧠 Conclusions

- Economic strength and social support are primary drivers of happiness.
- Reducing corruption and improving life satisfaction metrics can significantly enhance a country's overall happiness score.
- Outliers (like countries with extreme values) offer insights into unique social and political conditions.

---

## 🛠️ Tech Stack Used

- Python 🐍
  - pandas
  - matplotlib
  - seaborn

---

## 📌 How to Run the Project

1. Clone the repository or download the `.ipynb` file.
2. Install required packages if not already available:
   ```bash
   pip install pandas seaborn matplotlib
