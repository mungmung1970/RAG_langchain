import copy
import datetime


def load_metadata_template(filepath):
    template = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            key = line.strip()
            if key:
                template[key] = ""
    return template


import copy
import datetime


def load_metadata_template(filepath):
    template = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            key = line.strip()
            if key:
                template[key] = ""
    return template


def create_metadata(row, page, chunk_index, template):
    meta = copy.deepcopy(template)

    # 기본 row 값 입력
    for key in template.keys():
        if key in row:
            meta[key] = row[key]

    # RAG 운영 필드 생성
    notice_id = row.get("notice_id", "")
    meta["document_id"] = notice_id
    meta["page"] = page
    meta["chunk_index"] = chunk_index
    meta["chunk_id"] = f"{notice_id}_p{page}_c{chunk_index}"
    meta["version"] = "v1.0"
    meta["ingested_at"] = datetime.datetime.utcnow().isoformat()

    return meta
