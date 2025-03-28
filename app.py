from flask import Flask, request, render_template_string
from verify import validate_username

app = Flask(__name__)

# HTML form template
HTML = """
<h2>Username Validator</h2>
<form method="POST">
  <input name="username" placeholder="Enter username">
  <button type="submit">Validate</button>
</form>

{% if result is not none %}
  <p><strong>{{ result }}</strong></p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        username = request.form["username"]
        result = "✅ Valid username" if validate_username(username) else "❌ Invalid username"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
