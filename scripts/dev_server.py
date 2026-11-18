import http.server
import os
import urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def translate_path(self, path):
        parsed = urllib.parse.urlsplit(path)
        clean_path = parsed.path
        fs_path = super().translate_path(clean_path)
        if os.path.isdir(fs_path) or os.path.splitext(fs_path)[1]:
            return fs_path
        candidate = fs_path + ".html"
        if os.path.isfile(candidate):
            return candidate
        return fs_path


if __name__ == "__main__":
    port = 8080
    server = http.server.ThreadingHTTPServer(("0.0.0.0", port), CleanUrlHandler)
    print(f"Serving {ROOT} with clean URLs at http://localhost:{port}")
    server.serve_forever()
