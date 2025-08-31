import reflex as rx
from login.styles import styles as st

def ReturnButton() -> rx.Component:
    return rx.link(
            rx.box(
                rx.icon("arrow-left", size=24, color=st.Colors.LoginCard.text_primary),
                width="48px",
                height="48px",
                display="flex",
                align_items="center",
                justify_content="center",
                background=st.Colors.LoginCard.glass_card,
                border_radius="50%",
                backdrop_filter="blur(10px)",
                border=f"1px solid {st.Colors.border}",
                _hover={
                    "background": st.Colors.LoginCard.glass_strong,
                    "transform": "scale(1.05)",
                    "border_color": st.Colors.accent
                },
                transition="all 0.3s ease"
            ),
            href="/",
            position="absolute",
            top="32px",
            left="32px",
            z_index="20"
        )

def TermnsConditions() -> rx.Component:
    return rx.center(
        rx.text(
            [
                "Al continuar, aceptas nuestros ",
                rx.link(
                    "Términos de Servicio",
                    href="#",
                    color=st.Colors.accent,
                    _hover={"color": st.Colors.LoginCard.text_primary},
                    transition="colors 0.3s ease"
                ),
                " y ",
                rx.link(
                    "Política de Privacidad",
                    href="#",
                    color=st.Colors.accent,
                    _hover={"color": st.Colors.LoginCard.text_primary},
                    transition="colors 0.3s ease"
                )
            ],
            color=st.Colors.LoginCard.text_muted,
            font_size="0.875rem",
            text_align="center",
            max_width="350px",
            line_height="1.5"
        ),
        margin_top="1.5rem"
    )