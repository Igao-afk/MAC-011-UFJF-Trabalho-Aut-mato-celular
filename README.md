# Simulação de Competição por Espaço (Autômatos Celulares)
**Universidade Federal de Juiz de Fora - MAC011: Introdução à Engenharia Computacional**

**Autores:**
* Isabella Silva Ramos
* Igor José de Almeida Oliveira

---

## 📖 Resumo do Trabalho
Neste trabalho foi investigada a competição por espaço, um processo ecológico no qual diferentes colônias disputam áreas limitadas de um ambiente[cite: 30]. No sistema baseado em grids, cada célula ocupada representa território conquistado[cite: 31].

Utilizamos simulações computacionais para avaliar a dinâmica de crescimento entre duas populações (Verdes e Vermelhas), baseando-se em estudos de autômatos celulares em ecossistemas[cite: 33, 34].

## 🧪 Metodologia e Implementação
O código simula um ambiente de grid bidimensional onde o crescimento ocorre pela ocupação de vizinhos livres[cite: 58, 62].

### Principais Alterações e Parâmetros
Para garantir uma simulação robusta, implementamos:
* **Grid Dinâmico:** Ajuste de tamanho (`tamanho_grid`) para diferentes densidades.
* **Probabilidade de Crescimento:** Controle da chance de ocupação (`prob_crescimento`).
* **Tratamento de Colisões:** Regras para evitar sobreposição imediata.
* **Seed Aleatória:** Garante a reprodutibilidade exata dos experimentos.

## 📊 Resultados Obtidos
A análise foi feita com base em 100 simulações controladas[cite: 200].

### 1. Estatísticas de Vitória
Nenhuma colônia apresentou vantagem absoluta, provando que o resultado depende de condições iniciais e aleatoriedade[cite: 188].

| Resultado | Porcentagem |
| :--- | :--- |
| **Vitória Verdes** | 39,0% |
| **Vitória Vermelhas** | 37,0% |
| **Empates** | 24,0% |
*Fonte: Dados extraídos das simulações (Gráfico 3)[cite: 190, 191, 192].*

### 2. Evolução Temporal
Observou-se que as colônias vermelhas iniciaram com crescimento mais rápido, mas ao final, ambas as populações atingiram valores médios próximos (cerca de 38 células), evidenciando uma **coexistência parcial** no longo prazo[cite: 214].

## 💡 Conclusão
O modelo demonstrou que, mesmo em ambientes competitivos, a estrutura espacial e a aleatoriedade permitem a persistência de múltiplas espécies, refletindo fenômenos reais como mosaicos ecológicos[cite: 229]. A regra de substituição de células foi crucial para evitar o domínio total precoce de uma única espécie[cite: 225].

---
*Agosto de 2025 - Juiz de Fora, MG [cite: 4, 5]*