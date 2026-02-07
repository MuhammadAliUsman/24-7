import sys
import time
import os

# Typing effect
def type_text(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ASCII Banner
banner = r"""
██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
                    DragonCloud
"""

# Clear terminal
os.system("clear")

# Show banner
print(banner)
time.sleep(1)

# Startup typing
type_text("Initializing DragonCloud...", 0.06)
type_text("Checking nodes...", 0.05)
type_text("Starting services...", 0.05)
type_text("DragonCloud is ONLINE ☁️🐉", 0.07)

time.sleep(1)
print("\nSpamming initiated...\n")

# Spam DragonCloud forever
try:
    while True:
        type_text("DragonCloud", 0.02)
except KeyboardInterrupt:
    print("\nStopped by user 👋")
