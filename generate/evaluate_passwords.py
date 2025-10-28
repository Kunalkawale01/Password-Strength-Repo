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
with out.open('w', newline='') as f:
writer = csv.writer(f)
writer.writerow(['password', 'description'])
for p in sample_passwords:
writer.writerow([p, 'sample'])
print(f'Wrote {out}')


# Evaluate passwords from a CSV with columns: password,description
# Outputs CSV with columns: password,description,length,entropy,zxcvbn_score,zxcvbn_feedback,guesses,crack_time

import csv
import argparse
from pathlib import Path
from helpers import shannon_entropy, zxcvbn_score

def evaluate(input_csv: Path, output_csv: Path):
rows = []
with input_csv.open(newline='') as f:
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

output_csv.parent.mkdir(parents=True, exist_ok=True)
with output_csv.open('w', newline='') as f:
fieldnames = ['password','description','length','entropy_bits','zxcvbn_score','zxcvbn_feedback','guesses','crack_time']
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
for row in rows:
writer.writerow(row)
print(f'Results written to {output_csv}')

if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', default='data/sample_passwords.csv')
parser.add_argument('--output', '-o', default='data/evaluation_results.csv')
args = parser.parse_args()
evaluate(Path(args.input), Path(args.output))
