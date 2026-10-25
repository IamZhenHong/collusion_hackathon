"""Render inherited/REPORT.md as a PDF laid out like the Apart Research submission template.

Title block (title, author / affiliation, "With Apart Research"), boxed abstract, numbered sections,
figures with captions kept together, letter pages with 1-inch margins. Uses headless Chrome.

    uv run --with markdown --with pymupdf python tools/build_report.py
    -> inherited/report_build/Inherited_Collusion_report.pdf (+ page count and where References starts)
"""

import re
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "inherited" / "REPORT.md"
OUT = ROOT / "inherited" / "report_build"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: Letter; margin: 0.9in 0.95in; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 10.2pt; line-height: 1.42; color: #111; }
h1.title { font-size: 19pt; text-align: center; margin: 0 0 10pt; line-height: 1.2; font-weight: bold; }
p.subtitle { font-size: 13pt; text-align: center; margin: -4pt 0 12pt; line-height: 1.3; }
p.authors { text-align: center; margin: 0; font-size: 10.5pt; }
p.with { text-align: center; font-weight: bold; margin: 2pt 0 12pt; font-size: 10.5pt; }
div.abstract { border: 1px solid #999; padding: 8pt 11pt; margin: 0 0 14pt; }
div.abstract h2 { text-align: center; font-size: 11pt; margin: 0 0 4pt; }
div.abstract p { margin: 0; text-align: justify; }
h2 { font-size: 13pt; margin: 14pt 0 5pt; font-weight: bold; break-after: avoid; }
h3 { font-size: 11pt; margin: 10pt 0 4pt; font-weight: bold; break-after: avoid; }
p { margin: 0 0 6pt; text-align: justify; }
ol, ul { margin: 0 0 6pt; padding-left: 18pt; }
li { margin-bottom: 2pt; }
code { font-family: "Courier New", monospace; font-size: 9pt; }
figure { margin: 8pt 0 10pt; break-inside: avoid; }
figure img { width: 100%; display: block; }
figure.narrow img { width: 82%; margin: 0 auto; }
figcaption { font-size: 8.8pt; line-height: 1.35; margin-top: 4pt; text-align: justify; }
table { border-collapse: collapse; width: 100%; font-size: 8.8pt; margin: 6pt 0 4pt; break-inside: avoid; }
th, td { border-bottom: 1px solid #bbb; padding: 3pt 4pt; text-align: left; vertical-align: top; }
th { border-bottom: 1.5px solid #333; }
p.tcap { font-size: 8.8pt; line-height: 1.35; margin-top: 2pt; }
.pagebreak { break-before: page; }
a { color: #1a4fa0; text-decoration: none; }
"""

WIDTH = {"fig_example.png": 82, "fig_simple.png": 78, "fig7_copy_or_learn.png": 90, "fig_enforcement.png": 82,
         "fig_saydo.png": 90, "fig2_fixes_gpt41mini_PI.png": 75, "fig1_carriers_gpt41mini_PI.png": 72}


def build_html(md_text: str) -> str:
    title_m = re.match(r"# (.+?)\n", md_text)
    title = title_m.group(1)
    # "Headline: explanation" -> large headline, explanation as a subtitle line
    head, _, sub = title.partition(": ")
    rest = md_text[title_m.end():]
    authors, with_line, rest = rest.strip().split("\n\n", 2)
    abstract, rest = rest.split("## 1. Introduction", 1)
    abstract = abstract.replace("## Abstract", "").strip()
    body = markdown.markdown("## 1. Introduction" + rest, extensions=["tables"])
    # figures: <p><img .../></p> followed by <p><em>Figure ...</em></p>
    def fig(m):
        src, cap = m.group(1), m.group(2)
        w = WIDTH.get(Path(src).name, 100)
        return (f'<figure><img src="{src}" alt="" style="width:{w}%;margin:0 auto"/>'
                f'<figcaption>{cap}</figcaption></figure>')
    body = re.sub(r'<p><img alt="[^"]*" src="([^"]+)" /></p>\s*<p><em>(.+?)</em></p>', fig, body, flags=re.S)
    # table captions
    body = re.sub(r"(<table>.+?</table>)\s*<p><em>(Table .+?)</em></p>",
                  r'<div style="break-inside: avoid">\1<p class="tcap"><em>\2</em></p></div>', body, flags=re.S)
    # appendices start on a new page
    body = body.replace("<h2>References</h2>", '<h2 class="pagebreak">References</h2>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>{title}</title><style>{CSS}</style></head><body>
<h1 class="title">{head}</h1>
{f'<p class="subtitle">{sub}</p>' if sub else ""}
<p class="authors">{markdown.markdown(authors)[3:-4]}</p>
<p class="with">{with_line}</p>
<div class="abstract"><h2>Abstract</h2>{markdown.markdown(abstract)}</div>
{body}
</body></html>"""


def main():
    OUT.mkdir(exist_ok=True)
    html = build_html(SRC.read_text())
    html_path = OUT / "report.html"
    # figure paths in REPORT.md are relative to inherited/; the HTML sits one level deeper
    html_path.write_text(html.replace('src="../results/', 'src="../../results/'))
    pdf = OUT / "Inherited_Collusion_report.pdf"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html_path.as_uri()], check=True, capture_output=True)
    import fitz  # pymupdf

    doc = fitz.open(pdf)
    ref_page = next((i + 1 for i, p in enumerate(doc) if "References" in p.get_text() and
                     re.search(r"^References\s*$", p.get_text(), re.M)), None)
    print(f"{pdf}: {doc.page_count} pages; References starts on page {ref_page} "
          f"(main text = pages 1-{(ref_page or doc.page_count + 1) - 1})")
    for i, page in enumerate(doc):
        page.get_pixmap(dpi=70).save(OUT / f"page_{i + 1:02d}.png")


if __name__ == "__main__":
    sys.exit(main())
