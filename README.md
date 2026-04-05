🏙 AI-Powered Urban Problem Reporter 🚧
📌 Overview

This project is an AI-based web application that allows users to report urban issues such as potholes and garbage by uploading images. The system uses deep learning (CNN) to automatically detect the issue, assign priority, and store it in a database for further action. It also provides an admin dashboard and analytics for monitoring and decision-making.

🚀 Features
🤖 AI Image Classification
Detects potholes and garbage using a CNN model
⚠️ Priority Assignment
Automatically assigns priority (High/Medium) based on issue type
📊 Severity Detection
Uses image processing to estimate severity (Low / Moderate / Severe)
🗄 Database Integration
Stores complaints with image, issue type, priority, and status
🖥 Admin Dashboard
View all complaints in a structured table
See uploaded images
Track complaint status
✅ Status Management
Update complaint status from Pending → Resolved
📈 Analytics Dashboard
Visual representation of complaint distribution using graphs
🎨 User-Friendly UI
Styled interface with improved user experience
🧠 AI Concepts Used
Convolutional Neural Networks (CNN)
Image Preprocessing (Resizing, Normalization)
Data Augmentation
Supervised Learning
Softmax Classification
Feature Extraction
Overfitting Prevention (Dropout)
Heuristic-based Severity Detection
🛠 Tech Stack
Frontend: HTML, CSS
Backend: Python (Flask)
Database: SQLite
AI/ML: TensorFlow, Keras, OpenCV
Visualization: Chart.js
📂 Project Structure
urban_ai_project/
│
├── app.py
├── predict.py
├── train_model.py
├── database.db
│
├── dataset/
│   ├── pothole/
│   └── garbage/
│
├── static/
│   └── uploads/
│
├── templates/
│   ├── index.html
│   ├── admin.html
│   └── analytics.html
⚙️ How to Run
Clone the repository

Install dependencies:

pip install flask tensorflow opencv-python numpy pandas scikit-learn pillow scipy

Train the model:

python train_model.py

Run the application:

python app.py

Open in browser:

http://127.0.0.1:5000/
🎯 Future Improvements
📍 Location/GPS integration
🔐 User authentication system
📱 Mobile-friendly UI
☁️ Deployment on cloud
🧠 Advanced AI models (CNN + LSTM)
👨‍💻 Author

Daksh Aryan
B.Tech Student
