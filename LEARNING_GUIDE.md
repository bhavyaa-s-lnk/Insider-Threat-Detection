# Project Learnings & Educational Guide

This document outlines the core skills and concepts demonstrated in the **Insider Threat Detection** project, as well as a roadmap for anyone looking to learn from this repository.

---

## Part 1: Your Key Learnings & Achievements

By developing this end-to-end system, you have demonstrated proficiency in several critical domains:

### 1. Cybersecurity & Anomaly Detection
- **Threat Modeling**: Understanding how normal user behavior deviates during an insider threat scenario (e.g., sudden spikes in downloads, after-hours logins).
- **Behavioral Analytics**: Applying machine learning to monitor human-centric metrics (login times, file access frequency) rather than just technical signatures.

### 2. Machine Learning Pipeline (Python, Scikit-Learn)
- **Synthetic Data Generation**: Using `pandas` and `numpy` to generate realistic, skewed datasets that simulate normal vs. anomalous user behavior (`generate_sample_data.py`).
- **Unsupervised Learning**: Implementing the **Isolation Forest** algorithmic model, which is specifically designed to isolate anomalies instead of profiling normal data points.
- **Model Serialization**: Training models and saving them using `joblib` so they can be loaded quickly in a production environment.

### 3. Backend Development (FastAPI)
- **RESTful APIs**: Structuring backend routes using FastAPI to handle cross-origin resource sharing (CORS) and serve JSON data.
- **Model Inference**: Integrating the pre-trained ML model directly into API endpoints to serve real-time anomaly scores.
- **Data Management**: Aggregating historical statistics for dashboard metrics directly from the backend.

### 4. Frontend & UI/UX Design (HTML, CSS, JavaScript)
- **Glassmorphism Design Concept**: Using advanced CSS (`backdrop-filter`, RGBA transparency) to create a premium, modern dashboard overlaying a visually striking background.
- **Asynchronous JavaScript**: Utilizing the `fetch` API to pull data from the FastAPI backend and dynamically update the DOM without page reloading.
- **Responsive Layouts**: Organizing dashboard cards and grids effectively.

---

## Part 2: How Others Can Learn From This Project

If someone wants to understand how this system works and recreate it, they should follow this step-by-step learning path:

### Step 1: Understand the Data (`generate_sample_data.py`)
- **What to study**: Learn how `pandas` creates DataFrames and how `numpy` generates random intervals and choices.
- **Actionable Task**: Read through the generation script to see how "anomalies" are intentionally injected into the dataset (e.g., multiplying download counts by 10).

### Step 2: Explore the Data (`Tutorial/explore_data.py`)
- **What to study**: Learn how to use `matplotlib` and `seaborn` to visualize data distributions.
- **Actionable Task**: Run the exploration script. Notice how the anomalous events stand out as outliers on the graphs compared to the clustered grouping of normal activities.

### Step 3: Practice the Machine Learning (`practice_exercises.py`)
- **What to study**: This file is created exactly for beginners! It contains fill-in-the-blank code exercises for loading data, initializing the Isolation Forest, and making predictions.
- **Actionable Task**: Complete the blank sections (`___`) in the practice file to get hands-on experience before looking at the production `ml/train.py` script.

### Step 4: Study the Backend (`backend/main.py`)
- **What to study**: FastAPI syntax, routing (`@app.get`), and CORS middleware.
- **Actionable Task**: Try adding a new endpoint (e.g., `/api/users/count`) that returns the total number of unique users tracked by the system.

### Step 5: Connect the Frontend (`frontend/js/dashboard.js`)
- **What to study**: How JavaScript interacts with Python. Look at how `fetch('http://127.0.0.1:8000/api/dashboard-stats')` requests data and parses it as `response.json()`.
- **Actionable Task**: Change the CSS styling in `style.css` or try rendering the fetched data into visual charts using a library like Chart.js.
