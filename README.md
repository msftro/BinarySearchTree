# Algoritmo Binary Search Tree (BST)

<img src="https://github.com/user-attachments/assets/3d7c502e-70ac-4046-8e8d-a21c7b455e90">

## Resumo

Um **Binary Search Tree (BST)**, ou Árvore de Busca Binária, é uma estrutura de dados hierárquica na qual cada nó possui no máximo dois filhos, conhecidos como filho esquerdo e filho direito. A principal característica de uma BST é que, para qualquer nó:

- Todos os valores na subárvore esquerda são menores ou iguais ao valor do nó.
- Todos os valores na subárvore direita são maiores que o valor do nó.

<p align="center">
  <img src="https://github.com/user-attachments/assets/e98b58f1-2c9b-4322-ba91-6842a95841c2" alt="GIF BST">
</p>

## Operações Básicas

1. **Inserção**: Adiciona um novo valor à árvore, mantendo a propriedade da BST.
2. **Busca**: Encontra um valor específico na árvore, aproveitando a propriedade de ordenação.
3. **Remoção**: Remove um valor da árvore, ajustando a estrutura para manter a propriedade da BST.
4. **Travessia (Traversal)**: Visita todos os nós da árvore em uma ordem específica, como:
   - **Em-ordem (In-order)**: Visita a subárvore esquerda, o nó, e depois a subárvore direita. Resulta em uma lista de valores ordenados.
   - **Pré-ordem (Pre-order)**: Visita o nó antes de suas subárvores.
   - **Pós-ordem (Post-order)**: Visita as subárvores antes do nó.

## O Que Pode Ser Aprendido com o Estudo de BSTs

1. **Estrutura de Dados**: Entender como estruturas de dados hierárquicas funcionam e como manipulá-las.
2. **Algoritmos de Ordenação e Busca**: Aprender sobre técnicas eficientes para ordenar e buscar dados.
3. **Recursão**: Explorar o uso de recursão em algoritmos de travessia e manipulação de árvores.
4. **Complexidade**: Avaliar o desempenho das operações em termos de complexidade de tempo e espaço.

## Implementação no Código

No código fornecido:

- **TreeNode**: Representa um nó da árvore com dados e referências para filhos esquerdo e direito.
- **BinarySearchTree**: Gerencia a árvore, fornecendo métodos para inserção, travessia e recuperação dos dados ordenados.
- **Método `insert`**: Insere valores na árvore mantendo a propriedade de BST.
- **Método `get_sorted`**: Realiza a travessia em-ordem para coletar os valores em uma lista ordenada.

Esse código pode ser usado para implementar e entender os conceitos fundamentais de BSTs e explorar como diferentes operações afetam a estrutura da árvore.

## Visualização do Algoritmo

Para uma visualização interativa do algoritmo Binary Search Tree, você pode visitar a página [Binary Search Tree](https://www.cs.usfca.edu/~galles/visualization/BST.html). Essa ferramenta permite ver como a árvore evolui à medida que os valores são inseridos e removidos.

## Contribuição

Se você deseja contribuir com este projeto, por favor, faça um *fork* do repositório e envie um *pull request* com suas alterações.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma issue ou entrar em contato:

- LinkedIn: [Márcio Ferreira](https://www.linkedin.com/in/ms-ferreira)
