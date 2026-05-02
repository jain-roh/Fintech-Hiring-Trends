
# 📊 Fintech Job Market Analysis
# 📊 Fintech Hiring Trends

Fintech Hiring Trends is a **research-driven data engineering and analytics project** aimed at understanding how top U.S. banks are hiring in **fintech-related roles**.

The project combines **data scraping, NLP-based classification, and pipeline automation** to analyze job postings and identify trends in fintech hiring.

---

## 🔗 Project Resources

- 📘 **Google Codelab**  
  https://codelabs-preview.appspot.com/?file_id=1587kQyFCBuz2GoGBCno3f3WbojxPtiVVphsBJvFQ_Dk#8  

- 🐳 **Docker Image**  
  https://hub.docker.com/r/rohitjain058/datascience  

- 💻 **GitHub Repository**  
  https://github.com/phadkeraj/A2_Fintech-Analysis  

- 📂 **Keywords Dataset (Dropbox)**  
  https://www.dropbox.com/home/DataScienceTeam9?preview=Keywords+and+Bucketing.xlsx  
  *(Final keyword dictionary used for classification)*  

- 📊 **Final Dataset (Dropbox)**  
  https://www.dropbox.com/home/DataScienceTeam9?preview=Fintech_Data.csv  
  *(Processed dataset used for analysis)*  

---

## 🎯 Objective

- Analyze hiring trends in fintech across major U.S. banks  
- Classify jobs into **Fintech vs Non-Fintech** using NLP  
- Identify key domains driving fintech growth  
- Build an automated data pipeline for continuous analysis  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Pipeline:** Luigi  
- **Data Processing:** Pandas, NLP techniques  
- **Visualization:** Tableau  
- **Deployment:** Docker  
- **Storage:** Dropbox  

---

## ⚙️ Pipeline Architecture (Luigi Workflow)

The project uses a **Luigi pipeline** to automate data processing:

1. Generate a merged dataset containing:
   - Institution  
   - Job URL  
   - Position  
   - Location  

2. Fetch dataset from Dropbox  

3. Apply **Fintech classification algorithm**:
   - Keyword-based NLP approach  
   - Feature engineering (FinWords vs TechWords)  

4. Generate enriched dataset  

5. Upload final dataset back to Dropbox  

6. Establish live connection with **Tableau Server** for visualization  

---

## 🔄 How to Run the Project

### Prerequisites
- Python installed  
- Required libraries (Luigi, Pandas, etc.)  
- Docker (optional)  

---

### 🧪 Local Setup

1. Clone the repository:

```bash
git clone https://github.com/phadkeraj/A2_Fintech-Analysis
cd A2_Fintech-Analysis
