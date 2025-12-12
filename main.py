from pipeline.build_index import build_index

row = {
    "notice_id": "A2025-001",
    "project_name": "클라우드 구축 사업",
    "ordering_agency": "산업부",
    "file_name": "notice.pdf",
}

text = "여기에 PDF에서 추출한 전체 텍스트 넣기"
page = 1

build_index(row, page, text)
