"""
Insider Threat Detection System - Data Generator
This script creates sample user activity logs for training

Author: Your Name
Date: 2024
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed so results are reproducible
np.random.seed(42)
random.seed(42)

print("🔧 Generating sample user activity data...")
print("=" * 60)

# Define our fake company
users = ['john.smith', 'jane.doe', 'bob.johnson', 'alice.williams', 'charlie.brown']
departments = {
    'john.smith': 'Engineering',
    'jane.doe': 'HR', 
    'bob.johnson': 'Finance',
    'alice.williams': 'HR',
    'charlie.brown': 'IT'
}

locations = ['NYC', 'San Francisco', 'London']
normal_work_hours = list(range(9, 18))  # 9 AM to 6 PM

# Start date for logs
start_date = datetime(2024, 1, 1)

data = []

print("📝 Generating normal behavior patterns...")

# Generate 10,000 NORMAL log entries
for i in range(10000):
    user = random.choice(users)
    dept = departments[user]
    
    # Normal behavior characteristics:
    # - Login during work hours
    # - Access files from own department
    # - Normal file sizes (1-100 MB)
    # - From known locations
    
    hour = random.choice(normal_work_hours)
    timestamp = start_date + timedelta(
        days=random.randint(0, 30),
        hours=hour,
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59)
    )
    
    action = random.choice(['login', 'file_access', 'email_sent', 'download'])
    
    data.append({
        'timestamp': timestamp,
        'user': user,
        'action': action,
        'department_accessed': dept,  # Same as user's dept
        'file_size_mb': random.randint(1, 100) if action == 'download' else 0,
        'location': random.choice(locations),
        'device': f"laptop_{random.randint(1, 3)}",
        'success': True,
        'is_anomaly': False
    })

print(f"   ✅ Generated {len(data)} normal activities")

# Now add ANOMALOUS behavior (insider threats)
print("\n🚨 Injecting anomalous behavior...")

# ANOMALY 1: Late-night large downloads (john.smith)
print("   → Adding late-night large downloads...")
for i in range(50):
    hour = random.choice(list(range(22, 24)) + list(range(0, 6)))
    timestamp = start_date + timedelta(
        days=random.randint(15, 30),  # Last 2 weeks
        hours=hour,
        minutes=random.randint(0, 59)
    )
    
    data.append({
        'timestamp': timestamp,
        'user': 'john.smith',
        'action': 'download',
        'department_accessed': 'Engineering',
        'file_size_mb': random.randint(500, 2000),  # HUGE downloads!
        'location': 'NYC',
        'device': 'laptop_1',
        'success': True,
        'is_anomaly': True
    })

print(f"      ✅ Added 50 suspicious late-night downloads")

# ANOMALY 2: Logins from unusual location (jane.doe)
print("   → Adding logins from unusual locations...")
for i in range(30):
    hour = random.choice(normal_work_hours)
    timestamp = start_date + timedelta(
        days=random.randint(15, 30),
        hours=hour,
        minutes=random.randint(0, 59)
    )
    
    data.append({
        'timestamp': timestamp,
        'user': 'jane.doe',
        'action': 'login',
        'department_accessed': 'HR',
        'file_size_mb': 0,
        'location': 'Moscow',  # UNUSUAL!
        'device': 'unknown_device',
        'success': True,
        'is_anomaly': True
    })

print(f"      ✅ Added 30 logins from suspicious location")

# ANOMALY 3: Cross-department file access (alice.williams - HR accessing Engineering files)
print("   → Adding unauthorized cross-department access...")
for i in range(40):
    hour = random.choice(normal_work_hours)
    timestamp = start_date + timedelta(
        days=random.randint(10, 30),
        hours=hour,
        minutes=random.randint(0, 59)
    )
    
    data.append({
        'timestamp': timestamp,
        'user': 'alice.williams',
        'action': 'file_access',
        'department_accessed': 'Engineering',  # She's in HR!
        'file_size_mb': random.randint(100, 500),
        'location': 'NYC',
        'device': 'laptop_2',
        'success': True,
        'is_anomaly': True
    })

print(f"      ✅ Added 40 unauthorized department accesses")

# ANOMALY 4: Multiple failed login attempts (bob.johnson)
print("   → Adding brute force login attempts...")
for i in range(25):
    hour = random.choice(normal_work_hours)
    timestamp = start_date + timedelta(
        days=random.randint(20, 30),
        hours=hour,
        minutes=random.randint(0, 59)
    )
    
    data.append({
        'timestamp': timestamp,
        'user': 'bob.johnson',
        'action': 'login',
        'department_accessed': 'Finance',
        'file_size_mb': 0,
        'location': 'San Francisco',
        'device': 'laptop_1',
        'success': False,  # FAILED attempts
        'is_anomaly': True
    })

print(f"      ✅ Added 25 failed login attempts")

print("\n" + "=" * 60)
print(f"📊 TOTAL EVENTS GENERATED: {len(data)}")

# Convert to DataFrame
df = pd.DataFrame(data)

# Sort by timestamp
df = df.sort_values('timestamp').reset_index(drop=True)

# Add some derived features
df['hour'] = df['timestamp'].apply(lambda x: x.hour)
df['day_of_week'] = df['timestamp'].apply(lambda x: x.strftime('%A'))
df['is_weekend'] = df['timestamp'].apply(lambda x: x.weekday() >= 5)
df['is_night'] = df['hour'].apply(lambda x: x >= 22 or x <= 6)

# Save to CSV
output_file = 'user_activity_logs.csv'
df.to_csv(output_file, index=False)

print(f"💾 Saved to: {output_file}")
print("\n" + "=" * 60)
print("📈 DATASET STATISTICS:")
print("=" * 60)

print(f"\nTotal log entries: {len(df):,}")
print(f"Normal activities: {len(df[df['is_anomaly'] == False]):,}")
print(f"Anomalous activities: {len(df[df['is_anomaly'] == True]):,}")
print(f"Anomaly rate: {(df['is_anomaly'].sum() / len(df) * 100):.2f}%")

print("\n📋 Activities by type:")
print(df['action'].value_counts())

print("\n👥 Activities by user:")
print(df['user'].value_counts())

print("\n🌍 Activities by location:")
print(df['location'].value_counts())

print("\n⏰ Activities by hour of day:")
print(df['hour'].value_counts().sort_index())

print("\n" + "=" * 60)
print("✅ DATA GENERATION COMPLETE!")
print("=" * 60)
print("\nNext steps:")
print("1. Run: python explore_data.py")
print("2. Or open Jupyter: jupyter notebook")
print("3. Start analyzing the data!")
