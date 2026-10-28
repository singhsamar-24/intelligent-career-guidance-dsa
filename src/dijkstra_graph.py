"""
Graph-Based Skill Dependency Router using Dijkstra's Shortest Path.
Models curriculum prerequisites as a Directed Acyclic Graph (DAG) using Adjacency Lists.
Course: Data Structures and Algorithms (CCSE0301)
"""

import heapq
from typing import Dict, List, Tuple


class SkillGraph:
    """Directed weighted graph representing prerequisite relationships and estimated learning hours."""

    def __init__(self):
        self.adj: Dict[str, List[Tuple[str, float]]] = {}

    def add_edge(self, u: str, v: str, weight: float) -> None:
        """Add directed dependency edge: learning 'u' enables 'v' with 'weight' estimated study hours."""
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append((v, weight))

    def dijkstra_shortest_path(self, start_skill: str, target_skill: str) -> Tuple[List[str], float]:
        """
        Finds the lowest-effort sequential learning pathway from start to target skill.
        Time Complexity: O((V + E) log V) where V = skills, E = prerequisites.
        """
        dist: Dict[str, float] = {node: float('inf') for node in self.adj}
        prev: Dict[str, Optional[str]] = {node: None for node in self.adj}

        if start_skill not in dist:
            dist[start_skill] = 0
        dist[start_skill] = 0

        pq: List[Tuple[float, str]] = [(0.0, start_skill)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist.get(u, float('inf')):
                continue
            if u == target_skill:
                break

            for v, weight in self.adj.get(u, []):
                new_dist = dist.get(u, float('inf')) + weight
                if new_dist < dist.get(v, float('inf')):
                    dist[v] = new_dist
                    prev[v] = u
                    heapq.heappush(pq, (new_dist, v))

        # Reconstruct path backwards from target
        path: List[str] = []
        curr = target_skill
        while curr:
            path.append(curr)
            curr = prev.get(curr)
        path.reverse()

        total_hours = dist.get(target_skill, float('inf'))
        if path and path[0] == start_skill:
            return path, total_hours
        return [], float('inf')
