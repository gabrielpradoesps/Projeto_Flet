import flet as ft


class Solitaire:
    def __init__(self):
        self.start_top = 0
        self.start_left = 0


def main(page: ft.Page):
    solitaire = Solitaire()

    def move_on_top(card, controls):
        """Coloca a carta no fim da lista (fica por cima)"""
        controls.remove(card)
        controls.append(card)
        page.update()

    def bounce_back(game, card):
        """Devolve a carta para a posição original"""
        card.top = game.start_top
        card.left = game.start_left
        page.update()

    def place(card, slot):
        """Encaixa a carta no slot"""
        card.top = slot.top
        card.left = slot.left
        page.update()

    def start_drag(e: ft.DragStartEvent):
        move_on_top(e.control, controls)
        solitaire.start_top = e.control.top
        solitaire.start_left = e.control.left
        e.control.update()

    def drag(e: ft.DragUpdateEvent):
        e.control.top = max(0, e.control.top + e.local_delta.y)
        e.control.left = max(0, e.control.left + e.local_delta.x)
        e.control.update()

    def drop(e: ft.DragEndEvent):
        for slot in slots:
            if (
                abs(e.control.top - slot.top) < 20
                and abs(e.control.left - slot.left) < 20
            ):
                place(e.control, slot)
                e.control.update()
                return
        bounce_back(solitaire, e.control)
        e.control.update()

    # slots
    slot0 = ft.Container(width=70, height=100, left=0, top=0, border=ft.Border.all(1))
    slot1 = ft.Container(width=70, height=100, left=200, top=0, border=ft.Border.all(1))
    slot2 = ft.Container(width=70, height=100, left=300, top=0, border=ft.Border.all(1))
    slots = [slot0, slot1, slot2]

    # cartas com imagens
    card1 = ft.GestureDetector(
        mouse_cursor=ft.MouseCursor.MOVE,
        drag_interval=5,
        on_pan_start=start_drag,
        on_pan_update=drag,
        on_pan_end=drop,
        left=0,
        top=0,
        content=ft.Container(
            image=ft.DecorationImage(
                src="card1.png",
                fit="cover",
            ),
            width=70,
            height=100,
            border_radius=5,
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
            image=ft.DecorationImage(
                src="card2.png",
                fit="cover",
            ),
            width=70,
            height=100,
            border_radius=5,
        ),
    )

    controls = [slot0, slot1, slot2, card1, card2]
    page.add(ft.Stack(controls=controls, width=1000, height=500))

    # distribui as cartas no slot0
    place(card1, slot0)
    place(card2, slot0)


ft.run(main, assets_dir="assets")