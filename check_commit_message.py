#!/usr/bin/env python3
import re
import sys

def main():
    msg_file = sys.argv[1]
    with open(msg_file, 'r') as f:
        message = f.read().strip()

    pattern = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|chore)(\(\w+\))?: .+")
    if not pattern.match(message):
        print("❌ Commit message does not follow Conventional Commits format.")
        print("👉 Example: feat(auth): add OAuth login")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
