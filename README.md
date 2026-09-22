# Smart Health & BMI Suite

An architectural, multi-module Python application for monitoring physical metrics including Body Mass Index (BMI), Basal Metabolic Rate (BMR), and healthy weight targets.

## Features
- **User Authentication**: Multi-user support with SHA-256 encrypted password persistence.
- **Health Metrics Calculation**: Implements standard BMI formulas and Mifflin-St Jeor equation for BMR.
- **Input Validation**: Custom validation layer protecting against unexpected inputs or negative numbers.
- **Data Analytics & Reports**: Tabular history visualization powered by SQLite.

## Project Structure
```text
bmi_health_suite/
├── src/            # Core business logic modules
├── tests/          # Unit test suites (PyTest)
├── main.py         # Application entry point
├── requirements.txt
├── statement.md
└── README.md