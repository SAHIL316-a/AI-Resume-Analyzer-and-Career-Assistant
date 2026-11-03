# assistant.py
# A very simple rule-based career chatbot (no API key needed).
# It looks for keywords in the question and returns a matching answer.

from skills_data import ROADMAPS

def get_reply(question):
    q = question.lower()

    for role, roadmap in ROADMAPS.items():
        # match on any main word of the role name, e.g. "backend", "data analyst"
        if role.lower() in q or any(w in q for w in role.lower().split()[:2] if len(w) > 4):
            return f"Roadmap for {role}: {roadmap}"

    if "interview" in q:
        return ("Interview tips: research the company, practise explaining your projects "
                "in simple words, revise basics of your main language, and prepare 2 "
                "questions to ask the interviewer.")
    if "resume" in q or "cv" in q:
        return ("Resume tips: keep it to 1-2 pages, use action verbs, list projects with "
                "results, and add your GitHub link.")
    if "project" in q:
        return ("Project ideas: a to-do web app, a quiz app, an expense tracker, a "
                "resume analyzer, or a simple chatbot. Put every project on GitHub.")
    if "salary" in q:
        return "Salary depends on skills, city and company. Focus on building projects first; pay follows skill."
    if "hello" in q or "hi" in q.split():
        return "Hello! Ask me about career roadmaps, interviews, resumes or project ideas."

    return ("I'm a simple assistant. Try asking about: 'data analyst roadmap', "
            "'interview tips', 'resume tips' or 'project ideas'.")
