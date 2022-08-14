from typing import List


def gen_chunks(filename: str, chunk_size: int = 100):
    reader = open(filename, "rt", encoding="utf-8")
    chunks: List[str] = list()
    for i, line in enumerate(reader):
        if i % chunk_size == 0 and i > 0:
            yield chunks
            del chunks[:]
        chunks.append(line)
    yield chunks
