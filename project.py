import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('student_habits_performance.csv')
# print(df.head(2))
print(df.columns.tolist)
# df=df.dropna()
# print(df.isnull().sum())
# print(df.info())
# print(df.describe(include='object'))
categorical_cols=['gender','part_time_job','diet_quality','parental_education_level','internet_quality','extracurricular_participation']
for col in categorical_cols:
    print(f"value counts for {col}: \n {df[col].value_counts()}")
df.hist(bins=30,edgecolor='black')
plt.tight_layout()
plt.show()

for col in categorical_cols:
    count=df[col].value_counts()
    plt.bar(count.index,count.values)
    plt.title(f"Distribution of {col}")
    plt.xticks(rotation=45)
    plt.show()

num_features=['age','study_hours_per_day','social_media_hours','netflix_hours','attendance_percentage','sleep_hours','exercise_frequency','mental_health_rating','exam_score']
for feature in num_features[:-1]:
    plt.scatter(df[feature],df['exam_score'])
    plt.title(f"{feature} vs Exam Score")
    plt.xlabel(feature)
    plt.ylabel('Exam Score')
    plt.show()