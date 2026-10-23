import flet as ft

class Solitaire:
    def __init__(self):
        self.start_positions = {}
        self.drag_group = []

def main(page: ft.Page):
    solitaire = Solitaire()

    def move_on_top(cards, controls):
        """Move o grupo de cartas para a camada da frente"""
        for card in cards:
            controls.remove(card)
            controls.append(card)
        page.update()

    def bounce_back(cards):
        """Devolve o grupo de cartas para a posição original"""
        for card in cards:
            card.top = solitaire.start_positions[card]["top"]
            card.left = solitaire.start_positions[card]["left"]
        page.update()

    def place(cards, slot):
        """Encaixa o grupo no slot, empilhando sob as cartas já existentes"""
        # Conta quantas cartas já estão neste slot (excluindo as que estão sendo arrastadas)
        cards_in_slot = [c for c in all_cards if c not in cards and c.left == slot.left]
        
        # A posição base no eixo Y começa após a última carta
        base_top = slot.top + (len(cards_in_slot) * 30)
        
        for i, card in enumerate(cards):
            card.top = base_top + (i * 30)
            card.left = slot.left
        page.update()

    def start_drag(e: ft.DragStartEvent):
        dragged_card = e.control
        solitaire.drag_group = [dragged_card]

        # Agrupa as cartas que estão na mesma coluna e abaixo da carta clicada
        for card in all_cards:
            if (
                card != dragged_card 
                and card.left == dragged_card.left 
                and card.top > dragged_card.top
            ):
                solitaire.drag_group.append(card)

        # Ordena para garantir que a pilha não inverta a ordem
        solitaire.drag_group.sort(key=lambda c: c.top)

        move_on_top(solitaire.drag_group, controls)
        
        for card in solitaire.drag_group:
            solitaire.start_positions[card] = {
                "top": card.top,
                "left": card.left,
            }
        page.update()

    def drag(e: ft.DragUpdateEvent):
        # Move todo o grupo simultaneamente
        for card in solitaire.drag_group:
            card.top = max(0, card.top + e.local_delta.y)
            card.left = max(0, card.left + e.local_delta.x)
            card.update()

    def drop(e: ft.DragEndEvent):
        main_card = solitaire.drag_group[0]
        
        for slot in slots:
            # Calcula o alvo dinâmico baseado em quantas cartas já existem no slot
            cards_in_slot = [c for c in all_cards if c not in solitaire.drag_group and c.left == slot.left]
            target_top = slot.top + (len(cards_in_slot) * 30)
            
            # Verifica a proximidade com o fundo da pilha no slot
            if (
                abs(main_card.left - slot.left) < 30
                and abs(main_card.top - target_top) < 40
            ):
                place(solitaire.drag_group, slot)
                return

        bounce_back(solitaire.drag_group)

    # slots
    slot0 = ft.Container(width=70, height=100, left=0, top=0, border=ft.Border.all(1))
    slot1 = ft.Container(width=70, height=100, left=200, top=0, border=ft.Border.all(1))
    slot2 = ft.Container(width=70, height=100, left=300, top=0, border=ft.Border.all(1))
    slots = [slot0, slot1, slot2]

    # cartas
    card1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=0,
        top=0,
        content=ft.Container(
            image=ft.DecorationImage(src="card1.png", fit="cover"),
            width=70, 
            height=100,
            border_radius=5
        ),
    )

    card2 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=100,
        top=0,
        content=ft.Container(
            image=ft.DecorationImage(src="card2.png", fit="cover"),
            width=70, 
            height=100,
            border_radius=5
        ),
    )

    card3 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=200,
        top=0,
        content=ft.Container(
            image=ft.DecorationImage(src="card3.png", fit="cover"),
            width=70, 
            height=100,
            border_radius=5
        ),
    )

    all_cards = [card1, card2, card3]
    controls = [slot0, slot1, slot2, card1, card2, card3]

    page.add(ft.Stack(controls=controls, width=1000, height=500))

    # deal cards
    place(all_cards, slot0)

ft.run(main, assets_dir="assets")