from bs4 import BeautifulSoup
from pathlib import Path

SUFFIXES = ["*.html", "*.php"]

file_count = 0
code_snippet_count = 0
test1 = True
test2 = True

def _get_code_snippet(pre_content):
    content = str(pre_content).split('>', maxsplit=1)[1].rsplit("</pre>", 1)[0]
    print(content)
    return content

for path in [p for suffix in SUFFIXES for p in Path().resolve().rglob(suffix)]:
    with open(path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'html.parser')

        for code_section in soup.find_all("div", class_="section-example-container"):
            for code_snippet in code_section.find_all('pre', {'class' : 'python'}):
                # test case 1
                if test1:
                    clean_snippet = _get_code_snippet(code_snippet)
                    
                    test1 = False
                code_snippet_count += 1
                
        for code_section in soup.find_all("div", class_="python section-example-container"):
            for code_snippet in code_section.find_all('pre'):
                # test case 2
                if test2:
                    clean_snippet = _get_code_snippet(code_snippet)
                    test2 = False
                code_snippet_count += 1
            
    file_count += 1
            
print(f"Found {code_snippet_count} pieces of code snippets from {file_count} files.")