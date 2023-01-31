def solution(citations):
    citations.sort(reversed=True)

    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx

    return len(citations)
