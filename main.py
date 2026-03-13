import time
from engine import run_cycle

print("Quant platform started")

while True:

    run_cycle()

    time.sleep(300)
