from rag_core import chunk_text,retrieve
def test_overlap():
 c=chunk_text("one two three four five six",4,1)
 assert c[0]=="one two three four" and c[1].startswith("four")
def test_retrieval():
 hits=retrieve("document chunks",["blue sky","RAG retrieves relevant document chunks"],1)
 assert hits and "document chunks" in hits[0][2]
