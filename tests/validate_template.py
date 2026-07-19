from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "index.html"
FORBIDDEN_ASSETS = {
    "profile.jpg",
    "pub-1.jpg",
    "pub-2.jpg",
    "pub-3.jpg",
    "pub-4.jpg",
    "university-logo-1.png",
    "university-logo-2.png",
    "university-logo-3.png",
}


class TemplateParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.local_assets: set[str] = set()
        self.errors: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html" and values.get("lang") != "en":
            self.errors.append("html lang must match the English template content")
        if values.get("target") == "_blank":
            rel = set((values.get("rel") or "").split())
            if not {"noopener", "noreferrer"}.issubset(rel):
                self.errors.append("target=_blank link lacks noopener noreferrer")
        if any(name.lower().startswith("on") for name in values):
            self.errors.append(f"inline event handler on <{tag}>")
        if tag == "img" and values.get("src", "").startswith("assets/"):
            self.local_assets.add(values["src"])


def main() -> int:
    text = HTML.read_text(encoding="utf-8")
    parser = TemplateParser()
    parser.feed(text)
    for relative in parser.local_assets:
        if not (ROOT / relative).is_file():
            parser.errors.append(f"missing local asset: {relative}")
    referenced_names = {Path(path).name for path in parser.local_assets}
    stale = sorted(referenced_names & FORBIDDEN_ASSETS)
    if stale:
        parser.errors.append("personal assets still referenced: " + ", ".join(stale))
    if '<meta name="description"' not in text:
        parser.errors.append("missing description metadata")
    if parser.errors:
        raise SystemExit("\n".join(parser.errors))
    print(f"template valid; {len(parser.local_assets)} neutral local assets referenced")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
