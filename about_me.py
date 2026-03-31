#!/usr/bin/env python3
"""
🐍 About Me — Interactive script by Mathew Dyrin
Run it and discover fun facts!
"""

import random
import time
import sys


def typing_effect(text, delay=0.03):
    """Print text with a cool typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def show_banner():
    banner = r"""
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║     __  __       _   _                   ║
    ║    |  \/  | __ _| |_| |__   _____      __║
    ║    | |\/| |/ _` | __| '_ \ / _ \ \ /\ / /║
    ║    | |  | | (_| | |_| | | |  __/\ V  V / ║
    ║    |_|  |_|\__,_|\__|_| |_|\___| \_/\_/  ║
    ║                                          ║
    ║            D Y R I N                     ║
    ╚══════════════════════════════════════════╝
    """
    print(banner)


def about():
    info = {
        "👤 Name": "Mathew Dyrin",
        "💻 Role": "Python Developer",
        "🐍 Fav Language": "Python",
        "📂 Public Repos": "9+",
        "🔧 Frameworks": "Django, DRF, aiogram",
        "🌍 Interests": "Web Dev, Bots, Scraping, ML",
    }

    typing_effect("\n📋 About Me:\n")
    for key, value in info.items():
        typing_effect(f"  {key}: {value}")
        time.sleep(0.1)


def fun_facts():
    facts = [
        "🎲 I once wrote a cipher algorithm from scratch (own_cipher repo)!",
        "🤖 I've built multiple Telegram bots for different purposes.",
        "📊 I love analyzing data and building scrapers.",
        "🎮 I even wrote scripts in Lua for trading charts (QUIKChartLevels)!",
        "🌐 My first big project was a charity platform (goodgift).",
        "📁 I automated file sorting because I hate messy folders.",
        "☕ Coffee + Python = Productivity × 10",
        "🧠 I enjoy machine learning experiments in my free time.",
    ]

    typing_effect("\n🎯 Fun Facts (random selection):\n")
    selected = random.sample(facts, min(4, len(facts)))
    for i, fact in enumerate(selected, 1):
        typing_effect(f"  {i}. {fact}")
        time.sleep(0.2)


def skills_bar():
    skills = {
        "Python":     95,
        "Django":     85,
        "JavaScript": 60,
        "Docker":     70,
        "Git":        90,
        "ML/AI":      65,
        "Scraping":   88,
        "Bots":       92,
    }

    typing_effect("\n📊 Skills:\n")
    for skill, level in skills.items():
        bar = "█" * (level // 5) + "░" * (20 - level // 5)
        typing_effect(f"  {skill:<12} [{bar}] {level}%")
        time.sleep(0.1)


def main():
    show_banner()
    about()
    skills_bar()
    fun_facts()

    typing_effect("\n✨ Thanks for checking out my profile!")
    typing_effect("🔗 GitHub: https://github.com/MathewDyrin")
    typing_effect("\n👋 See you around!\n")


if __name__ == "__main__":
    main()
