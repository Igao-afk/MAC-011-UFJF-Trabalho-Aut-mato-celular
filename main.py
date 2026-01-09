import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Função para desenhar a grade com cores por espécie
def draw_frame(grid):
    rgb_grid = np.zeros((grid.shape[0], grid.shape[1], 3))
    for value, color in color_dict.items():
        rgb_grid[grid == value] = color
    return rgb_grid

def animation(initial_grid, rule, frames=200, interval=100):
    initial_grid = np.array(initial_grid)
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.axis("off")
    img = ax.imshow(draw_frame(initial_grid), interpolation="nearest")

    grid = initial_grid
    grid_history = [grid.copy()]

    def update(frame):
        nonlocal grid
        grid = rule(grid)
        grid_history.append(grid.copy())
        img.set_data(draw_frame(grid))
        return img,

    anim = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)
    plt.close(fig)
    return anim, grid_history

# Cores: branco vazio, vermelho espécie A, azul espécie B
color_dict = {
    0: (1, 1, 1),    # vazio
    1: (1, 0, 0),    # espécie A
    2: (0, 0, 1)     # espécie B
}

# Atualização com competição
def update_grid(grid):
    new_grid = grid.copy()
    rows, cols = grid.shape

    for i in range(rows):
        for j in range(cols):
            # Contagem de vizinhos por espécie
            neighbors_A = 0
            neighbors_B = 0

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == 1:
                            neighbors_A += 1
                        elif grid[ni][nj] == 2:
                            neighbors_B += 1

            total_neighbors = neighbors_A + neighbors_B
            current_state = grid[i][j]

            # Regras de sobrevivência
            if current_state == 1:
                if neighbors_A < 2 or neighbors_A > 3:
                    new_grid[i][j] = 0  # morre
                elif neighbors_B > neighbors_A + 1:  
                    new_grid[i][j] = 2  # invadido
            elif current_state == 2:
                if neighbors_B < 2 or neighbors_B > 3:
                    new_grid[i][j] = 0
                elif neighbors_A > neighbors_B + 1:
                    new_grid[i][j] = 1

            # Nascimento em célula vazia
            if current_state == 0:
                if total_neighbors == 3:
                    if neighbors_A > neighbors_B:
                        new_grid[i][j] = 1
                    elif neighbors_B > neighbors_A:
                        new_grid[i][j] = 2
                    else:
                        new_grid[i][j] = random.choice([1, 2])  # empate

    return new_grid

# Parâmetros
grid_size = (100, 100)
steps = 300
densidade_A = 0.15
densidade_B = 0.15

# Grade inicial aleatória com duas espécies
initial_grid = np.zeros(grid_size, dtype=int)
mask_A = np.random.rand(*grid_size) < densidade_A
mask_B = (np.random.rand(*grid_size) < densidade_B) & (~mask_A)

initial_grid[mask_A] = 1
initial_grid[mask_B] = 2

# Criar animação
anim, grid_history = animation(initial_grid, update_grid, steps, 50)
HTML(anim.to_jshtml())

# Estatísticas
species_A_counts = [(grid == 1).sum() for grid in grid_history]
species_B_counts = [(grid == 2).sum() for grid in grid_history]

plt.figure(figsize=(10, 6))
plt.plot(species_A_counts, label="Espécie A", color='red')
plt.plot(species_B_counts, label="Espécie B", color='blue')
plt.xlabel("Tempo")
plt.ylabel("Número de células")
plt.title("Competição por espaço entre espécies")
plt.legend()
plt.grid(True)
plt.show()
