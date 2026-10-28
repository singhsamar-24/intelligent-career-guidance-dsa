"""
Dynamic Programming 0/1 Knapsack Semester Study Planner.
Maximizes total career readiness value within time/study hour constraints.
Course: Data Structures and Algorithms (CCSE0301)
"""

from typing import List, Tuple


class DPOptimizer:
    """Solves the 0/1 Knapsack optimization problem for personalized student curriculum planning."""

    @staticmethod
    def optimize_study_plan(skills_list: List[Tuple[str, int, int]], max_hours: int) -> Tuple[List[Tuple[str, int, int]], int]:
        """
        Solves 0/1 Knapsack where:
        - weight = learning hours required for skill
        - value = readiness contribution / priority points
        - capacity = available semester study budget (hours)
        
        Complexity: O(N * W) time and space, where N = candidate skills, W = max_hours.
        Returns: (selected_skills, total_readiness_value)
        """
        n = len(skills_list)
        dp = [[0] * (max_hours + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            name, cost, val = skills_list[i - 1]
            for w in range(max_hours + 1):
                if cost > w:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + val)

        # Backtrack to identify chosen skills
        selected_skills = []
        w = max_hours
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                name, cost, val = skills_list[i - 1]
                selected_skills.append((name, cost, val))
                w -= cost

        selected_skills.reverse()
        total_value = dp[n][max_hours]
        return selected_skills, total_value
