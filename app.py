# app.py
# The Flask web app: connects URLs (routes) to our Python functions.

from flask import Flask, render_template, request
from analyzer import extract_text, analyze_resume, match_job, suggest_careers
from assistant import get_reply

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # max upload 5 MB


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("resume")
    job_text = request.form.get("job_description", "").strip()

    if not file or file.filename == "":
        return render_template("index.html", error="Please choose a resume file.")

    try:
        text = extract_text(file)
    except ValueError as e:
        return render_template("index.html", error=str(e))
    except Exception:
        return render_template("index.html", error="Sorry, I could not read that file.")

    if len(text.strip()) < 50:
        return render_template("index.html",
                               error="No text found. Scanned/image PDFs are not supported.")

    report = analyze_resume(text)
    match = match_job(report["skills_flat"], job_text) if job_text else None
    careers = suggest_careers(report["skills_flat"])
    return render_template("result.html", r=report, match=match,
                           careers=careers, job_given=bool(job_text))


@app.route("/assistant", methods=["GET", "POST"])
def assistant():
    question, reply = "", None
    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            reply = get_reply(question)
    return render_template("assistant.html", question=question, reply=reply)


if __name__ == "__main__":
    app.run(debug=True)
