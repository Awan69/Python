from collections import deque

queue = deque ([1,2,3,4,5])

queue.append(6)
print(f"Antrian Masuk {6}")

queue.append(7)
print(f"Antrian Massuk {7}")

out = queue.popleft()
print(f"Antrian Keluar {out}")
print(f"Antrian Sekarang {out}")
