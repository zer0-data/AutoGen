import os
import io
import zipfile
from pathlib import Path
from flask import Flask, render_template, request, redirect, url_for, send_file, jsonify, flash

from backend import create_and_deploy_project


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key")

    @app.route("/", methods=["GET"]) 
    def index():
        return render_template("index.html")

    @app.route("/generate", methods=["POST"]) 
    def generate():
        prompt = request.form.get("prompt", "").strip()
        project_name = request.form.get("project_name", "").strip() or None

        # Optional image upload
        img_path = None
        file = request.files.get("image")
        if file and file.filename:
            uploads_dir = Path("uploads")
            uploads_dir.mkdir(parents=True, exist_ok=True)
            img_path = str(uploads_dir / file.filename)
            file.save(img_path)

        auto_deploy = request.form.get("auto_deploy") == "on"
        username = request.form.get("github_username") or None
        repo_name = request.form.get("repo_name") or None
        token = request.form.get("github_token") or os.getenv("GITHUB_TOKEN")

        if not prompt:
            flash("Prompt is required", "error")
            return redirect(url_for("index"))

        result = create_and_deploy_project(
            prompt=prompt,
            project_name=project_name,
            github_token=token if auto_deploy else None,
            username=username if auto_deploy else None,
            repo_name=repo_name if auto_deploy else None,
            auto_deploy=auto_deploy,
            img=img_path,
        )

        if not result.get("success"):
            flash(result.get("error", "Generation failed"), "error")
            return redirect(url_for("index"))

        return render_template("result.html", result=result)

    @app.route("/download", methods=["GET"]) 
    def download():
        project_path = request.args.get("path")
        if not project_path or not os.path.isdir(project_path):
            flash("Invalid project path", "error")
            return redirect(url_for("index"))

        # Create in-memory zip
        mem = io.BytesIO()
        with zipfile.ZipFile(mem, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(project_path):
                for f in files:
                    full = os.path.join(root, f)
                    arcname = os.path.relpath(full, project_path)
                    zf.write(full, arcname)
        mem.seek(0)
        proj = Path(project_path).name
        return send_file(mem, as_attachment=True, download_name=f"{proj}.zip")

    return app


if __name__ == "__main__":
    app = create_app()
    debug = os.getenv("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=debug, use_reloader=False)
