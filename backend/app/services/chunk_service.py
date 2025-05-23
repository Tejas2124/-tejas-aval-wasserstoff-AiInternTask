from typing import List

def chunk_text(text: str, chunk_size: int = 500) -> List[str]:
    words = text.split()
    chunks = [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
    return chunks
