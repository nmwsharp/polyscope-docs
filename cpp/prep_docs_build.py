# MkDocs macros plugin hook (https://mkdocs-macros-plugin.readthedocs.io).
# Runs at doc build time to populate template variables used across the docs.
# Currently fetches the latest polyscope release tag from GitHub so code
# snippets stay up to date without manual edits.
import urllib.request
import json

def define_env(env):
    try:
        url = "https://api.github.com/repos/nmwsharp/polyscope/releases/latest"
        req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        env.variables["polyscope_latest_version"] = data["tag_name"]
    except Exception:
        env.variables["polyscope_latest_version"] = "POLYSCOPE_LATEST_VERSION_TAG_HERE"
