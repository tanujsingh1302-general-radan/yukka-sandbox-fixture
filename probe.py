"""Network-isolation probe for the Yukka AUDIT_EXEC sandbox.

Run inside the sandbox:  python probe.py
Each check prints one line. PASS means the connection/lookup was BLOCKED (what we want).
Exit code: 0 if everything was blocked, 1 if anything connected or resolved.
Standard library only; no dependencies.
"""

import os
import socket
import sys

TIMEOUT_S = 3

TARGETS = [
    ("1.1.1.1", 443, "internet (1.1.1.1:443)"),
    ("postgres", 5432, "postgres:5432"),
    ("redis", 6379, "redis:6379"),
    ("ollama", 11434, "ollama:11434"),
]


def blocked_reason(host, port):
    """None if the connection succeeded; otherwise why it was blocked."""
    try:
        with socket.create_connection((host, port), timeout=TIMEOUT_S):
            return None
    except OSError as exc:
        return type(exc).__name__ + (f" errno={exc.errno}" if exc.errno else "")


def main():
    failures = 0
    for host, port, label in TARGETS:
        reason = blocked_reason(host, port)
        if reason is None:
            failures += 1
            print(f"FAIL {label}: CONNECTED")
        else:
            print(f"PASS {label}: blocked ({reason})")

    try:
        infos = socket.getaddrinfo("pypi.org", 443)
        failures += 1
        print(f"FAIL dns lookup pypi.org: resolved to {sorted({i[4][0] for i in infos})}")
    except OSError as exc:
        print(f"PASS dns lookup pypi.org: blocked ({type(exc).__name__})")

    try:
        ifaces = sorted(os.listdir("/sys/class/net"))
        print(f"INFO network interfaces: {', '.join(ifaces)}")
    except OSError:
        pass

    print("RESULT: all blocked" if failures == 0 else f"RESULT: {failures} check(s) CONNECTED")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
