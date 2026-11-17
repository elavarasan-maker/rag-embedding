# Module 04 — RAG, Embeddings & Vector Databases
Pipeline: document ingestion → text extraction → chunking → embeddings → vector index → retrieval → context assembly → LLM answer → grounding/citations.

Chunking improves retrieval granularity and avoids sending entire large documents. Overlap can preserve context across chunk boundaries but excessive overlap duplicates text. Embeddings represent text as vectors; similarity is a relevance signal, not proof. A vector database supports vector search and often metadata filtering.

This project implements a transparent lexical TF-IDF-style baseline so it runs offline. It is **not** semantic embedding search or a production vector DB. Production improvements: embedding model, FAISS/Chroma/managed vector DB, metadata filters, reranking, citations, access control and evaluation. Evaluate Recall@k, answer faithfulness, relevance and abstention using labelled questions.
