# YouTube Sentiment Analysis using Machine Learning

An intelligent system that performs sentiment analysis on YouTube video content using machine learning techniques. Built as a final year project at SKNCOE (2022-2023) by a team of computer engineering students.

## 📝 Description
This project provides a user-friendly web application that analyzes sentiment in YouTube videos through advanced machine learning algorithms. The system processes video content using natural language processing and machine learning techniques to classify sentiments as positive, negative, or neutral. Our solution achieved an accuracy of 74.77% using Random Forest classification.

## 🔑 Key Features
- Real-time sentiment analysis of YouTube videos through URL input
- Multiple ML models comparison (Random Forest, Linear SVM, Naive Bayes, Logistic Regression)
- Clean and intuitive web interface
- Detailed sentiment analysis reports with visualization
- Support for analyzing video transcripts and comments

## 💻 Tech Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript 
- **Machine Learning**: scikit-learn, NLTK, NLP
- **APIs**: YouTube Data API, AssemblyAI API
- **Database**: SQLite
- **Other Tools**: Git, pandas, NumPy

## 📊 Model Performance
| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|---------|-----------|
| Random Forest | 0.7477 | 0.7233 | 0.45 | 0.4733 |
| Linear SVM | 0.7432 | 0.6933 | 0.4533 | 0.4700 |
| Multinomial NB | 0.7164 | 0.55 | 0.3867 | 0.3633 |
| Logistic Regression | 0.7339 | 0.6733 | 0.4 | 0.4 |

## 👥 Team Members
- Sarthak Zende (Team Lead) 
- Atharva Wadkar
- Aayush Giri
- Mujahid Hussain

## 🎯 Future Scope
- Expansion to support multiple languages
- Integration of deep learning models
- Real-time streaming analysis
- Enhanced visualization features
- Mobile application development

## 🚀 Setup and Installation
1. Clone the repository
2. Install required dependencies using `pip install -r requirements.txt`
3. Configure API keys in config.py
4. Run `python app.py`
5. Access the web interface at `localhost:5000`

## 📋 Project Guide
Prof. Suresh Shinde  
Department of Computer Engineering  
SKNCOE, Pune

---

Feel free to reach out if you have any questions or would like to contribute to the project!

