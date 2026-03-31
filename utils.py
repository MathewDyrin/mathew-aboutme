"""
utils.py — Utility functions for the about-me project.
"""

import datetime
import hashlib


def get_greeting():
    """Return a time-based greeting."""
    hour = datetime.datetime.now().hour
    if hour < 6:
        return "🌙 Good night!"
    elif hour < 12:
        return "☀️ Good morning!"
    elif hour < 18:
        return "🌤 Good afternoon!"
    else:
        return "🌆 Good evening!"


def generate_avatar_hash(name: str) -> str:
    """Generate a unique avatar hash from a name."""
    return hashlib.md5(name.encode()).hexdigest()


def format_skills(skills: dict) -> str:
    """Pretty-print a skills dictionary as a bar chart."""
    lines = []
    for skill, level in sorted(skills.items(), key=lambda x: -x[1]):
        bar = "█" * (level // 5) + "░" * (20 - level // 5)
        lines.append(f"  {skill:<15} {bar} {level}%")
    return "\n".join(lines)


if __name__ == "__main__":
    print(get_greeting())
    print(f"\nAvatar hash: {generate_avatar_hash('Mathew Dyrin')}")
    print(f"\nSkills:\n{format_skills({'Python': 95, 'Git': 90, 'Docker': 80})}")
