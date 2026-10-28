"""
Multi-Factor Skill Matching and Max-Heap Priority Ranking Module.
Implements Career Match Score (CMS) computation and O(log K) heap extraction.
Course: Data Structures and Algorithms (CCSE0301)
"""

import heapq
from typing import Dict, List, Tuple
from .models import AVLNode, StudentProfile


class MatchingEngine:
    """Evaluates student competency overlap against career requirements and computes deterministic match scores."""

    @staticmethod
    def evaluate(student: StudentProfile, career_node: AVLNode) -> Tuple[float, List[str]]:
        """
        Calculates Composite Match Score (CMS) based on:
        - Mandatory skills fulfillment (weighted 70% of skill component)
        - Elective skills enrichment (weighted 30% of skill component)
        - Student domain interest alignment
        - Core gap penalty factor
        """
        total_weight, earned_weight = 0.0, 0.0
        missing_core = []

        for skill, min_prof in career_node.mandatory_skills.items():
            s_clean = skill.lower()
            weight = 3.0
            total_weight += weight
            if s_clean in student.skills:
                earned_weight += weight * min(1.0, student.skills[s_clean] / float(min_prof))
            else:
                missing_core.append(skill)

        for skill, weight in career_node.elective_skills.items():
            s_clean = skill.lower()
            total_weight += weight
            if s_clean in student.skills:
                earned_weight += weight * min(1.0, student.skills[s_clean] / 3.0)

        s_comp = (earned_weight / total_weight) if total_weight > 0 else 0.0
        i_comp = 1.0 if career_node.domain.lower() in student.interests else 0.30
        p_core = max(0.40, 1.0 - (0.15 * min(4, len(missing_core))))
        cms = ((0.70 * s_comp) + (0.30 * i_comp)) * p_core * 100.0

        return round(cms, 2), missing_core


class MaxHeapRanker:
    """Maintains candidate careers in a priority queue for optimal Top-K extraction in O(N + K log N)."""

    def __init__(self):
        self.heap: List[Tuple[float, str, str, List[str]]] = []

    def push(self, score: float, career_title: str, domain: str, missing_skills: List[str]) -> None:
        # Negate score to convert min-heap into max-heap
        heapq.heappush(self.heap, (-score, career_title, domain, missing_skills))

    def extract_top_k(self, k: int) -> List[Dict]:
        results = []
        count = 0
        while self.heap and count < k:
            neg_score, title, domain, missing = heapq.heappop(self.heap)
            results.append({
                "rank": count + 1,
                "career": title,
                "domain": domain,
                "cms": -neg_score,
                "gaps": missing
            })
            count += 1
        return results
