#1

def sum_nested_list(lst):
    total = 0

    for item in lst:
        if isinstance(item, list):
            total += sum_nested_list(item)
        else:
            total += item

    return total

root = [
    5,
    [6, 7],
    [[8, 9], 10]
]

print(sum_nested_list(root))



#2
def count_nested_levels(nested_documents, target_document_id, level=0):
    for doc_id in nested_documents:
        if doc_id == target_document_id:
            return level

        result = count_nested_levels(
            nested_documents[doc_id],
            target_document_id,
            level + 1
        )

        if result != -1:
            return result

    return -1

docs = {
    1: {
        3: {}
    },
    2: {}
}

print(count_nested_levels(docs, 3))  # 1
print(count_nested_levels(docs, 2))  # 0
print(count_nested_levels(docs, 5))  # -1