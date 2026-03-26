"""
PRACTICE EXERCISES - Learn Python for Insider Threat Detection

Complete these exercises to learn Python basics before moving to Part 2.
Each exercise builds on the previous one.

Instructions:
1. Read each exercise
2. Try to solve it yourself first
3. Check the solution at the bottom
4. Experiment and modify the code!
"""

import pandas as pd

# Load the data first
df = pd.read_csv('user_activity_logs.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])

print("=" * 60)
print("🎓 PYTHON PRACTICE EXERCISES")
print("=" * 60)
print("\nData loaded! Let's practice...\n")

# ============================================================
# BEGINNER EXERCISES
# ============================================================

print("=" * 60)
print("📚 BEGINNER LEVEL")
print("=" * 60)

# EXERCISE 1: Print specific information
print("\n📝 Exercise 1: Display Information")
print("-" * 40)
print("Task: Print the total number of rows in the dataset")
print("Hint: Use len(df)")

# YOUR CODE HERE:
# answer = 

print(f"\n✅ Check your answer (uncomment to see):")
# print(f"Total rows: {len(df)}")


# EXERCISE 2: Select specific columns
print("\n📝 Exercise 2: Select Columns")
print("-" * 40)
print("Task: Create a new DataFrame with only 'user' and 'action' columns")
print("Hint: df[['column1', 'column2']]")

# YOUR CODE HERE:
# user_actions = 

print("\n✅ Solution:")
# user_actions = df[['user', 'action']]
# print(user_actions.head())


# EXERCISE 3: Filter rows
print("\n📝 Exercise 3: Filter Data")
print("-" * 40)
print("Task: Find all rows where user is 'john.smith'")
print("Hint: df[df['column'] == 'value']")

# YOUR CODE HERE:
# john_activities = 

print("\n✅ Solution:")
# john_activities = df[df['user'] == 'john.smith']
# print(f"John has {len(john_activities)} activities")


# ============================================================
# INTERMEDIATE EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("🎯 INTERMEDIATE LEVEL")
print("=" * 60)

# EXERCISE 4: Multiple conditions
print("\n📝 Exercise 4: Complex Filtering")
print("-" * 40)
print("Task: Find all downloads larger than 1000 MB")
print("Hint: Use & for AND, | for OR")

# YOUR CODE HERE:
# large_downloads = 

print("\n✅ Solution:")
# large_downloads = df[(df['action'] == 'download') & (df['file_size_mb'] > 1000)]
# print(f"Found {len(large_downloads)} large downloads")
# print(large_downloads[['user', 'file_size_mb', 'timestamp']].head())


# EXERCISE 5: Grouping and aggregation
print("\n📝 Exercise 5: Calculate Averages")
print("-" * 40)
print("Task: Calculate average file size per user")
print("Hint: df.groupby('column')['value_column'].mean()")

# YOUR CODE HERE:
# avg_file_size = 

print("\n✅ Solution:")
# avg_file_size = df.groupby('user')['file_size_mb'].mean()
# print(avg_file_size)


# EXERCISE 6: Count occurrences
print("\n📝 Exercise 6: Count Activities")
print("-" * 40)
print("Task: Count how many logins each user has")
print("Hint: Filter for logins first, then use value_counts()")

# YOUR CODE HERE:
# login_counts = 

print("\n✅ Solution:")
# logins = df[df['action'] == 'login']
# login_counts = logins['user'].value_counts()
# print(login_counts)


# ============================================================
# ADVANCED EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("🚀 ADVANCED LEVEL")
print("=" * 60)

# EXERCISE 7: Time-based filtering
print("\n📝 Exercise 7: Night Activity Detection")
print("-" * 40)
print("Task: Find all activities that happened between 10 PM (22) and 6 AM")
print("Hint: Extract hour from timestamp, then filter")

# YOUR CODE HERE:
# df['hour'] = 
# night_activity = 

print("\n✅ Solution:")
# df['hour'] = df['timestamp'].dt.hour
# night_activity = df[(df['hour'] >= 22) | (df['hour'] <= 6)]
# print(f"Found {len(night_activity)} night activities")
# print(night_activity[['user', 'hour', 'action']].head())


# EXERCISE 8: Create new columns
print("\n📝 Exercise 8: Feature Engineering")
print("-" * 40)
print("Task: Create a new column 'is_large_download' (True if >500 MB)")
print("Hint: df['new_column'] = df['existing_column'] > threshold")

# YOUR CODE HERE:
# df['is_large_download'] = 

print("\n✅ Solution:")
# df['is_large_download'] = df['file_size_mb'] > 500
# print(f"Large downloads: {df['is_large_download'].sum()}")


# EXERCISE 9: Multiple aggregations
print("\n📝 Exercise 9: User Statistics")
print("-" * 40)
print("Task: For each user, calculate total activities, avg file size, and max file size")
print("Hint: .agg(['count', 'mean', 'max'])")

# YOUR CODE HERE:
# user_stats = 

print("\n✅ Solution:")
# user_stats = df.groupby('user')['file_size_mb'].agg(['count', 'mean', 'max'])
# print(user_stats)


# EXERCISE 10: Suspicious activity detector
print("\n📝 Exercise 10: Build a Simple Threat Detector")
print("-" * 40)
print("Task: Find users who have:")
print("  1. More than 5 night activities")
print("  2. OR downloaded more than 5000 MB total")

# YOUR CODE HERE:
# Step 1: Count night activities per user
# night_counts = 

# Step 2: Calculate total downloads per user
# total_downloads = 

# Step 3: Find suspicious users
# suspicious_users = 

print("\n✅ Solution:")
# df['hour'] = df['timestamp'].dt.hour
# df['is_night'] = (df['hour'] >= 22) | (df['hour'] <= 6)
# 
# night_counts = df[df['is_night']].groupby('user').size()
# total_downloads = df.groupby('user')['file_size_mb'].sum()
# 
# suspicious_night = night_counts[night_counts > 5].index.tolist()
# suspicious_download = total_downloads[total_downloads > 5000].index.tolist()
# suspicious_users = list(set(suspicious_night + suspicious_download))
# 
# print(f"\n🚨 Suspicious users detected: {suspicious_users}")
# for user in suspicious_users:
#     print(f"\n{user}:")
#     if user in suspicious_night:
#         print(f"  - {night_counts[user]} night activities")
#     if user in suspicious_download:
#         print(f"  - {total_downloads[user]:.0f} MB total downloaded")


# ============================================================
# CHALLENGE EXERCISES
# ============================================================

print("\n" + "=" * 60)
print("💪 CHALLENGE EXERCISES")
print("=" * 60)

# CHALLENGE 1: Unusual location detector
print("\n📝 Challenge 1: Location Anomaly Detection")
print("-" * 40)
print("Task: For each user, find their most common location.")
print("Then find activities from OTHER locations (potentially suspicious)")

# YOUR CODE HERE:


# CHALLENGE 2: Failed login pattern detector
print("\n📝 Challenge 2: Brute Force Detection")
print("-" * 40)
print("Task: Find users with more than 3 failed login attempts in a single day")
print("Hint: Use df['timestamp'].dt.date to group by date")

# YOUR CODE HERE:


# CHALLENGE 3: Cross-department access detector
print("\n📝 Challenge 3: Unauthorized Access Detection")
print("-" * 40)
print("Task: Find users accessing departments different from their normal pattern")
print("Hint: Find each user's most common department, then find exceptions")

# YOUR CODE HERE:


# ============================================================
# COMPLETED ALL EXERCISES?
# ============================================================

print("\n" + "=" * 60)
print("🎉 EXERCISE SUMMARY")
print("=" * 60)

print("""
If you completed all exercises, you now know:

✅ How to load data with pandas
✅ How to filter and select data
✅ How to use conditions (and, or)
✅ How to group and aggregate data
✅ How to create new columns
✅ How to work with timestamps
✅ How to detect patterns in data

These are the EXACT skills needed for building
the Insider Threat Detection System!

🎯 Next Steps:
1. Make sure all exercises run without errors
2. Experiment with the code - change values, try different filters
3. When ready, move to Part 2: Visualization and Machine Learning

Ready? Run: python visualize_data.py
""")

print("=" * 60)

# ============================================================
# SOLUTIONS (Run this to check all solutions)
# ============================================================

def show_all_solutions():
    """
    Uncomment this function call at the bottom to see all solutions
    """
    print("\n" + "=" * 60)
    print("📖 ALL SOLUTIONS")
    print("=" * 60)
    
    # Exercise 1
    print(f"\n1. Total rows: {len(df)}")
    
    # Exercise 2
    user_actions = df[['user', 'action']]
    print(f"\n2. User actions DataFrame created with {len(user_actions)} rows")
    
    # Exercise 3
    john = df[df['user'] == 'john.smith']
    print(f"\n3. John has {len(john)} activities")
    
    # Exercise 4
    large = df[(df['action'] == 'download') & (df['file_size_mb'] > 1000)]
    print(f"\n4. Found {len(large)} large downloads")
    
    # Exercise 5
    avg = df.groupby('user')['file_size_mb'].mean()
    print(f"\n5. Average file sizes per user:")
    print(avg)
    
    # Exercise 6
    logins = df[df['action'] == 'login']
    counts = logins['user'].value_counts()
    print(f"\n6. Login counts:")
    print(counts)
    
    # Exercise 7
    df['hour'] = df['timestamp'].dt.hour
    night = df[(df['hour'] >= 22) | (df['hour'] <= 6)]
    print(f"\n7. Night activities: {len(night)}")
    
    # Exercise 8
    df['is_large_download'] = df['file_size_mb'] > 500
    print(f"\n8. Large downloads: {df['is_large_download'].sum()}")
    
    # Exercise 9
    stats = df.groupby('user')['file_size_mb'].agg(['count', 'mean', 'max'])
    print(f"\n9. User statistics:")
    print(stats)
    
    # Exercise 10
    df['is_night'] = (df['hour'] >= 22) | (df['hour'] <= 6)
    night_counts = df[df['is_night']].groupby('user').size()
    total_downloads = df.groupby('user')['file_size_mb'].sum()
    
    suspicious_night = night_counts[night_counts > 5].index.tolist()
    suspicious_download = total_downloads[total_downloads > 5000].index.tolist()
    suspicious_users = list(set(suspicious_night + suspicious_download))
    
    print(f"\n10. Suspicious users: {suspicious_users}")

# Uncomment to see all solutions:
# show_all_solutions()
