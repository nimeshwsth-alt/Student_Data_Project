# Student Performance Analysis System

A Python-based data analysis project using Pandas for cleaning, transforming, and analyzing student performance data from CSV files.

---

## Features

- Load CSV dataset
- Clean invalid or missing data
- Transform data and generate grades
- Analyze student performance
- Generate final report
- Display statistics like:
  - Average Marks
  - Highest Marks
  - Lowest Marks
  - Grade Distribution

---

## Technologies Used

- Python
- Pandas
- CSV

---

## Project Structure

```bash
Student_Data_Project/
│
├── data/
│   └── student_dataset_v2.csv
│
├── output/
│   └── cleaned_data.csv
│
├── src/
│   ├── load_data.py
│   ├── clean_data.py
│   ├── transform.py
│   ├── analyze.py
│   └── report.py
│
├── main.py
├── README.md
└── requirements.txt
```

---

## How to Run

### Step 1: Install Pandas

```bash
pip install pandas
```

### Step 2: Run the Project

```bash
python main.py
```

---

## Sample Output

```bash
STUDENT PERFORMANCE DASHBOARD

Total Students: 951
Average Marks: 69.99
Highest Marks: 99.9
Lowest Marks: 40.0
```

---

## Future Improvements

- Add data visualization graphs
- Create interactive dashboard
- Add machine learning predictions
- Export reports to PDF

---

## Author

Nimesh Awasthi
