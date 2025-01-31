import pymupdf4llm
def process_pdf(path):
    md_text = pymupdf4llm.to_markdown(path)
    return md_text
