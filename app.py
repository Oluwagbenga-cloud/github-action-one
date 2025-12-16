import argparse
from datetime import datetime

#!/usr/bin/env python3
"""Simple demo script: greet by name and repeat."""


def greet(name: str, count: int = 1) -> None:
    """Print greeting 'count' times with timestamp."""
    for _ in range(count):
        print(f"{datetime.now().isoformat()} - Hello, {name}!")

def main():
    parser = argparse.ArgumentParser(description="Simple greeter")
    parser.add_argument("--name", "-n", default="World", help="Name to greet")
    parser.add_argument("--count", "-c", type=int, default=1, help="How many times to greet")
    args = parser.parse_args()
    greet(args.name, args.count)

if __name__ == "__main__":
    main()