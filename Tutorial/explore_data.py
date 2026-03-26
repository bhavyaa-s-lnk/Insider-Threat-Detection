"""
Insider Threat Detection System - Data Explorer
This script helps you explore and understand the user activity data

Author: Your Name
Date: 2024
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for prettier plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("=" * 60)
print("📂 LOADING DATA...")
print("=" * 60)

# Read the CSV file
df = pd.read_csv('user_activity_logs.csv')

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

print("✅ Data loaded successfully!\n")

# ============================================================
# BASIC INFORMATION
# ============================================================

print("=" * 60)
print("📊 DATASET OVERVIEW")
print("=" * 60)

print(f"\nTotal log entries: {len(df):,}")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Number of users: {df['user'].nunique()}")
print(f"Number of unique locations: {df['location'].nunique()}")

print("\n📋 Column information:")
print(df.info())

print("\n" + "=" * 60)
print("👀 FIRST 10 LOG ENTRIES")
print("=" * 60)
print(df.head(10))

# ============================================================
# STATISTICS
# ============================================================

print("\n" + "=" * 60)
print("📈 NUMERICAL STATISTICS")
print("=" * 60)
print(df[['file_size_mb', 'hour']].describe())

# ============================================================
# BREAKDOWNS
# ============================================================

print("\n" + "=" * 60)
print("📋 ACTIVITY BREAKDOWN")
print("=" * 60)

print("\n🎯 Actions:")
print(df['action'].value_counts())
print(f"\nMost common action: {df['action'].value_counts().index[0]}")

print("\n👥 Users:")
user_counts = df['user'].value_counts()
print(user_counts)
print(f"\nMost active user: {user_counts.index[0]} ({user_counts.iloc[0]} activities)")

print("\n🌍 Locations:")
print(df['location'].value_counts())

print("\n🏢 Departments accessed:")
print(df['department_accessed'].value_counts())

print("\n⏰ Hour of day:")
hour_counts = df['hour'].value_counts().sort_index()
print(hour_counts)

# ============================================================
# ANOMALY DETECTION (we already know which are anomalous)
# ============================================================

print("\n" + "=" * 60)
print("🚨 ANOMALY ANALYSIS")
print("=" * 60)

anomalies = df[df['is_anomaly'] == True]
print(f"\nTotal anomalies: {len(anomalies)}")
print(f"Anomaly rate: {(len(anomalies) / len(df) * 100):.2f}%")

print("\n🔍 Anomalies by user:")
print(anomalies['user'].value_counts())

print("\n🔍 Anomalies by type:")
print(anomalies['action'].value_counts())

# ============================================================
# IDENTIFY SUSPICIOUS PATTERNS (without using the label)
# ============================================================

print("\n" + "=" * 60)
print("🕵️ SUSPICIOUS PATTERNS DETECTED")
print("=" * 60)

# Pattern 1: Large downloads
large_downloads = df[df['file_size_mb'] > 500]
print(f"\n⚠️  Large downloads (>500 MB): {len(large_downloads)}")
if len(large_downloads) > 0:
    print("Top offenders:")
    print(large_downloads.groupby('user')['file_size_mb'].agg(['count', 'mean', 'max']))

# Pattern 2: Night activity
night_activity = df[df['is_night'] == True]
print(f"\n🌙 Night activity (10 PM - 6 AM): {len(night_activity)}")
if len(night_activity) > 0:
    print("Users with night activity:")
    print(night_activity['user'].value_counts())

# Pattern 3: Unusual locations
common_locations = df['location'].value_counts().index[:3]
unusual_locations = df[~df['location'].isin(common_locations)]
print(f"\n🌐 Activity from unusual locations: {len(unusual_locations)}")
if len(unusual_locations) > 0:
    print(unusual_locations[['user', 'location', 'timestamp']].head(10))

# Pattern 4: Failed logins
failed_logins = df[df['success'] == False]
print(f"\n❌ Failed login attempts: {len(failed_logins)}")
if len(failed_logins) > 0:
    print("Users with failed logins:")
    print(failed_logins['user'].value_counts())

# Pattern 5: Cross-department access
print("\n🔐 Potential unauthorized access:")
for user in df['user'].unique():
    user_dept = df[df['user'] == user]['department_accessed'].mode()
    if len(user_dept) > 0:
        user_dept = user_dept[0]
        other_dept_access = df[(df['user'] == user) & (df['department_accessed'] != user_dept)]
        if len(other_dept_access) > 0:
            print(f"   {user}: {len(other_dept_access)} accesses to other departments")

# ============================================================
# USER PROFILES
# ============================================================

print("\n" + "=" * 60)
print("👤 USER BEHAVIOR PROFILES")
print("=" * 60)

for user in df['user'].unique():
    user_data = df[df['user'] == user]
    anomaly_count = user_data['is_anomaly'].sum()
    
    print(f"\n{user}:")
    print(f"  Total activities: {len(user_data)}")
    print(f"  Anomalies: {anomaly_count} ({anomaly_count/len(user_data)*100:.1f}%)")
    print(f"  Most common action: {user_data['action'].mode()[0]}")
    print(f"  Avg file size: {user_data['file_size_mb'].mean():.1f} MB")
    print(f"  Most common location: {user_data['location'].mode()[0]}")
    print(f"  Typical hours: {user_data['hour'].min()}-{user_data['hour'].max()}")
    
    if anomaly_count > 0:
        print(f"  ⚠️  WARNING: {anomaly_count} suspicious activities detected!")

# ============================================================
# RECOMMENDATIONS
# ============================================================

print("\n" + "=" * 60)
print("💡 ANALYSIS COMPLETE - NEXT STEPS")
print("=" * 60)

print("\n🎯 Detected Issues:")
issues = []

if len(large_downloads) > 0:
    issues.append(f"• {len(large_downloads)} unusually large downloads")
    
if len(night_activity) > 0:
    issues.append(f"• {len(night_activity)} activities during non-work hours")
    
if len(unusual_locations) > 0:
    issues.append(f"• {len(unusual_locations)} logins from unusual locations")
    
if len(failed_logins) > 0:
    issues.append(f"• {len(failed_logins)} failed login attempts")

for issue in issues:
    print(issue)

print("\n📚 Ready for next phase:")
print("1. ✅ Data loaded and explored")
print("2. ⏭️  Next: Create visualizations (run: python visualize_data.py)")
print("3. ⏭️  Then: Build machine learning model")

print("\n" + "=" * 60)
