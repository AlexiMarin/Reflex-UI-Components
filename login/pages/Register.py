import reflex as rx
from assets import styles as st
from login.state.RegisterState import RegisterState

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
            href="/login",
            position="absolute",
            top="32px",
            left="32px",
            z_index="20"
        )

def TermsConditions() -> rx.Component:
    return rx.center(
        rx.text(
            [
                "Al registrarte, aceptas nuestros ",
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

def RegisterCard() -> rx.Component:
    """Formulario de registro elegante"""
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
                            # Icono central
                            rx.box(
                                rx.icon(
                                    "user-plus",
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
                                "Crear nueva cuenta",
                                size="8",
                                color=st.Colors.LoginCard.text_primary,
                                font_weight="500",
                                text_align="center",
                                margin_bottom="0.5rem",
                                font_family="sans-serif"
                            ),
                            rx.text(
                                "Regístrate para comenzar",
                                color=st.Colors.LoginCard.text_secondary,
                                text_align="center"
                            ),
                            spacing="2",
                            align="center"
                        )
                    ),
                    
                    # Formulario
                    rx.vstack(
                        # Campo de nombre
                        rx.vstack(
                            rx.text(
                                "Nombre completo",
                                font_weight="500",
                                color=st.Colors.LoginCard.text_primary
                            ),
                            rx.box(
                                rx.icon("user", size=20, color=st.Colors.LoginCard.text_muted, position="absolute", left="12px", top="50%", transform="translateY(-50%)"),
                                rx.input(
                                    placeholder="Tu nombre completo",
                                    type="text",
                                    value=RegisterState.name,
                                    on_change=RegisterState.set_name,
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
                        
                        # Campo de email
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
                                    value=RegisterState.email,
                                    on_change=RegisterState.set_email,
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
                        
                        # Campo de contraseña
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
                                    value=RegisterState.password,
                                    on_change=RegisterState.set_password,
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
                        
                        # Campo de confirmar contraseña
                        rx.vstack(
                            rx.text(
                                "Confirmar contraseña",
                                font_weight="500",
                                color=st.Colors.LoginCard.text_primary
                            ),
                            rx.box(
                                rx.icon("lock", size=20, color=st.Colors.LoginCard.text_muted, position="absolute", left="12px", top="50%", transform="translateY(-50%)"),
                                rx.input(
                                    placeholder="••••••••",
                                    type="password",
                                    value=RegisterState.confirm_password,
                                    on_change=RegisterState.set_confirm_password,
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
                        
                        # Botón de registro
                        rx.button(
                            rx.hstack(
                                rx.icon("user-plus", size=20),
                                "Crear cuenta",
                                spacing="2",
                                align="center"
                            ),
                            on_click=RegisterState.register,
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
                    
                    # Link de login
                    rx.center(
                        rx.text(
                            [
                                "¿Ya tienes cuenta? ",
                                rx.link(
                                    "Inicia sesión aquí",
                                    href="/login",
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

                TermsConditions(),
                
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

@rx.page(route="/register", title="Create an account")
def register() -> rx.Component:
    return RegisterCard()