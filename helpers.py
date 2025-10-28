import math
from zxcvbn import zxcvbn

SPECIAL_CHARACTERS = r"!@#$%^&*()-_=+[]{}|;:'\",.<>/?`~"


def shannon_entropy(password: str) -> float:
    """Calculate Shannon entropy per NIST-like approximation (bits)."""
    if not password:
        return 0.0

    # Frequency of characters
    freq = {}
    for ch in password:
        freq[ch] = freq.get(ch, 0) + 1

    entropy = 0.0
    length = len(password)
    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)

    # Total entropy bits = entropy per char * length
    return entropy * length


def zxcvbn_score(password: str) -> dict:
    """Run zxcvbn and return score dict (0-4) and feedback."""
    result = zxcvbn(password)
    return {
        'score': result['score'],
        'guesses': result.get('guesses', None),
        'crack_time_display': result.get('crack_times_display', {}).get(
            'offline_slow_hashing_1e4_per_second'
        ),
        'feedback': result.get('feedback', {})
    }
