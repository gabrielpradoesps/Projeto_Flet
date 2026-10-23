Tenho um código base de um jogo de Paciência (Solitaire) construído em Python com o framework Flet, onde atualmente consigo arrastar apenas uma carta por vez em direção aos slots. 

Preciso que você altere meu código para adicionar a mecânica de **arrastar múltiplas cartas de uma vez** e **empilhamento dinâmico**. Aplique as seguintes regras sem alterar o layout atual ou quebrar a lógica de UI:

1. **Lógica de Agrupamento (Start Drag):**
   * Ao clicar em uma carta para arrastar, o código deve buscar todas as outras cartas no jogo que estejam na mesma coluna (`left` igual) e posicionadas abaixo dela na pilha (valor de `top` maior).
   * Agrupe a carta clicada e essas cartas adicionais em uma lista (ex: `drag_group`) e salve a coordenada inicial exata de cada uma delas.

2. **Arrasto Sincronizado (Drag Update):**
   * Durante o evento de movimento do mouse, aplique o delta de deslocamento de forma simultânea a **todas as cartas** do grupo, para que se movam juntas pela tela sem perder a distância (offset) entre elas.

3. **Alvo Dinâmico e Colisão (Drop):**
   * Ao soltar o clique, não verifique a colisão apenas com as coordenadas fixas do slot vazio. 
   * Conte quantas cartas já existem fisicamente no slot de destino. O alvo para validar o drop deve ser o fundo da pilha existente (ex: `slot.top + (cartas_no_slot * 30)`).
   * Se a carta principal do grupo de arraste atingir essa zona alvo (margem de ~30 a 40 pixels), permita o encaixe. Caso contrário, devolva todo o grupo para as posições originais.

4. **Encaixe em Cascata (Place):**
   * Ao encaixar o grupo com sucesso em um slot, posicione-o a partir do fundo da pilha atual desse slot.
   * Mantenha o espaçamento visual de 30 pixels no eixo Y entre cada carta adicionada, formando uma cascata.