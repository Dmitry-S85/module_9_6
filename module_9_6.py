# def all_variants(text):
#     if not text:
#         return
#
#     length = len(text)
#     for i in range(length + 1):
#         for j in range(length - i + 1):
#             yield text[j:i + j]
#
# a = all_variants("abc")
# for i in a:
#     print(i)

def all_variants(text):
    if not text:
        return

    length = len(text)
    for i in range(length + 1):
        for j in range(length - i + 1):
            yield text[j:i + j]

a = all_variants("abc")
for i in a:
    print(i)