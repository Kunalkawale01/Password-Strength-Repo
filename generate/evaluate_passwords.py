# Simple generator for sample passwords used in internship evaluation

sample_passwords = [
    'kunal123',
    'Kunal@123',
    'Kunal@2025!',
    'Dh@rm@_Flame99',
    '!T@thv@ya#2025_Fl@meWithin',
]


if __name__ == '__main__':
    import csv
    from pathlib import Path

    out = Path('data/sample_passwords.csv')
    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['password', 'description'])
        for p in sample_passwords:
            writer.writerow([p, 'sample'])

    print(f' Wrote {out.resolve()}')


# Evaluate passwords from a CSV with columns: password,description
# Outputs CSV with columns: password,description,length,entropy,zxcvbn_score,zxcvbn_feedback,guesses,crack_time

import csv
import argparse
from pathlib import Path
from helpers import shannon_entropy, zxcvbn_score


def evaluate(input_csv: Path, output_csv: Path):
    rows = []
    # Read the input CSV
    with input_csv.open(newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            pwd = r['password']
            desc = r.get('description', '')
            length = len(pwd)
            entropy = shannon_entropy(pwd)
            z = zxcvbn_score(pwd)

            rows.append({
                'password': pwd,
                'description': desc,
                'length': length,
                'entropy_bits': round(entropy, 2),
                'zxcvbn_score': z['score'],
                'zxcvbn_feedback': str(z.get('feedback')),
                'guesses': z.get('guesses'),
                'crack_time': z.get('crack_time_display')
            })

    # Write the output CSV (properly indented)
    fieldnames = [
        'password', 'description', 'length',
        'entropy_bits', 'zxcvbn_score', 'zxcvbn_feedback',
        'guesses', 'crack_time'
    ]
    with output_csv.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Evaluate password strength using entropy and zxcvbn.")
    parser.add_argument("input_csv", type=Path, help="Path to input CSV file with passwords.")
    parser.add_argument("output_csv", type=Path, help="Path to output CSV file for results.")
    args = parser.parse_args()

    evaluate(args.input_csv, args.output_csv)
    print(f" Evaluation completed. Results saved to: {args.output_csv}")


if __name__ == "__main__":
    main()
