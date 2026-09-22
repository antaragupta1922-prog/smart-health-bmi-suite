# Problem Statement
Individuals aiming to improve or monitor their personal wellness frequently lack a simple, secure tool to evaluate body metrics like Body Mass Index (BMI), Basal Metabolic Rate (BMR), and healthy weight ranges over time. Existing applications often lock user history behind accounts or present unvalidated inputs.

# Scope & Deliverables
The **Smart Health & BMI Suite** is an offline-first, modular desktop application providing secure individual tracking, validated mathematical estimation of body composition metrics, and tabular historical progress logging.

# Target Users
- Students and health-conscious individuals tracking weight trends.
- Academic evaluators looking for a clean, modular Python architecture.

# Key Features
- **User Authentication**: Secure user registration and login using SHA-256 password hashing.
- **Health Engine**: Calculates BMI, WHO category classification, BMR, and recommended healthy weight ranges.
- **Data Persistence**: Local SQLite relational database storing user entries securely.
- **Input Guardrails**: Robust validation layer catching invalid numbers, negative inputs, and out-of-range ages.