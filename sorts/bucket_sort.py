def name():
    return "Bucket sort"

def sort(my_list: list) -> list:
    if len(my_list) == 0:
        return []
    min_value, max_value = min(my_list), max(my_list)
    bucket_count = int(max_value - min_value) + 1
    buckets: list[list] = [[] for _ in range(bucket_count)]

    for i in my_list:
        buckets[int(i - min_value)].append(i)

    return [v for bucket in buckets for v in sorted(bucket)]
