from rag.pdf_loader import PDFLoader

def test_text_extraction():
    loader = PDFLoader("data/sample.pdf")
    pages = loader.extract_text()
    assert isinstance(pages, list)
