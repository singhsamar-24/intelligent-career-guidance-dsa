"""
Balanced AVL Career Taxonomy Module.
Maintains career catalog in a self-balancing binary search tree with guaranteed O(log N) operations.
Course: Data Structures and Algorithms (CCSE0301)
"""

from typing import Dict, List, Optional
from .models import AVLNode


class AVLTree:
    """Self-balancing binary search tree guaranteeing O(log N) insertion, deletion, and lookup."""

    def get_height(self, node: Optional[AVLNode]) -> int:
        return node.height if node else 0

    def get_balance(self, node: Optional[AVLNode]) -> int:
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, y: AVLNode) -> AVLNode:
        x = y.left
        assert x is not None
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x: AVLNode) -> AVLNode:
        y = x.right
        assert y is not None
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root: Optional[AVLNode], career_id: str, title: str, domain: str,
               mandatory_skills: Dict[str, int], elective_skills: Dict[str, float]) -> AVLNode:
        if not root:
            return AVLNode(career_id, title, domain, mandatory_skills, elective_skills)

        if title < root.title:
            root.left = self.insert(root.left, career_id, title, domain, mandatory_skills, elective_skills)
        elif title > root.title:
            root.right = self.insert(root.right, career_id, title, domain, mandatory_skills, elective_skills)
        else:
            # Duplicate title, update details
            root.career_id = career_id
            root.domain = domain
            root.mandatory_skills = mandatory_skills
            root.elective_skills = elective_skills
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left-Left Case
        if balance > 1 and root.left and title < root.left.title:
            return self.right_rotate(root)
        # Right-Right Case
        if balance < -1 and root.right and title > root.right.title:
            return self.left_rotate(root)
        # Left-Right Case
        if balance > 1 and root.left and title > root.left.title:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Right-Left Case
        if balance < -1 and root.right and title < root.right.title:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root: Optional[AVLNode], title: str) -> Optional[AVLNode]:
        """O(log N) exact match lookup by career title."""
        if not root or root.title == title:
            return root
        if title < root.title:
            return self.search(root.left, title)
        return self.search(root.right, title)

    def in_order_traversal(self, root: Optional[AVLNode], accumulator: List[AVLNode]) -> None:
        """Alphabetically sorted traversal of all indexed careers."""
        if root:
            self.in_order_traversal(root.left, accumulator)
            accumulator.append(root)
            self.in_order_traversal(root.right, accumulator)

    def display(self, root: Optional[AVLNode], level: int = 0, prefix: str = "Root: ") -> List[str]:
        """Generate structured visual string representation of the AVL tree."""
        lines = []
        if root is not None:
            lines.append(" " * (level * 4) + prefix + f"{root.title} [BF={self.get_balance(root)}, H={root.height}]")
            if root.left or root.right:
                if root.left:
                    lines.extend(self.display(root.left, level + 1, "L--- "))
                else:
                    lines.append(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    lines.extend(self.display(root.right, level + 1, "R--- "))
                else:
                    lines.append(" " * ((level + 1) * 4) + "R--- None")
        return lines
