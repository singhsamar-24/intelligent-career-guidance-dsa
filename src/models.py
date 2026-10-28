"""
Domain Models for the Intelligent Career Guidance Platform.
Course: Data Structures and Algorithms (CCSE0301) | NIET Greater Noida
Student: Samar Singh (Roll No: 2501331940042)
"""

from typing import Dict, List, Optional


class AVLNode:
    """Represents a self-balancing AVL tree node indexing career records."""
    def __init__(self, career_id: str, title: str, domain: str, mandatory_skills: Dict[str, int], elective_skills: Dict[str, float]):
        self.career_id = career_id
        self.title = title
        self.domain = domain
        self.mandatory_skills = mandatory_skills  # dict: skill -> min_proficiency (1-5)
        self.elective_skills = elective_skills    # dict: skill -> weight (1.0-3.0)
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1

    def __repr__(self) -> str:
        return f"AVLNode({self.career_id}, {self.title}, domain={self.domain}, height={self.height})"


class StudentProfile:
    """Encapsulates student competencies, ratings, domain interests, and study budget."""
    def __init__(self, student_id: str, name: str, skills_dict: Dict[str, int], interests: List[str], study_hours: int = 100):
        self.student_id = student_id
        self.name = name
        self.skills = {k.lower(): v for k, v in skills_dict.items()}
        self.interests = [i.lower() for i in interests]
        self.study_hours = study_hours

    def __repr__(self) -> str:
        return f"StudentProfile({self.student_id}, {self.name}, skills={len(self.skills)}, budget={self.study_hours}h)"
