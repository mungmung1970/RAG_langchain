### 1) Chroma DB 생성
### 2) 메타데이터 스키마 설계
### 3) chunk_id 생성 규칙 정의
### 4) 텍스트 청킹
### 5) 임베딩 생성
### 6) Chroma에 저장(ids, documents, embeddings, metadatas)


[사용자 질문]
      │
      ▼
pipelines/rag_pipeline.py
      │
      ├─ retrieval/hybrid.py      ← 문서 후보 검색
      │       ├─ dense.py
      │       └─ lexical.py
      │
      ├─ generation/reranker.py   ← 문서 재정렬
      │
      └─ generation/answer.py     ← 최종 답변 생성
      │
      ▼
[최종 답변 + 출처]