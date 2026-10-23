
Atue como um desenvolvedor especialista em Python e no framework Flet.

Preciso do código completo de uma aplicação GUI simples de Paciência (Solitaire) com suporte a mecânica de Arrastar e Soltar (Drag & Drop).

Requisitos do projeto:
1. Estrutura de Classe:
   - Utilize uma classe `Solitaire` para controlar as coordenadas de posição inicial (`start_top`, `start_left`) durante os movimentos de arrastar.

2. Lógica de Drag & Drop:
   - Usar `ft.GestureDetector` para capturar os eventos do mouse (`on_pan_start`, `on_pan_update`, `on_pan_end`).
   - `move_on_top`: Colocar a carta atual no fim da lista de controles para que fique no topo da camada visual.
   - `bounce_back`: Devolver a carta para a posição inicial de onde o arrasto começou se for solta longe de um slot.
   - `place`: Encaixar a carta na posição exata do slot se for solta a uma distância menor que 20 pixels dele.

3. Interface e Layout:
   - Utilizar um `ft.Stack` de 1000x500 para permitir posicionamento absoluto via `left` e `top`.
   - 3 slots de destino (`slot0`, `slot1`, `slot2`) com bordas visíveis e tamanho 70x100 pixels.
   - 2 cartas (`card1` e `card2`) estilizadas usando `ft.Container` com imagens em segundo plano (`ft.DecorationImage` com `fit="cover"`), carregadas a partir da pasta local `assets` (`card1.png` e `card2.png`).

4. Execução:
   - Iniciar com `ft.run(main, assets_dir="assets")` para configurar corretamente a pasta de arquivos estáticos.

Por favor, forneça o código completo, funcional e compatível com as versões recentes do Flet.
