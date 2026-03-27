
# Queue (FIFO)

This folder contains an implementation of a Queue using a circular buffer approach.

---

## 🧩 What Problem It Solves

A queue processes elements **in the same order they arrive**: First-In, First-Out.

Common anywhere fairness or ordering matters.

---

## ⏱ Time & Space Complexity

| Operation | Time |
|----------|------|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Peek | O(1) |
| Space | O(n) |

---

## 🌍 Real-World Uses

- Operating system task scheduling  
- Print queues  
- Network packet queues  
- Breadth‑first search (BFS)  
- Messaging systems (Kafka, RabbitMQ)  

---

## 📄 Implementation File

`queue.py` includes:

- enqueue()  
- dequeue()  
- peek()  
- space-efficient pointer cleanup  
