from pathlib import Path
from collections import Counter
import re,math
def load_text(path):
 p=Path(path)
 if p.suffix.lower()==".pdf":
  try: from pypdf import PdfReader
  except ImportError as e: raise RuntimeError("Install pypdf") from e
  return "\n".join(page.extract_text() or "" for page in PdfReader(str(p)).pages)
 return p.read_text(encoding="utf-8",errors="ignore")
def chunk_text(text,chunk_size=700,overlap=100):
 if chunk_size<=0 or overlap<0 or overlap>=chunk_size: raise ValueError("Require chunk_size > overlap >= 0")
 words=text.split(); chunks=[]; start=0
 while start<len(words):
  end=min(start+chunk_size,len(words)); chunks.append(" ".join(words[start:end]))
  if end==len(words): break
  start=end-overlap
 return chunks
def tokenize(s): return re.findall(r"[a-z0-9]+",s.lower())
def retrieve(query,chunks,top_k=3):
 docs=[tokenize(c) for c in chunks]; terms=set(tokenize(query)); n=len(docs); df=Counter(t for d in docs for t in set(d)); out=[]
 for i,d in enumerate(docs):
  counts=Counter(d); score=sum((1+math.log(counts[t]))*math.log(1+n/(1+df[t])) for t in terms if counts[t])
  out.append((score,i,chunks[i]))
 return [x for x in sorted(out,reverse=True)[:top_k] if x[0]>0]
def grounded_answer(query,hits):
 if not hits: return "No relevant passage found in the supplied document. Rephrase or add a source."
 return "LOCAL EXTRACTIVE DEMO — no LLM called.\nRelevant excerpts:\n"+"\n\n".join(f"[Chunk {i}] {c}" for _,i,c in hits)+"\n\nQuestion: "+query+"\nReview the excerpts; this demo does not infer facts beyond them."
