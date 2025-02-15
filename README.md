# **Evaluation System**

## **Overview**
This project is a Django-based evaluation system that allows users to submit evaluation requests and retrieve results. It processes requests asynchronously using Celery and Redis, stores data in a PostgreSQL database, and sends email notifications via the Resend API upon completion. Additionally, a sentiment analysis task is included.

---

## **Features**
✅ **Django & PostgreSQL** – Manages evaluation requests and results in a structured database.  
✅ **REST API** – Provides endpoints for submitting requests and retrieving results.  
✅ **Celery for Asynchronous Processing** – Handles background evaluations without blocking the main app.  
✅ **Simulated Evaluation** – Generates dummy evaluation results asynchronously.  
✅ **Resend API for Email Notifications** – Sends completion emails upon task completion.  
✅ **Sentiment Analysis** – A separate task for analyzing text sentiment.  

---

## **Installation & Setup**

### **Prerequisites**
Ensure you have the following installed:  
- Python 3.12  
- PostgreSQL  
- Redis  
- Virtual environment (`venv`)  

### **1. Clone the Repository**  
```sh
git clone <repo_url>
cd evaluation_system
```

### **2. Create and Activate a Virtual Environment**  
```sh
python3 -m venv venv_eval
source venv_eval/bin/activate  # Windows: venv_eval\Scripts\activate
```

### **3. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4. Configure PostgreSQL Database**  
Update `DATABASES` in `settings.py` or use `.env`:  
```env
DATABASE_URL=postgres://postgres:<password>@localhost:5432/evaluation_db
```
Apply migrations:  
```sh
python manage.py migrate
```

### **5. Start Required Services**  
```sh
sudo service postgresql start  
redis-server
```

### **6. Run the Django Development Server**  
```sh
python manage.py runserver
```

### **7. Start Celery Worker & Beat**  
```sh
celery -A evaluation_system worker --loglevel=info
celery -A evaluation_system beat --loglevel=info  # If using periodic tasks
```

---

## **API Endpoints**  

### **1. Submit Evaluation Request**  
**Endpoint:** `POST /api/evaluate`  
**Description:** Submits an evaluation request and stores it in the database.  
**Request Body:**  
```json
{
  "input_prompt": "Evaluate the performance of a given process."
}
```
**Response:**  
```json
{
  "id": 1,
  "status": "pending"
}
```

### **2. Retrieve Evaluation Result**  
**Endpoint:** `GET /api/evaluate/<id>`  
**Description:** Fetches the status and result of an evaluation.  
**Response (Pending):**  
```json
{
  "id": 1,
  "status": "pending",
  "result": null
}
```
**Response (Completed):**  
```json
{
  "id": 1,
  "status": "completed",
  "result": "Evaluation completed. The process meets the expected performance criteria."
}
```

### **3. Sentiment Analysis Task**  
**Endpoint:** `POST /api/sentiment/analyze`  
**Request Body:**  
```json
{
  "text": "This is amazing!"
}
```
**Response:**  
```json
{
  "sentiment": "positive"
}
```

---

## **Architecture & Workflow**  

1. **User submits an evaluation request.**  
2. **Django API stores the request in the database with a "pending" status.**  
3. **Celery worker picks up the task and simulates an evaluation.**  
4. **Generated evaluation result is stored in the database, and the status is updated to "completed".**  
5. **An email notification is sent via the Resend API to inform the user.**  

---

## **Environment Variables (.env)**  
```env
DATABASE_URL=postgres://postgres:<password>@localhost:5432/evaluation_db
REDIS_URL=redis://localhost:6379/0
RESEND_API_KEY=<your_resend_api_key>
```

---



