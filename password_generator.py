#!/usr/bin/env python3
"""
Password Generator CLI.

Generates a random password using a mix of uppercase letters, lowercase letters,
digits, and symbols.
"""
import argparse
import string
import secrets
import sys

def generate_password(
    length: int,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    pool = ''
    if use_upper:
        pool += string.ascii_uppercase
    if use_lower:
        pool += string.ascii_lowercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += string.punctuation
    if not pool:
        raise ValueError('At least one character set must be enabled')
    return ''.join(secrets.choice(pool) for _ in range(length))

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument(
        '-l', '--length',
        type=int,
        default=12,
        help='Length of the password (default: 12)',
    )
    parser.add_argument(
        '--no-uppercase',
        action='store_true',
        help='Exclude uppercase letters',
    )
    parser.add_argument(
        '--no-lowercase',
        action='store_true',
        help='Exclude lowercase letters',
    )
    parser.add_argument(
        '--no-digits',
        action='store_true',
        help='Exclude digits',
    )
    parser.add_argument(
        '--no-symbols',
        action='store_true',
        help='Exclude symbols',
    )
    return parser.parse_args()

def main() -> None:
    args = parse_args()
    try:
        password = generate_password(
            length=args.length,
            use_upper=not args.no_uppercase,
            use_lower=not args.no_lowercase,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        )
    except ValueError as e:
        sys.exit(f'Error: {e}')
    print(password)

if __name__ == '__main__':
    main()