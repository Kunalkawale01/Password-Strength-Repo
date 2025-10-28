## Author
**Kunal Kawale**  
Cybersecurity Intern 

# Password-Strength-Repo
A complete GitHub-style repository to Create a Strong Password and Evaluate Its Strength . This repository contains everything needed : code to evaluate passwords, sample data, a professional report, CI workflow, and instructions.

# Password Strength Evaluation — Internship Task

**Project goal:** Create multiple passwords with varying complexity, evaluate their strength programmatically and via offline scoring (using zxcvbn + entropy), prepare a professional report with results and recommendations.

## What's included
- `scripts/evaluate_passwords.py`: Main script to evaluate passwords (scores, entropy, zxcvbn feedback).
- `scripts/generate_passwords.py`: Helper to produce sample passwords of different complexity for testing.
- `data/sample_passwords.csv`: Example passwords used for the evaluation.
- `report/Password_Strength_Report.md`: Full internship-style report with findings and recommendations ready to export to PDF.
- `assets/screenshots/`: Placeholder screenshots showing how to include online tool screenshots (for submission, replace with real screenshots).
- GitHub Actions workflow (`.github/workflows/ci.yml`) to run the evaluation on push.

## Requirements

```
pip install -r requirements.txt 
```
## requirements.txt includes:
```
zxcvbn (or zxcvbn-python)

pandas

```
How to run

Install requirements: ``` pip install -r requirements.txt ```

Run evaluation: ``` python scripts/evaluate_passwords.py --input data/sample_passwords.csv --output data/evaluation_results.csv ```

Open ``` data/evaluation_results.csv ``` and ``` report/Password_Strength_Report.md ``` for results and explanations.


