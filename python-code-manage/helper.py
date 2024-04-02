import re

SUFFIXES = ["*.html", "*.php"]
EXCEPTIONS = {
    "ETF": "etf",
    "SMA": "sma",
    "EMA": "ema"
}

def get_code_snippet(pre_content):
    content = str(pre_content).split('>', maxsplit=1)[1].rsplit("</pre>", 1)[0]
    return content

def conversion(content):
    for original, new in EXCEPTIONS.items():
        if original in content:
            content = content.replace(original, new)
        
    methods = re.findall(r"def\s+([A-Za-z0-9_]+)\s*\(", content)

    for method in methods:
        snake_case_method = _title_to_snake_case(method)
        content = content.replace(f"def {method}(", f"def {snake_case_method}(")
    
    methods = re.findall(r"\.([A-Za-z0-9_]+)", content)

    for method in methods:
        snake_case_method = _title_to_snake_case(method)
        content = content.replace(f".{method}", f".{snake_case_method}")
        
    return content

def _title_to_snake_case(title):
    # for whole method is upper case: indicators
    if title.isupper():
        return title.lower()
    
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', title).lower()
    return snake_case