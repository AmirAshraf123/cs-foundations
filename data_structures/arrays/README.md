
# Dynamic Array

This folder contains a manual implementation of a dynamic array, similar to Python's built‑in list.

---

## 🧩 What Problem It Solves

A dynamic array stores multiple elements in contiguous memory and automatically grows when capacity is reached. It supports:

- Fast index access  
- Amortized O(1) appends  
- Efficient iteration  

---

## ⏱ Time & Space Complexity

| Operation | Complexity |
|----------|------------|
| Get by index | O(1) |
| Set by index | O(1) |
| Append | Amortized O(1) |
| Insert/remove (middle) | O(n) |
| Search | O(n) |
| Space | O(n) |

---

## 🌍 Real-World Uses

- Python lists  
- Arrays in C, Java, JavaScript  
- Memory buffers  
- Machine learning tensors (NumPy, Torch)  
- Database result sets  

---

## 📄 Implementation File

`array.py` contains:

- Auto-resizing logic  
- Index lookup  
- Push / pop methods  
