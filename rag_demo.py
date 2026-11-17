from pathlib import Path
from rag_core import load_text,chunk_text,retrieve,grounded_answer
def main():
 p=Path(__file__).parent/"sample_knowledge.txt"; chunks=chunk_text(load_text(p),80,15)
 print("Loaded local sample into",len(chunks),"chunks.")
 while True:
  q=input("\nQuestion (/exit to quit): ")
  if q=="/exit": break
  print(grounded_answer(q,retrieve(q,chunks)))
if __name__=="__main__": main()
