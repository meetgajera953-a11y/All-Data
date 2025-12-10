# ---------------------------------------------
# Titanic Survival Analysis Project
# ---------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------
# 1. Loading the dataset
# ---------------------------------------------
def load_data():
    try:
        print("Loading Titanic dataset...")
        data = pd.read_csv("train.csv")   # put your file here
        print("Dataset loaded successfully!\n")
        return data
    except Exception as e:
        print("Error while loading data:", e)
        return None

# ---------------------------------------------
# 2. Basic Information About Dataset
# ---------------------------------------------
def dataset_info(df):
    print("First 5 rows of the dataset:")
    print(df.head())
    print("\nDataset Summary:")
    print(df.info())
    print("\nStatistical Description:")
    print(df.describe())

# ---------------------------------------------
# 3. Cleaning the dataset
# ---------------------------------------------
def clean_data(df):
    print("\nCleaning dataset...")
    
    df["Age"].fillna(df["Age"].median(), inplace=True)

    df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

    if "Cabin" in df.columns:
        df.drop("Cabin", axis=1, inplace=True)

    print("Cleaning Completed!\n")
    return df

# ---------------------------------------------
# 4. Survival Analysis (Core Project Logic)
# ---------------------------------------------
def survival_by_gender(df):
    print("Survival count by Gender:")
    print(df.groupby("Sex")["Survived"].mean())

    df.groupby("Sex")["Survived"].mean().plot(kind="bar")
    plt.title("Survival Rate by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Survival Rate")
    plt.show()

def survival_by_class(df):
    print("\nSurvival count by Passenger Class:")
    print(df.groupby("Pclass")["Survived"].mean())

    df.groupby("Pclass")["Survived"].mean().plot(kind="bar")
    plt.title("Survival Rate by Passenger Class")
    plt.xlabel("Class (1 = highest)")
    plt.ylabel("Survival Rate")
    plt.show()

def age_distribution(df):
    df["Age"].plot(kind="hist", bins=20)
    plt.title("Age Distribution of Passengers")
    plt.xlabel("Age")
    plt.show()

def fare_distribution(df):
    df["Fare"].plot(kind="hist", bins=20)
    plt.title("Fare Distribution")
    plt.xlabel("Fare")
    plt.show()

# ---------------------------------------------
# 5. Correlation Heatmap (Simple Version)
# ---------------------------------------------
def correlation_heatmap(df):
    print("\nGenerating correlation heatmap...")

    numeric_df = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]]
    corr = numeric_df.corr()

    plt.imshow(corr, cmap="coolwarm", interpolation="nearest")
    plt.colorbar()
    plt.title("Correlation Heatmap")
    plt.xticks(range(len(corr)), corr.columns, rotation=45)
    plt.yticks(range(len(corr)), corr.columns)
    plt.show()

# ---------------------------------------------
# 6. Main Function
# ---------------------------------------------
def main():
    df = load_data()
    if df is None:
        return

    dataset_info(df)

    df = clean_data(df)

    print("\nStarting Analysis...\n")
    survival_by_gender(df)
    survival_by_class(df)
    age_distribution(df)
    fare_distribution(df)
    correlation_heatmap(df)

    print("\nAnalysis Completed Successfully!")

# ---------------------------------------------
# Running the project
# ---------------------------------------------
if __name__ == "__main__":
    main()