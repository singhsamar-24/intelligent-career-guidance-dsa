# 🎓 Intelligent Career Guidance Platform (DSA Capstone)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](tests/)
[![Academic Project](https://img.shields.io/badge/NIET-PBL%20Capstone-blueviolet.svg)](docs/)
[![SDG](https://img.shields.io/badge/SDG%204-Quality%20Education-orange.svg)](https://sdgs.un.org/goals/goal4)

An algorithmic decision-support and curriculum optimization engine developed as the **Capstone Project for Data Structures and Algorithms (CCSE0301)** at **Noida Institute of Engineering & Technology (NIET)**.

The platform synthesizes four core computer science algorithmic paradigms—**Self-Balancing AVL Search Trees**, **Max-Heap Priority Queues**, **Dijkstra's Shortest Path on Weighted DAGs**, and **0/1 Knapsack Dynamic Programming**—to dynamically index career requirements, match student competencies, compute prerequisite learning pathways, and optimize personalized semester study budgets.

---

## 🏛️ System Architecture & Algorithmic Workflow

```
   +-------------------------------------------------------+
   |            Student Competency Profile                 |
   |   (Skills, Domain Interests, Semester Hour Budget)    |
   +---------------------------+---------------------------+
                               |
                               v
+-------------------------------------------------------------+
|  Module 1 & 2: Self-Balancing AVL Career Taxonomy Tree      |
|  - Guaranteed O(log N) lookup & alphabetical traversal      |
|  - Tracks height balance factors (-1, 0, 1) with rotations   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|  Module 3: Multi-Factor Matcher & Max-Heap Ranker           |
|  - Computes Composite Match Score (CMS) with gap penalties   |
|  - O(N + K log N) optimal extraction of Top-K career roles   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|  Module 4: Graph Prerequisite Router (Dijkstra)             |
|  - Models curriculum skill prerequisites as a weighted DAG   |
|  - O((V + E) log V) least-effort learning path reconstruction|
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|  Module 5: DP 0/1 Knapsack Semester Study Optimizer         |
|  - Maximizes total career readiness value within time budget |
|  - O(N * W) pseudo-polynomial optimal subset reconstruction  |
+-------------------------------------------------------------+
```

---

## ⚡ Algorithmic Complexity Matrix

| Engine | Data Structure / Algorithm | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity | Real-World Application |
|---|---|---|---|---|---|
| **Career Catalog** | **AVL Search Tree** | $\mathcal{O}(\log N)$ | $\mathcal{O}(\log N)$ | $\mathcal{O}(N)$ | Scalable, balanced search across thousands of evolving job titles |
| **Top-K Ranking** | **Max-Heap Priority Queue** | $\mathcal{O}(N + K \log N)$ | $\mathcal{O}(N + K \log N)$ | $\mathcal{O}(N)$ | Instant retrieval of best career matches without sorting the full database |
| **Pathway Routing** | **Dijkstra's Algorithm (DAG)** | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V + E)$ | Minimum required study hours to bridge prerequisite knowledge gaps |
| **Curriculum Budget** | **0/1 Knapsack Dynamic Prog.** | $\mathcal{O}(N \times W)$ | $\mathcal{O}(N \times W)$ | $\mathcal{O}(N \times W)$ | Maximizing semester skill gains within a strict weekly hour limit |

---

## 📂 Project Directory Structure

```
intelligent-career-guidance-dsa/
├── docs/                                    # Academic reports & presentations
│   ├── Month_2_Report.docx                  # Mid-term progress report
│   ├── Month_3_Final_Report.docx            # Comprehensive 30+ page final report
│   ├── Intelligent_Career_Guidance_Platform.pptx
│   └── Intelligent_Career_Guidance_Platform_Preview.pdf
├── src/                                     # Modular engine implementation
│   ├── __init__.py                          # Package exports
│   ├── models.py                            # Domain entities (AVLNode, StudentProfile)
│   ├── avl_tree.py                          # AVL Tree with balancing & rotations
│   ├── priority_heap.py                     # MatchingEngine & MaxHeapRanker
│   ├── dijkstra_graph.py                    # Directed weighted graph & Dijkstra
│   ├── dp_optimizer.py                      # 0/1 Knapsack DP optimizer
│   └── pipeline.py                          # Integrated pipeline orchestrator
├── tests/
│   └── test_dsa.py                          # Comprehensive unit test suite
├── .gitignore                               # Standard Python gitignore
├── LICENSE                                  # MIT License
├── main.py                                  # CLI runner & demonstration benchmark
└── requirements.txt                         # Runtime dependencies
```

---

## 🚀 Quickstart & Execution

### 1. Prerequisites
- Python 3.10 or higher
- Standard library only (no mandatory third-party runtime dependencies)

### 2. Run the Demonstration Pipeline
```bash
python main.py
```

**Sample Output:**
```
========================================================================
   INTELLIGENT CAREER GUIDANCE & OPTIMIZATION PLATFORM
   Algorithmic Foundation: AVL Trees | Max-Heaps | Dijkstra | 0/1 Knapsack
   Course: CCSE0301 (DSA Capstone) | NIET Greater Noida
   Author: Samar Singh (Roll No: 2501331940042)
========================================================================

[+] Initializing Student Profile: Samar Singh (B.Tech CSE-AI)
    - Student ID:    2501331940042
    - Current Skills: {'python': 4, 'sql': 3, 'git': 4, 'data structures': 3, 'machine learning': 3}
    - Interests:     ['data science', 'artificial intelligence']
    - Study Budget:  100 Hours

[1] AVL Tree Career Taxonomy Catalog (In-Order Visual Tree):
    Root: Data Analyst [BF=1, H=3]
        L--- Cloud DevOps Engineer [BF=0, H=2]
            L--- Backend Developer [BF=0, H=1]
            R--- Cybersecurity Analyst [BF=0, H=1]
        R--- Machine Learning Engineer [BF=0, H=1]

[2] Max-Heap Priority Extraction (Top-3 Career Matches):
    -----------------------------------------------------------------
    Rank   Career Role                  Match Score    Skill Gaps
    -----------------------------------------------------------------
    #1     Data Analyst                  63.75%       Stats
    #2     Backend Developer             45.90%       Docker
    #3     Machine Learning Engineer     24.75%       ML, DS, DL
    -----------------------------------------------------------------

[3] Dijkstra Prerequisite Shortest Pathway:
    Target: 'Python Basics' -> 'Deep Learning'
    Optimal Route: Python Basics -> Data Structures -> Machine Learning -> Deep Learning
    Total Prerequisite Effort: 95 Hours

[4] DP 0/1 Knapsack Optimal Semester Plan (Budget: 100 Hours):
    Maximized Readiness Value: 150 Points
      + Statistical Inference      (Effort: 20h | Readiness Gain: +35 pts)
      + Docker Containerization    (Effort: 25h | Readiness Gain: +30 pts)
      + Deep Learning Frameworks   (Effort: 40h | Readiness Gain: +60 pts)
      + Advanced Data Structures   (Effort: 15h | Readiness Gain: +25 pts)

[SUCCESS] Integrated Pipeline Execution Completed Successfully.
```

### 3. Run Unit Tests
```bash
python -m unittest discover -s tests -p "test_*.py"
```

---

## 👨‍💻 Author & Academic Attribution

- **Student:** Samar Singh
- **Roll Number:** 2501331940042
- **Programme:** B.Tech Computer Science & Engineering (Artificial Intelligence)
- **Institution:** Noida Institute of Engineering & Technology (NIET), Greater Noida
- **Course:** Data Structures and Algorithms (CCSE0301)
- **Faculty Mentor:** Mr. Vikash Tripathi (Assistant Professor, Dept. of AI)
- **UN SDG Alignment:** Goal 4: Quality Education (Target 4.4 - Skills for Employment)

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
