
# Hash Map

This folder contains a basic hash map implementation using **separate chaining** to handle collisions.

---

## 🧩 What Problem It Solves

Hash maps allow instant key‑to‑value lookup without scanning through all items.

Perfect when you need fast access based on a key.

---

## ⏱ Time & Space Complexity

| Operation | Average | Worst |
|----------|----------|--------|
| Insert | O(1) | O(n) |
| Get | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Space | O(n) | |

Worst case rarely happens unless many keys collide.

---

## 🌍 Real-World Uses

- Python dictionaries  
- Java HashMap  
- C++ unordered_map  
- Caching systems  
- Routing tables  
- Databases (indexing)  

---

## 📄 Implementation File

`hashmap.py` includes:

- Hash function  
- Buckets (lists)  
- Collision handling via chaining  
- get(), set(), delete()  
