# skills_data.py
# All the "knowledge" of our app lives here as plain Python lists/dicts.
# To teach the app new skills, just add words to these lists.

SKILLS = {
    "Programming": ["python", "java", "c++", "c#", "javascript", "typescript",
                    "php", "go", "kotlin", "swift", "r", "sql"],
    "Web": ["html", "css", "react", "angular", "vue", "node.js", "flask",
            "django", "fastapi", "bootstrap", "tailwind", "rest api"],
    "Data & AI": ["machine learning", "deep learning", "nlp", "pandas", "numpy",
                  "scikit-learn", "tensorflow", "pytorch", "data analysis",
                  "power bi", "tableau", "excel", "statistics"],
    "Database": ["mysql", "postgresql", "mongodb", "sqlite", "oracle"],
    "Tools & Cloud": ["git", "github", "docker", "linux", "aws", "azure",
                      "jenkins", "postman", "vs code"],
    "Soft Skills": ["communication", "teamwork", "leadership",
                    "problem solving", "time management", "critical thinking"],
}

# Strong verbs make a resume sound active and confident
ACTION_VERBS = ["built", "developed", "designed", "created", "implemented",
                "led", "managed", "improved", "analyzed", "optimized",
                "launched", "automated", "organized", "achieved", "deployed",
                "tested", "collaborated", "wrote", "reduced", "increased"]

# Section name -> words that usually appear as its heading
SECTIONS = {
    "Summary / Objective": ["summary", "objective", "profile", "about me"],
    "Education": ["education", "academic", "qualification"],
    "Experience": ["experience", "internship", "employment", "work history"],
    "Projects": ["projects", "project work"],
    "Skills": ["skills", "technical skills", "technologies"],
    "Certifications": ["certification", "certifications", "courses"],
}

# Career path -> skills usually needed for it
CAREER_PATHS = {
    "Python Backend Developer": ["python", "flask", "django", "fastapi",
                                 "sql", "git", "rest api", "docker"],
    "Frontend Developer": ["html", "css", "javascript", "react", "git",
                           "bootstrap", "typescript"],
    "Data Analyst": ["python", "sql", "excel", "pandas", "power bi",
                     "tableau", "statistics", "data analysis"],
    "Machine Learning Engineer": ["python", "machine learning", "pandas",
                                  "numpy", "scikit-learn", "tensorflow",
                                  "deep learning", "git"],
    "Full Stack Developer": ["html", "css", "javascript", "react", "node.js",
                             "sql", "git", "rest api"],
    "Software Developer (C++/Java)": ["c++", "java", "git", "sql",
                                      "problem solving", "linux"],
}

# Learning tips for each career, used by the assistant
ROADMAPS = {
    "Python Backend Developer": "Learn Python basics -> Flask -> SQL & SQLite -> build a REST API -> learn Git -> try Docker.",
    "Frontend Developer": "HTML -> CSS -> JavaScript -> React -> build 3 small websites and host them on GitHub Pages.",
    "Data Analyst": "Excel -> SQL -> Python (pandas) -> Power BI or Tableau -> do 2 projects on public datasets.",
    "Machine Learning Engineer": "Python -> statistics -> pandas/numpy -> scikit-learn -> a small ML project -> deep learning basics.",
    "Full Stack Developer": "HTML/CSS/JS -> React -> Node.js or Flask -> a database -> build one complete app with login.",
    "Software Developer (C++/Java)": "Master one language -> data structures & algorithms -> OOP -> Git -> build a console project.",
}
