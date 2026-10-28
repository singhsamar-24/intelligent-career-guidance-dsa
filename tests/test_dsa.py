"""
Unit Tests for the Intelligent Career Guidance Platform.
Course: Data Structures and Algorithms (CCSE0301)
"""

import unittest
from src.models import StudentProfile, AVLNode
from src.avl_tree import AVLTree
from src.priority_heap import MatchingEngine, MaxHeapRanker
from src.dijkstra_graph import SkillGraph
from src.dp_optimizer import DPOptimizer


class TestDSAAlgorithms(unittest.TestCase):

    def setUp(self):
        self.avl = AVLTree()
        self.root = None

    def test_avl_balance_factor(self):
        """Verify AVL self-balancing property holds under sequential insertions."""
        keys = [
            ("C1", "Software Engineer"),
            ("C2", "Data Scientist"),
            ("C3", "DevOps Engineer"),
            ("C4", "Cloud Architect"),
            ("C5", "AI Specialist")
        ]
        for cid, title in keys:
            self.root = self.avl.insert(self.root, cid, title, "Tech", {"Coding": 3}, {})

        # In an AVL tree, every node must have balance factor in {-1, 0, 1}
        def check_balance(node):
            if not node:
                return True
            bf = self.avl.get_balance(node)
            self.assertIn(bf, [-1, 0, 1], f"Node {node.title} has invalid balance factor {bf}")
            return check_balance(node.left) and check_balance(node.right)

        self.assertTrue(check_balance(self.root))

    def test_avl_search(self):
        """Verify O(log N) lookup returns target career node."""
        self.root = self.avl.insert(None, "C1", "Backend Developer", "Tech", {"SQL": 3}, {})
        self.root = self.avl.insert(self.root, "C2", "Frontend Developer", "Tech", {"CSS": 3}, {})
        res = self.avl.search(self.root, "Frontend Developer")
        self.assertIsNotNone(res)
        self.assertEqual(res.career_id, "C2")

    def test_max_heap_ordering(self):
        """Verify MaxHeapRanker extracts candidates in strict descending order of score."""
        ranker = MaxHeapRanker()
        ranker.push(72.5, "Role A", "Domain", [])
        ranker.push(95.0, "Role B", "Domain", [])
        ranker.push(84.0, "Role C", "Domain", [])

        top = ranker.extract_top_k(3)
        self.assertEqual(top[0]["career"], "Role B")
        self.assertEqual(top[1]["career"], "Role C")
        self.assertEqual(top[2]["career"], "Role A")

    def test_dijkstra_shortest_path(self):
        """Verify Dijkstra algorithm calculates lowest-cost pathway correctly."""
        graph = SkillGraph()
        graph.add_edge("A", "B", 10)
        graph.add_edge("A", "C", 30)
        graph.add_edge("B", "C", 5)
        path, cost = graph.dijkstra_shortest_path("A", "C")
        self.assertEqual(path, ["A", "B", "C"])
        self.assertEqual(cost, 15)

    def test_knapsack_optimization(self):
        """Verify 0/1 Knapsack maximizes total readiness within hour capacity."""
        skills = [
            ("Skill 1", 20, 30),
            ("Skill 2", 30, 40),
            ("Skill 3", 40, 60),
            ("Skill 4", 10, 15)
        ]
        # Budget = 50 hours: Optimal subset is Skill 4 (10h, 15) + Skill 3 (40h, 60) = 50h, 75 val
        chosen, max_val = DPOptimizer.optimize_study_plan(skills, 50)
        self.assertEqual(max_val, 75)
        self.assertEqual(sum(item[1] for item in chosen), 50)


if __name__ == '__main__':
    unittest.main()
