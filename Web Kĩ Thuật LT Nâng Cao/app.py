from flask import Flask, render_template, request
import os
import time
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads folder if not exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

# =========================
# 1. KMP ALGORITHM
# =========================
def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    result = []

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            start = i - j
            end = i - 1
            result.append((start, end))
            j = lps[j - 1]

        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


# =========================
# 2. BOYER MOORE
# =========================
def bad_char_heuristic(pattern):
    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char


def boyer_moore(text, pattern):
    bad_char = bad_char_heuristic(pattern)
    m = len(pattern)
    n = len(text)
    result = []

    s = 0
    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:
            start = s
            end = s + m - 1
            result.append((start, end))
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return result


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_text_from_file(filepath):
    try:
        if filepath.endswith('.txt'):
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        elif filepath.endswith('.pdf'):
            try:
                import PyPDF2
                with open(filepath, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    text = ''
                    for page in reader.pages:
                        text += page.extract_text()
                    return text
            except:
                return ""
        elif filepath.endswith('.docx'):
            try:
                from docx import Document
                doc = Document(filepath)
                return '\n'.join([p.text for p in doc.paragraphs])
            except:
                return ""
    except:
        return ""
    return ""


# =========================
# WEB
# =========================
@app.route("/", methods=["GET", "POST"])
def index():
    result_kmp = []
    result_bm = []
    time_kmp = 0
    time_bm = 0
    text = ""
    pattern = ""
    uploaded_filename = ""

    if request.method == "POST":
        text = request.form.get("text", "")
        pattern = request.form.get("pattern", "")
        
        # Check if file upload exists
        if "file" in request.files:
            file = request.files["file"]
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                uploaded_filename = filename
                
                # Extract text from file
                file_text = extract_text_from_file(filepath)
                if file_text:
                    text = file_text

        if pattern and text:
            # KMP Search with timing
            start_time = time.time()
            result_kmp = kmp_search(text, pattern)
            time_kmp = round((time.time() - start_time) * 1000, 4)  # Convert to milliseconds
            
            # Boyer-Moore Search with timing
            start_time = time.time()
            result_bm = boyer_moore(text, pattern)
            time_bm = round((time.time() - start_time) * 1000, 4)  # Convert to milliseconds

    return render_template("index.html",
                           result_kmp=result_kmp,
                           result_bm=result_bm,
                           time_kmp=time_kmp,
                           time_bm=time_bm,
                           text=text,
                           pattern=pattern,
                           uploaded_filename=uploaded_filename)


if __name__ == "__main__":
    app.run(debug=True)