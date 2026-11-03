# analyzer.py
# The brain of the app: reads the file, finds skills, scores the resume.

import re
from pypdf import PdfReader
from docx import Document
from skills_data import SKILLS, ACTION_VERBS, SECTIONS, CAREER_PATHS


# ---------- 1. Reading the file ----------
def extract_text(file):
    """Return plain text from a PDF, DOCX or TXT upload."""
    name = file.filename.lower()
    if name.endswith(".pdf"):
        reader = PdfReader(file.stream)
        return "\n".join((page.extract_text() or "") for page in reader.pages)
    if name.endswith(".docx"):
        doc = Document(file.stream)
        return "\n".join(p.text for p in doc.paragraphs)
    if name.endswith(".txt"):
        return file.read().decode("utf-8", errors="ignore")
    raise ValueError("Please upload a PDF, DOCX or TXT file.")


# ---------- 2. Small helper: find a word safely ----------
def has_word(text, word):
    """True if `word` appears as a whole word (so 'java' doesn't match 'javascript')."""
    pattern = r"(?<![a-z0-9])" + re.escape(word) + r"(?![a-z0-9])"
    return re.search(pattern, text) is not None


def find_skills(text):
    """Return {category: [skills found]} for the given text."""
    text = text.lower()
    found = {}
    for category, skills in SKILLS.items():
        matches = [s for s in skills if has_word(text, s)]
        if matches:
            found[category] = matches
    return found


def flatten(skill_dict):
    return [skill for group in skill_dict.values() for skill in group]


# ---------- 3. Main analysis ----------
def analyze_resume(text):
    lower = text.lower()
    words = re.findall(r"\w+", text)

    email = re.search(r"[\w.+-]+@[\w-]+\.[\w.]+", text)
    phone = re.search(r"(\+?\d[\d\s-]{8,13}\d)", text)
    has_linkedin = "linkedin.com" in lower
    has_github = "github.com" in lower

    sections_found = [name for name, keys in SECTIONS.items()
                      if any(has_word(lower, k) for k in keys)]
    sections_missing = [n for n in SECTIONS if n not in sections_found]

    skills = find_skills(text)
    skills_flat = flatten(skills)
    verbs_found = [v for v in ACTION_VERBS if has_word(lower, v)]

    # --- Scoring (adds up to 100) ---
    score = {}
    score["Contact info (20)"] = (10 if email else 0) + (10 if phone else 0)
    score["Sections (30)"] = round(30 * len(sections_found) / len(SECTIONS))
    score["Skills (20)"] = min(20, len(skills_flat) * 2)
    score["Action verbs (15)"] = min(15, len(verbs_found) * 3)
    score["Links (5)"] = (3 if has_github else 0) + (2 if has_linkedin else 0)
    wc = len(words)
    score["Length (10)"] = 10 if 150 <= wc <= 900 else 4
    total = sum(score.values())

    # --- Friendly tips ---
    tips = []
    if not email:
        tips.append("Add a professional email address.")
    if not phone:
        tips.append("Add a phone number.")
    for s in sections_missing:
        tips.append(f"Consider adding a '{s}' section.")
    if len(skills_flat) < 5:
        tips.append("List more technical skills (aim for 8 or more).")
    if len(verbs_found) < 4:
        tips.append("Start bullet points with action verbs like 'Built', 'Designed', 'Improved'.")
    if not has_github:
        tips.append("Add your GitHub link so recruiters can see your projects.")
    if wc < 150:
        tips.append("Your resume looks short. Add more detail about projects.")
    elif wc > 900:
        tips.append("Your resume is long. Try to keep it to 1-2 pages.")
    if not tips:
        tips.append("Great job! Your resume covers all the basics.")

    return {
        "word_count": wc, "email": email.group() if email else None,
        "phone": phone.group().strip() if phone else None,
        "sections_found": sections_found, "sections_missing": sections_missing,
        "skills": skills, "skills_flat": skills_flat,
        "verbs_found": verbs_found, "score": score, "total": total, "tips": tips,
    }


# ---------- 4. Compare with a job description ----------
def match_job(resume_skills, job_text):
    job_skills = flatten(find_skills(job_text))
    if not job_skills:
        return None
    matched = [s for s in job_skills if s in resume_skills]
    missing = [s for s in job_skills if s not in resume_skills]
    percent = round(100 * len(matched) / len(job_skills))
    return {"percent": percent, "matched": matched, "missing": missing}


# ---------- 5. Career suggestions ----------
def suggest_careers(resume_skills):
    results = []
    for role, needed in CAREER_PATHS.items():
        have = [s for s in needed if s in resume_skills]
        missing = [s for s in needed if s not in resume_skills]
        percent = round(100 * len(have) / len(needed))
        results.append({"role": role, "percent": percent, "missing": missing})
    results.sort(key=lambda r: r["percent"], reverse=True)
    return results[:3]
