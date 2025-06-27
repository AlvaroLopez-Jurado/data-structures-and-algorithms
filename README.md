
# 📚 Data Structures and Algorithms

Este repositorio contiene implementaciones de estructuras de datos y algoritmos clásicos en Python. Está diseñado como recurso educativo para estudiantes, desarrolladores y entusiastas de la informática que deseen mejorar su comprensión de los fundamentos de la programación.

---

## 🎯 Objetivo

Proporcionar una colección clara y bien organizada de algoritmos y estructuras de datos, junto con pruebas automatizadas, para facilitar el aprendizaje, la práctica y la preparación para entrevistas técnicas.

---

## 📂 Contenido
```text
algorithms-and-data-structures-main/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── .gitignore
├── README.md
├── algorithms/
│   ├── dinamyc_programming/
│   │   ├── fibonacci.py
│   │   ├── knapsack.py
│   │   ├── lcs.py
│   │   └── lis.py
│   ├── graphs/
│   │   ├── bfs.py
│   │   └── dijkstra.py
│   ├── math/
│   │   ├── gcd.py
│   │   ├── lcm.py
│   │   └── sieve_of_eratosthenes.py
│   ├── recursion/
│   │   ├── factorial.py
│   │   └── tower_of_hanoi.py
│   ├── search/
│   │   ├── binary_search.py
│   │   ├── exponential_search.py
│   │   ├── interpolation_search.py
│   │   ├── jump_search.py
│   │   ├── linear_search.py
│   │   └── ternary_search.py
│   └── sorting/
│       ├── bubble_sort.py
│       ├── bucket_sort.py
│       ├── counting_sort.py
│       ├── heap_sort.py
│       ├── insertion_sort.py
│       ├── merge_sort.py
│       ├── quick_sort.py
│       ├── radix_sort.py
│       └── shell_sort.py
├── data_structures/
│   ├── graph/
│   │   └── graph.py
│   ├── hash_table/
│   │   └── hash_table.py
│   ├── linked_list/
│   │   ├── doubly_linked_list.py
│   │   └── singly_linked_list.py
│   ├── min_heap/
│   │   └── min_heap.py
│   ├── queue/
│   │   └── queue.py
│   ├── stack/
│   │   └── stack.py
│   ├── tree/
│   │   ├── avl_tree.py
│   │   ├── binary_search_tree.py
│   │   └── trie.py
│   └── union_find/
│       └── union_find.py
├── foulder_tree.py
└── tests/
    ├── test_dinamyc_programming.py
    ├── test_factorial.py
    ├── test_graph.py
    ├── test_graphs.py
    ├── test_hash_table.py
    ├── test_linked_list.py
    ├── test_math.py
    ├── test_min_heap.py
    ├── test_queue.py
    ├── test_search.py
    ├── test_sorting.py
    ├── test_stack.py
    ├── test_tree.py
    ├── test_trie.py
    └── test_union_find.py
```
---

## 🧠 Estructuras de datos implementadas

- Listas enlazadas (simples y dobles)
- Pilas (Stacks)
- Colas (Queues)
- Árboles binarios de búsqueda
- Tablas hash
- Grafos

---

## 📐 Algoritmos implementados

- Ordenamiento: Bubble Sort, Merge Sort, Quick Sort
- Búsqueda: Búsqueda binaria, BFS, DFS
- Programación dinámica: Fibonacci, Subproblemas
- Matemáticos: Factorial, operaciones básicas

---

## 🛠️ Tecnologías

- Python 3.8+
- Pytest para testing
- Estructura modular por carpetas

---

## 🚀 Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/AlvaroLopez-Jurado/data-structures-and-algorithms.git
   cd data-structures-and-algorithms
   ```

2. Ejecuta los scripts directamente:
   ```bash
   python linked_list/singly_linked_list.py
   ```

3. (Opcional) Usa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

4. Ejecutar tests:
   ```bash
   python -m unittest discover tests
   ```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Puedes abrir un issue o enviar un pull request con mejoras, correcciones o nuevos algoritmos.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## 📬 Contacto

Creado por Álvaro López-Jurado — no dudes en contactarme para sugerencias o colaboraciones.
