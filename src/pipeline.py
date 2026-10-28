"""
End-to-End Execution Pipeline for Intelligent Career Guidance Platform.
Course: Data Structures and Algorithms (CCSE0301)
"""

from typing import Dict, Any, List
from .models import StudentProfile, AVLNode
from .avl_tree import AVLTree
from .priority_heap import MatchingEngine, MaxHeapRanker
from .dijkstra_graph import SkillGraph
from .dp_optimizer import DPOptimizer


def build_default_catalog(avl: AVLTree) -> AVLNode:
    """Builds standard career taxonomy catalog."""
    root = None
    catalog = [
        ("CR-01", "Data Analyst", "Data Science",
         {"SQL": 3, "Python": 3, "Git": 2, "Stats": 2}, {"Excel": 2}),
        ("CR-02", "Machine Learning Engineer", "Artificial Intelligence",
         {"Python": 4, "ML": 4, "DS": 3, "DL": 3}, {"Docker": 2}),
        ("CR-03", "Backend Developer", "Software Engineering",
         {"Python": 3, "SQL": 3, "Git": 2, "Docker": 3}, {"Linux": 2}),
        ("CR-04", "Cloud DevOps Engineer", "Cloud Computing",
         {"Linux": 4, "Docker": 3, "Git": 2, "Kubernetes": 3}, {"AWS": 3}),
        ("CR-05", "Cybersecurity Analyst", "Information Security",
         {"Networking": 4, "Linux": 3, "Python": 2, "Crypto": 3}, {"Bash": 2})
    ]
    for cid, title, dom, mand, elec in catalog:
        root = avl.insert(root, cid, title, dom, mand, elec)
    return root


def build_default_skill_graph() -> SkillGraph:
    """Constructs directed curriculum dependency graph."""
    graph = SkillGraph()
    graph.add_edge("Python Basics", "Data Structures", 25)
    graph.add_edge("Python Basics", "SQL Databases", 20)
    graph.add_edge("SQL Databases", "Data Wrangling", 15)
    graph.add_edge("Data Structures", "Machine Learning", 30)
    graph.add_edge("Data Wrangling", "Machine Learning", 30)
    graph.add_edge("Machine Learning", "Deep Learning", 40)
    return graph


def run_pipeline(student: StudentProfile, top_k: int = 3) -> Dict[str, Any]:
    """Executes all 4 DSA engines sequentially."""
    avl = AVLTree()
    root = build_default_catalog(avl)

    # 1. AVL In-Order Traversal
    all_careers: List[AVLNode] = []
    avl.in_order_traversal(root, all_careers)

    # 2. Max-Heap Ranker
    ranker = MaxHeapRanker()
    for c in all_careers:
        score, gaps = MatchingEngine.evaluate(student, c)
        ranker.push(score, c.title, c.domain, gaps)

    recommendations = ranker.extract_top_k(top_k)

    # 3. Dijkstra Shortest Pathway
    graph = build_default_skill_graph()
    path, effort = graph.dijkstra_shortest_path("Python Basics", "Deep Learning")

    # 4. DP 0/1 Knapsack Semester Plan
    candidate_skills = [
        ("Statistical Inference", 20, 35),
        ("Docker Containerization", 25, 30),
        ("Deep Learning Frameworks", 40, 60),
        ("Kubernetes Orchestration", 45, 40),
        ("Cloud Architecture (AWS)", 35, 45),
        ("Advanced Data Structures", 15, 25)
    ]
    chosen_plan, total_val = DPOptimizer.optimize_study_plan(candidate_skills, student.study_hours)

    return {
        "student": student,
        "recommendations": recommendations,
        "learning_pathway": {"path": path, "total_hours": effort},
        "study_plan": {"selected": chosen_plan, "total_value": total_val}
    }
