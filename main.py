"""
Intelligent Career Guidance Platform - Main CLI & Benchmark Runner
Course: Data Structures and Algorithms (CCSE0301) | NIET Greater Noida
Student: Samar Singh (Roll No: 2501331940042) | Mentor: Mr. Vikash Tripathi
"""

import sys
from src.models import StudentProfile
from src.avl_tree import AVLTree
from src.pipeline import build_default_catalog, build_default_skill_graph, run_pipeline


def print_banner():
    banner = r"""
========================================================================
   INTELLIGENT CAREER GUIDANCE & OPTIMIZATION PLATFORM
   Algorithmic Foundation: AVL Trees | Max-Heaps | Dijkstra | 0/1 Knapsack
   Course: CCSE0301 (DSA Capstone) | NIET Greater Noida
   Author: Samar Singh (Roll No: 2501331940042)
========================================================================
"""
    print(banner)


def run_demo():
    print_banner()
    print("[+] Initializing Student Profile: Samar Singh (B.Tech CSE-AI)")
    student = StudentProfile(
        student_id="2501331940042",
        name="Samar Singh",
        skills_dict={"Python": 4, "SQL": 3, "Git": 4, "Data Structures": 3, "Machine Learning": 3},
        interests=["Data Science", "Artificial Intelligence"],
        study_hours=100
    )

    print(f"    - Student ID:    {student.student_id}")
    print(f"    - Current Skills: {student.skills}")
    print(f"    - Interests:     {student.interests}")
    print(f"    - Study Budget:  {student.study_hours} Hours\n")

    avl = AVLTree()
    root = build_default_catalog(avl)
    print("[1] AVL Tree Career Taxonomy Catalog (In-Order Visual Tree):")
    for line in avl.display(root):
        print("    " + line)
    print()

    results = run_pipeline(student, top_k=3)

    print("[2] Max-Heap Priority Extraction (Top-3 Career Matches):")
    print("    " + "-" * 65)
    print(f"    {'Rank':<6} {'Career Role':<28} {'Match Score':<14} {'Skill Gaps'}")
    print("    " + "-" * 65)
    for r in results["recommendations"]:
        gaps_str = ", ".join(r['gaps']) if r['gaps'] else "None (Full Fit)"
        print(f"    #{r['rank']:<5} {r['career']:<28} {r['cms']:>6.2f}%       {gaps_str}")
    print("    " + "-" * 65 + "\n")

    pathway = results["learning_pathway"]
    print("[3] Dijkstra Prerequisite Shortest Pathway:")
    print(f"    Target: 'Python Basics' -> 'Deep Learning'")
    print(f"    Optimal Route: {' -> '.join(pathway['path'])}")
    print(f"    Total Prerequisite Effort: {pathway['total_hours']} Hours\n")

    plan = results["study_plan"]
    print(f"[4] DP 0/1 Knapsack Optimal Semester Plan (Budget: {student.study_hours} Hours):")
    print(f"    Maximized Readiness Value: {plan['total_value']} Points")
    for name, cost, val in plan["selected"]:
        print(f"      + {name:<26} (Effort: {cost}h | Readiness Gain: +{val} pts)")
    print("\n[SUCCESS] Integrated Pipeline Execution Completed Successfully.")


if __name__ == '__main__':
    run_demo()
