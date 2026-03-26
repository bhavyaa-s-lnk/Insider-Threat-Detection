# Insider Threat Detection System - Complete Beginner's Guide
## Part 1: Setup & Fundamentals

---

## 🎯 WHAT WE'RE BUILDING

Imagine you're a security analyst at a company. You need to spot when employees do suspicious things like:
- Logging in at 3 AM when they normally work 9-5
- Downloading 10GB of files when they usually download nothing
- Accessing HR files when they work in Engineering
- Trying to access servers they've never touched before

This system will **automatically** spot these weird behaviors and alert you.

---

## 📚 STEP 0: UNDERSTANDING THE BASICS

### What is Python?
Python is a programming language - basically, a way to tell computers what to do using English-like commands.

**Example:**
```python
# This is Python code - it's just giving instructions
print("Hello World")  # Tell computer to display text

age = 25  # Store a number
name = "John"  # Store text

if age > 18:  # Make a decision
    print(name + " is an adult")
```

### What is Machine Learning?
Instead of writing rules like "if login at 3 AM, then suspicious", we let the computer **learn patterns** from data.

**Think of it like:**
- You show the computer 1000 normal logins
- Computer learns: "OK, John logs in 9am-5pm from NYC"
- Then John logs in at 3am from Russia
- Computer says: "That's weird! Alert!"

### What are we analyzing?
**Logs** - just text files that record what users do:
```
2024-01-15 09:00:00, john.smith, login, success, NYC
2024-01-15 09:15:00, john.smith, file_access, HR_salaries.xlsx
2024-01-15 09:30:00, john.smith, download, 50MB
```

---

## 💻 STEP 1: INSTALL REQUIRED SOFTWARE

### 1.1 Install Python

**Windows:**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or newer
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Click Install

**Mac:**
1. Open Terminal (press Cmd+Space, type "Terminal")
2. Type: `brew install python3` (if you have Homebrew)
   OR download from https://www.python.org/downloads/

**Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Verify Installation:**
Open Terminal/Command Prompt and type:
```bash
python --version
```
You should see: `Python 3.11.x` or similar

### 1.2 Install a Code Editor

Download **Visual Studio Code** (it's free):
https://code.visualstudio.com/

This is where you'll write your code. It's like Microsoft Word, but for programming.

### 1.3 Create a Project Folder

**Windows:**
1. Open File Explorer
2. Create a folder: `C:\Users\YourName\insider-threat-detector`

**Mac/Linux:**
1. Open Terminal
2. Type:
```bash
mkdir ~/insider-threat-detector
cd ~/insider-threat-detector
```

### 1.4 Install Python Libraries

Open Terminal/Command Prompt in your project folder and run:

```bash
# Install data analysis tools
pip install pandas numpy

# Install machine learning tools
pip install scikit-learn

# Install visualization tools
pip install matplotlib seaborn

# Install Jupyter (interactive coding environment)
pip install jupyter notebook
```

**What these do:**
- **pandas**: Like Excel, but in code - for organizing data
- **numpy**: Math operations on large datasets
- **scikit-learn**: Machine learning algorithms
- **matplotlib/seaborn**: Create charts and graphs
- **jupyter**: Interactive coding environment (great for learning!)

---

## 📊 STEP 2: GET THE DATASET

We'll use real data from Los Alamos National Laboratory - actual anonymized logs of user behavior.

### 2.1 Download the Data

**Option 1: Direct Download (Easier)**
1. Go to: https://www.kaggle.com/datasets/markdcampbell/insider-threat-test-dataset
2. Create free Kaggle account
3. Download the dataset
4. Unzip to your project folder

**Option 2: We'll Use a Simpler Dataset First**
I'll create a small, easy-to-understand dataset for learning, then we'll move to the real one.

Create a file called `generate_sample_data.py`:

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)

# Create sample user data
users = ['john.smith', 'jane.doe', 'bob.johnson', 'alice.williams', 'charlie.brown']
departments = ['Engineering', 'HR', 'Finance', 'Sales', 'IT']
normal_hours = range(9, 18)  # 9 AM to 6 PM

# Generate 10,000 normal login events
data = []
start_date = datetime(2024, 1, 1)

for i in range(10000):
    user = random.choice(users)
    # Normal behavior: login during work hours
    hour = random.choice(normal_hours)
    timestamp = start_date + timedelta(days=random.randint(0, 30), hours=hour, minutes=random.randint(0, 59))
    
    data.append({
        'timestamp': timestamp,
        'user': user,
        'action': random.choice(['login', 'file_access', 'download']),
        'department': random.choice(departments),
        'file_size_mb': random.randint(1, 100),
        'location': 'NYC',
        'success': True
    })

# Add some ANOMALOUS behavior (insider threats)
# 1. Late night access
for i in range(50):
    data.append({
        'timestamp': start_date + timedelta(days=random.randint(0, 30), hours=random.randint(22, 4)),
        'user': 'john.smith',
        'action': 'file_access',
        'department': 'Engineering',
        'file_size_mb': random.randint(500, 2000),  # Large downloads
        'location': 'NYC',
        'success': True
    })

# 2. Access from unusual location
for i in range(30):
    data.append({
        'timestamp': start_date + timedelta(days=random.randint(0, 30), hours=random.choice(normal_hours)),
        'user': 'jane.doe',
        'action': 'login',
        'department': 'HR',
        'file_size_mb': 0,
        'location': 'Russia',  # Unusual!
        'success': True
    })

# 3. Cross-department access (HR person accessing Engineering files)
for i in range(40):
    data.append({
        'timestamp': start_date + timedelta(days=random.randint(0, 30), hours=random.choice(normal_hours)),
        'user': 'alice.williams',
        'action': 'file_access',
        'department': 'Engineering',  # She's in HR!
        'file_size_mb': random.randint(100, 500),
        'location': 'NYC',
        'success': True
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Sort by timestamp
df = df.sort_values('timestamp').reset_index(drop=True)

# Save to CSV
df.to_csv('user_activity_logs.csv', index=False)

print(f"✅ Generated {len(df)} log entries")
print(f"📁 Saved to: user_activity_logs.csv")
print("\nFirst few rows:")
print(df.head(10))
```

**Run this script:**
```bash
python generate_sample_data.py
```

You now have a file `user_activity_logs.csv` with sample data!

---

## 🔍 STEP 3: YOUR FIRST PYTHON PROGRAM

Let's write code to READ and EXPLORE the data.

Create a file called `explore_data.py`:

```python
# Import libraries (like importing tools from a toolbox)
import pandas as pd  # For working with data

# Read the CSV file
print("📂 Loading data...")
df = pd.read_csv('user_activity_logs.csv')

print("✅ Data loaded successfully!\n")

# Show basic information
print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)

# How many rows (log entries)?
print(f"Total log entries: {len(df)}")

# What columns do we have?
print(f"\nColumns: {list(df.columns)}")

# Show first 10 rows
print("\n📊 First 10 log entries:")
print(df.head(10))

# Show statistics
print("\n📈 Statistics:")
print(df.describe())

# Count actions by type
print("\n📋 Actions breakdown:")
print(df['action'].value_counts())

# Count by user
print("\n👥 Activity by user:")
print(df['user'].value_counts())

# Count by location
print("\n🌍 Activity by location:")
print(df['location'].value_counts())
```

**Run it:**
```bash
python explore_data.py
```

---

## 🎓 UNDERSTANDING THE CODE

Let's break down what each part does:

```python
import pandas as pd
```
**Translation:** "Hey Python, I need to use the pandas tool"

```python
df = pd.read_csv('user_activity_logs.csv')
```
**Translation:** "Read the CSV file and put it in a variable called 'df' (short for DataFrame)"

```python
print(df.head(10))
```
**Translation:** "Show me the first 10 rows of data"

```python
df['action'].value_counts()
```
**Translation:** "Count how many times each action appears"

---

## 🎯 STEP 4: INTERACTIVE LEARNING WITH JUPYTER

Jupyter Notebook lets you write code AND see results immediately. Great for learning!

**Start Jupyter:**
```bash
jupyter notebook
```

This opens in your browser. Click "New" → "Python 3"

**Try these commands one by one:**

```python
# Cell 1: Import and load data
import pandas as pd
df = pd.read_csv('user_activity_logs.csv')
```

```python
# Cell 2: See the data
df.head()
```

```python
# Cell 3: Filter data - show only John's activities
df[df['user'] == 'john.smith']
```

```python
# Cell 4: Find large downloads
df[df['file_size_mb'] > 500]
```

```python
# Cell 5: Find unusual locations
df[df['location'] != 'NYC']
```

**Each cell runs independently!** This is perfect for experimenting.

---

## 📝 HOMEWORK / PRACTICE

Before moving to Part 2, try these exercises:

### Exercise 1: Filter Data
Write code to find:
1. All logins by 'jane.doe'
2. All downloads larger than 1000 MB
3. All activities from 'Russia'

### Exercise 2: Calculate Statistics
Write code to:
1. Find the average file size downloaded per user
2. Count how many times each user logged in
3. Find the user with the most activities

### Exercise 3: Time Analysis
Write code to:
1. Convert timestamp to datetime format
2. Extract the hour from timestamps
3. Find all activities that happened between 10 PM and 6 AM

**Solutions:**

```python
# Exercise 1
jane_logins = df[(df['user'] == 'jane.doe') & (df['action'] == 'login')]
large_downloads = df[df['file_size_mb'] > 1000]
russia_activity = df[df['location'] == 'Russia']

# Exercise 2
avg_by_user = df.groupby('user')['file_size_mb'].mean()
login_counts = df[df['action'] == 'login'].groupby('user').size()
most_active = df['user'].value_counts().iloc[0]

# Exercise 3
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
night_activity = df[(df['hour'] >= 22) | (df['hour'] <= 6)]
```

---

## ✅ CHECKPOINT

By now, you should:
- ✅ Have Python installed
- ✅ Have VS Code installed
- ✅ Created a project folder
- ✅ Installed required libraries
- ✅ Generated sample data
- ✅ Written your first Python script
- ✅ Understand how to read and filter data

---

## 🎯 WHAT'S NEXT?

In **Part 2**, we'll:
1. Create visualizations (charts/graphs)
2. Engineer features (create new useful columns)
3. Build our first machine learning model
4. Detect anomalies automatically

**Ready to continue?** Let me know and I'll create Part 2!

---

## 🆘 COMMON ERRORS & FIXES

### "Python not found"
**Fix:** Make sure you checked "Add to PATH" during installation. Reinstall Python if needed.

### "No module named pandas"
**Fix:** Run `pip install pandas` again

### "Permission denied"
**Fix (Windows):** Run Command Prompt as Administrator
**Fix (Mac/Linux):** Use `sudo pip install pandas`

### "CSV file not found"
**Fix:** Make sure you're in the right folder. Run `pwd` (Mac/Linux) or `cd` (Windows) to check.

---

## 📚 LEARNING RESOURCES

**If you want to learn Python basics:**
- Python.org tutorial: https://docs.python.org/3/tutorial/
- Codecademy Python: https://www.codecademy.com/learn/learn-python-3
- Real Python: https://realpython.com/

**For pandas (data analysis):**
- 10 minutes to pandas: https://pandas.pydata.org/docs/user_guide/10min.html

**For machine learning:**
- scikit-learn tutorial: https://scikit-learn.org/stable/tutorial/

---

## 💪 YOU GOT THIS!

Learning to code seems hard at first, but it's like learning a new language. You won't understand everything immediately, and **that's OK**!

**Pro tips:**
- Type the code yourself (don't copy-paste) - you learn by doing
- Break things! Experiment! That's how you learn
- Google errors - every programmer does this daily
- Take breaks - your brain needs time to process

**Questions?** I'm here to help! Tell me:
- What didn't make sense?
- Where did you get stuck?
- What do you want more explanation on?

Let me know when you're ready for Part 2! 🚀
