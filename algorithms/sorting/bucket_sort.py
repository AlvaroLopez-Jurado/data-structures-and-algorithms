def bucket_sort(arr):
    if not arr:
        return []

    # Determinar el valor mínimo y máximo
    min_val = min(arr)
    max_val = max(arr)

    # Número de cubetas
    bucket_count = len(arr)
    bucket_range = (max_val - min_val) / bucket_count + 1e-9  # Evita división por cero

    # Crear cubetas vacías
    buckets = [[] for _ in range(bucket_count)]

    # Distribuir los elementos en las cubetas
    for num in arr:
        index = int((num - min_val) / bucket_range)
        buckets[index].append(num)

    # Ordenar cada cubeta y concatenar los resultados
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr
