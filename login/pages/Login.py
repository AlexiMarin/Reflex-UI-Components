import reflex as rx
from login.styles import styles as st
from login.state import RegisterState
from login.components.components import ReturnButton, TermnsConditions
from login.state.LoginSate import LoginState

def LoginCard() -> rx.Component:
    """Formulario de login elegante replicando el diseño React original"""
    return rx.box(

        ReturnButton(),
        
        # Formulario principal
        rx.center(
            rx.vstack(
                # Card principal con efecto glass
                rx.box(
                    # Header con icono y títulos
                    rx.center(
                        rx.vstack(
                            # Icono central con corazón animado
                            rx.box(
                                rx.icon(
                                    "user",
                                    size=40,
                                    color=st.Colors.accent
                                ),
                                width="80px",
                                height="80px",
                                display="flex",
                                align_items="center",
                                justify_content="center",
                                background=st.Colors.LoginCard.login_bg,
                                border_radius="50%",
                                box_shadow=st.Colors.LoginCard.shadow_medium,
                                margin_bottom="1.5rem"
                            ),
                            
                            rx.heading(
                                "Bienvenido de vuelta",
                                size="8",
                                color=st.Colors.LoginCard.text_primary,
                                font_weight="500",
                                text_align="center",
                                margin_bottom="0.5rem",
                                font_family="sans-serif"
                            ),
                            rx.text(
                                "Inicia sesión para acceder a tu cuenta",
                                color=st.Colors.LoginCard.text_secondary,
                                text_align="center",
                                margin='0 0 1.5rem 0'
                            ),
                            spacing="2",
                            align="center"
                        )
                    ),
                    
                    # Formulario
                    rx.vstack(
                        # Campo de email con icono
                        rx.vstack(
                            rx.text(
                                "Correo electrónico",
                                font_weight="500",
                                color=st.Colors.LoginCard.text_primary
                            ),
                            rx.box(
                                rx.icon("mail", size=20, color=st.Colors.LoginCard.text_muted, position="absolute", left="12px", top="50%", transform="translateY(-50%)"),
                                rx.input(
                                    placeholder="tu@correo.com",
                                    type="email",
                                    value=LoginState.email,
                                    on_change=LoginState.set_email,
                                    size="3",
                                    width="100%",
                                    height="48px",
                                    padding_left="40px",
                                    background=st.Colors.LoginCard.input_bg,
                                    border=f"1px solid {st.Colors.LoginCard.input_border}",
                                    border_radius="8px",
                                    backdrop_filter="blur(10px)",
                                    color=st.Colors.LoginCard.text_primary,
                                    _focus={
                                        "border_color": st.Colors.accent,
                                        "box_shadow": f"0 0 0 3px rgba(59,130,246,0.2)"
                                    },
                                    transition="all 0.3s ease"
                                ),
                                position="relative",
                                width="100%"
                            ),
                            spacing="2",
                            width="100%",
                            align="start"
                        ),
                        
                        # Campo de contraseña con icono
                        rx.vstack(
                            rx.text(
                                "Contraseña",
                                font_weight="500",
                                color=st.Colors.LoginCard.text_primary
                            ),
                            rx.box(
                                rx.icon("lock", size=20, color=st.Colors.LoginCard.text_muted, position="absolute", left="12px", top="50%", transform="translateY(-50%)"),
                                rx.input(
                                    placeholder="••••••••",
                                    type="password",
                                    value=LoginState.password,
                                    on_change=LoginState.set_password,
                                    size="3",
                                    width="100%",
                                    height="48px",
                                    padding_left="40px",
                                    background=st.Colors.LoginCard.input_bg,
                                    border=f"1px solid {st.Colors.LoginCard.input_border}",
                                    border_radius="8px",
                                    backdrop_filter="blur(10px)",
                                    color=st.Colors.LoginCard.text_primary,
                                    _focus={
                                        "border_color": st.Colors.accent,
                                        "box_shadow": f"0 0 0 3px rgba(59,130,246,0.2)"
                                    },
                                    transition="all 0.3s ease"
                                ),
                                position="relative",
                                width="100%"
                            ),
                            spacing="2",
                            width="100%",
                            align="start"
                        ),
                        
                        # Checkbox y enlace de contraseña
                        rx.hstack(
                            rx.fragment(),
                            rx.spacer(),
                            rx.link(
                                "¿Olvidaste tu contraseña?",
                                href="/forgot-password",
                                color=st.Colors.accent,
                                font_size="0.875rem",
                                _hover={"color": st.Colors.LoginCard.text_primary},
                                transition="colors 0.3s ease"
                            ),
                            width="100%",
                            align="center"
                        ),
                        
                        # Botón de iniciar sesión con icono
                        rx.button(
                            rx.hstack(
                                rx.icon("log-in", size=20),
                                "Iniciar sesión",
                                spacing="2",
                                align="center"
                            ),
                            on_click=LoginState.login,
                            size="3",
                            width="100%",
                            height="48px",
                            background=st.Colors.LoginCard.button_bg,
                            color="white",
                            border="none",
                            border_radius="8px",
                            font_weight="500",
                            font_size="1.125rem",
                            font_family="sans-serif",
                            cursor="pointer",
                            _hover={
                                "background": st.Colors.LoginCard.button_hover,
                                "transform": "scale(1.05)"
                            },
                            transition="all 0.3s ease"
                        ),
                        
                        spacing="6",
                        width="100%"
                    ),
                    
                    # Separador
                    rx.hstack(
                        rx.divider(flex="1", border_color=st.Colors.border),
                        rx.text(
                            "O continúa con",
                            color=st.Colors.LoginCard.text_muted,
                            font_size="0.875rem",
                            padding="0 1rem",
                            background=st.Colors.LoginCard.login_bg
                        ),
                        rx.divider(flex="1", border_color=st.Colors.border),
                        width="100%",
                        align="center",
                        margin="2rem 0"
                    ),
                    
                    # Link de registro
                    rx.center(
                        rx.text(
                            [
                                "¿No tienes cuenta? ",
                                rx.link(
                                    "Regístrate aquí",
                                    href="/register",
                                    color=st.Colors.accent,
                                    font_weight="500",
                                    _hover={"color": st.Colors.LoginCard.text_primary},
                                    transition="colors 0.3s ease"
                                )
                            ],
                            color=st.Colors.LoginCard.text_secondary
                        )
                    ),
                    
                    width="100%",
                    max_width="400px",
                    padding="2rem",
                    background=st.Colors.LoginCard.glass_card,
                    border=f"2px solid {st.Colors.border}",
                    border_radius="24px",
                    box_shadow=st.Colors.LoginCard.shadow_large,
                    backdrop_filter="blur(10px)",
                    _hover={
                        "border_color": st.Colors.accent
                    },
                    transition="all 0.5s ease",
                    spacing="8"
                ),

                TermnsConditions(),
                
                spacing="6",
                align="center",
                width="100%"
            )
        ),
        
        # Props del container principal
        background=st.Colors.background,
        min_height="100vh",
        position="relative",
        overflow="hidden",
        display="flex",
        align_items="center",
        justify_content="center",
        padding="1rem"
    )

@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return LoginCard()