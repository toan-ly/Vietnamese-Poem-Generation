# Vietnamese Poem Generator

This project generates Vietnamese poetry using deep learning models, trained on data collected from [Thi Viện](https://www.thivien.net/). It supports:
- **Thơ Ngũ Ngôn (5-syllable verse)**
- **Thơ Lục Bát (6-8 verse)**


## **Getting Started**  

### 1. Clone the repo  
```bash
git clone https://github.com/toan-ly/Vietnamese-Poem-Generation.git
cd Vietnamese-Poem-Generation
```

### 2. Install dependencies
```bash
pip install streamlit transformers
```

### 3. Crawl data
Run web scraping scripts in `notebooks/data_crawl_5.ipynb` for **Ngũ Ngôn poetry (5-syllable verse)** and `notebooks/data_crawl_68.ipynb` for **Lục Bát poetry (6-8 verse)**

### 4. Train models
All model training scripts are also in `notebooks/`

### 5. Run streamlit app
```bash
streamlit run app.py
```

