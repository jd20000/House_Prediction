# **🏡 House Price Prediction - Flask App**

## **📌 Project Overview**
This is a **Flask-based web application** that predicts house prices based on user inputs such as:
- Number of Bedrooms 🛏️
- Number of Bathrooms 🚿
- Size in Square Feet 📏
- Location 📍
- Median Income (in Lakhs ₹)

The application uses a **Machine Learning Model** trained on an open-source housing dataset (California) to provide accurate price predictions.

---

## **🚀 Installation Guide**
Follow these steps to set up the project on your local machine.

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/https://github.com/jd20000/House_Prediction/house-price-prediction.git
```


---

### **2️⃣ Navigate to the Project Directory**
```bash
cd house-price-prediction
```

---

### **3️⃣ Create a Virtual Environment (Recommended)**
A virtual environment helps isolate dependencies. Run:
```bash
python -m venv venv
```
Activate it:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

### **4️⃣ Install Dependencies**
Install the required libraries from `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### **5️⃣ Train the Model (If Not Already Trained)**
If the model file `house_price_model.pkl` is missing, run:
```bash
python model_training.py
```
This will train the model and save it inside the `model/` directory.

---

### **6️⃣ Run the Flask Application**
```bash
python app.py
```
The app will start on **http://127.0.0.1:5000/**.

If another project is running on this port, change it:
```bash
python app.py --port 5001
```

---

### **7️⃣ Open in Browser**
Go to:  
👉 **http://127.0.0.1:5000/**  

Enter house details and get the predicted price in **Indian Rupees (₹)**.

---

### **8️⃣ Deactivate Virtual Environment (When Done)**
```bash
deactivate
```

---

## **📊 Machine Learning Model Details**
### **🔹 Algorithm Used:**
We use **Linear Regression**, a simple yet effective ML algorithm for price prediction.

### **🔹 How It Works?**
- The model takes in various features like `size`, `bedrooms`, `location`, `median income`, etc.
- It learns the relationship between these features and house prices.
- When new inputs are given, it predicts the most likely price based on past data.

### **🔹 Key Features Explained:**
| Feature          | Meaning |
|-----------------|---------|
| **Median Income** | Average annual income of residents in Lakhs (₹1 Lakh = 1.0) |
| **House Age** | How old the house is (in years) 🏠 |
| **Average Rooms** | Average number of rooms per house in the area 📏 |
| **Average Occupancy** | Number of people living per house 👨‍👩‍👧‍👦 |

---

## **📜 License**
This project is **open-source**. Feel free to modify and enhance it! 🚀

---

## **💡 Contributing**
If you'd like to contribute, feel free to submit a pull request. 😊

---

## **📞 Contact**
For any queries, contact Jay - 📧 jaydeshmukh029@gmail.com

