import sys

mem = [0] * 1000000
i = 1000

mem[i] = (mem[i] + 9) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 9) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 9) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 4) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 3) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 3) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 3) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 2) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -4) & 0xFF
mem[i] = 0
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 3) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -3) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 251) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 6) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -6) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 253) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 8) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 8) & 0xFF
mem[i] = 0
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 7) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 6) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -6) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 247) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 4) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 250) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 4) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] - 1) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 6) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 249) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 252) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 4) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 6) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 6) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 9) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 7) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -7) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 248) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -4) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] - 1) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 6) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 6) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 5) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 254) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 250) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 249) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 5) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 5) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 249) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -5) & 0xFF
mem[i] = 0
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 6) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 6) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 2) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 253) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -4) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] - 1) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 6) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 6) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 3) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 249) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 250) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 3) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 3) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 6) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 4) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 7) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -4) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 252) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 4) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 1) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -4) & 0xFF
mem[i] = 0
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 4) & 0xFF
mem[i] = 0
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -4) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] - 1) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 8) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 6) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -6) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 248) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 5) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 251) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 6) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 250) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 5) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 5) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 4) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 4) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -4) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 254) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 6) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * -6) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 254) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i + 1] = (mem[i + 1] + 253) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
mem[i] = (mem[i] + 3) & 0xFF
mem[i + 1] = (mem[i + 1] + mem[i] * 3) & 0xFF
mem[i] = 0
mem[i + 1] = (mem[i + 1] + 4) & 0xFF
sys.stdout.write(chr(mem[i + 1]))
