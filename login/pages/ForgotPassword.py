import reflex as rx
from login.styles import styles as st
from login.components.components import ReturnButton, TermnsConditions
from login.state.ForgotPasswordState import ForgotPasswordState

def EmailStep() -> rx.Component:
    """Step 1: Enter email"""
    return rx.vstack(
        # Header
        rx.center(
            rx.vstack(
                rx.box(
                    rx.icon(
                        "mail",
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
                    "¿Olvidaste tu contraseña?",
                    size="8",
                    color=st.Colors.LoginCard.text_primary,
                    font_weight="500",
                    text_align="center",
                    margin_bottom="0.5rem",
                    font_family="sans-serif"
                ),
                rx.text(
                    "Ingresa tu email y te enviaremos un código para recuperar tu cuenta",
                    color=st.Colors.LoginCard.text_secondary,
                    text_align="center",
                    margin='0 0 1.5rem 0',
                    max_width="350px"
                ),
                spacing="2",
                align="center"
            )
        ),
        
        # Form
        rx.vstack(
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
                        value=ForgotPasswordState.email,
                        on_change=ForgotPasswordState.set_email,
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
            
            rx.button(
                rx.hstack(
                    rx.icon("send", size=20),
                    "Enviar código",
                    spacing="2",
                    align="center"
                ),
                on_click=ForgotPasswordState.send_reset_code,
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
        
        spacing="8",
        width="100%"
    )

def CodeStep() -> rx.Component:
    """Step 2: Enter verification code"""
    return rx.vstack(
        # Header
        rx.center(
            rx.vstack(
                rx.box(
                    rx.icon(
                        "shield-check",
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
                    "Verificar código",
                    size="8",
                    color=st.Colors.LoginCard.text_primary,
                    font_weight="500",
                    text_align="center",
                    margin_bottom="0.5rem",
                    font_family="sans-serif"
                ),
                rx.text(
                    f"Hemos enviado un código de 6 dígitos a {ForgotPasswordState.email}",
                    color=st.Colors.LoginCard.text_secondary,
                    text_align="center",
                    margin='0 0 1.5rem 0',
                    max_width="350px"
                ),
                spacing="2",
                align="center"
            )
        ),
        
        # Form
        rx.vstack(
            rx.vstack(
                rx.text(
                    "Código de verificación",
                    font_weight="500",
                    color=st.Colors.LoginCard.text_primary
                ),
                rx.box(
                    rx.icon("key", size=20, color=st.Colors.LoginCard.text_muted, position="absolute", left="12px", top="50%", transform="translateY(-50%)"),
                    rx.input(
                        placeholder="123456",
                        value=ForgotPasswordState.reset_code,
                        on_change=ForgotPasswordState.set_reset_code,
                        size="3",
                        width="100%",
                        height="48px",
                        padding_left="40px",
                        background=st.Colors.LoginCard.input_bg,
                        border=f"1px solid {st.Colors.LoginCard.input_border}",
                        border_radius="8px",
                        backdrop_filter="blur(10px)",
                        color=st.Colors.LoginCard.text_primary,
                        text_align="center",
                        font_size="1.25rem",
                        letter_spacing="0.5rem",
                        max_length=6,
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
            
            rx.hstack(
                rx.button(
                    "Atrás",
                    on_click=ForgotPasswordState.go_back,
                    size="3",
                    width="48%",
                    height="48px",
                    background="transparent",
                    color=st.Colors.LoginCard.text_secondary,
                    border=f"1px solid {st.Colors.border}",
                    border_radius="8px",
                    font_weight="500",
                    cursor="pointer",
                    _hover={
                        "background": st.Colors.LoginCard.login_bg,
                        "border_color": st.Colors.accent
                    },
                    transition="all 0.3s ease"
                ),
                
                rx.button(
                    "Verificar",
                    on_click=ForgotPasswordState.verify_reset_code,
                    size="3",
                    width="48%",
                    height="48px",
                    background=st.Colors.LoginCard.button_bg,
                    color="white",
                    border="none",
                    border_radius="8px",
                    font_weight="500",
                    cursor="pointer",
                    _hover={
                        "background": st.Colors.LoginCard.button_hover,
                        "transform": "scale(1.05)"
                    },
                    transition="all 0.3s ease"
                ),
                
                width="100%",
                justify="between"
            ),
            
            spacing="6",
            width="100%"
        ),
        
        spacing="8",
        width="100%"
    )

def NewPasswordStep() -> rx.Component:
    """Step 3: Set new password"""
    return rx.vstack(
        # Header
        rx.center(
            rx.vstack(
                rx.box(
                    rx.icon(
                        "lock",
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
                    "Nueva contraseña",
                    size="8",
                    color=st.Colors.LoginCard.text_primary,
                    font_weight="500",
                    text_align="center",
                    margin_bottom="0.5rem",
                    font_family="sans-serif"
                ),
                rx.text(
                    "Ingresa tu nueva contraseña",
                    color=st.Colors.LoginCard.text_secondary,
                    text_align="center",
                    margin='0 0 1.5rem 0'
                ),
                spacing="2",
                align="center"
            )
        ),
        
        # Form
        rx.vstack(
            rx.vstack(
                rx.text(
                    "Nueva contraseña",
                    font_weight="500",
                    color=st.Colors.LoginCard.text_primary
                ),
                rx.box(
                    rx.icon("lock", size=20, color=st.Colors.LoginCard.text_muted, position="absolute", left="12px", top="50%", transform="translateY(-50%)"),
                    rx.input(
                        placeholder="••••••••",
                        type="password",
                        value=ForgotPasswordState.new_password,
                        on_change=ForgotPasswordState.set_new_password,
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
                        value=ForgotPasswordState.confirm_password,
                        on_change=ForgotPasswordState.set_confirm_password,
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
            
            rx.hstack(
                rx.button(
                    "Atrás",
                    on_click=ForgotPasswordState.go_back,
                    size="3",
                    width="48%",
                    height="48px",
                    background="transparent",
                    color=st.Colors.LoginCard.text_secondary,
                    border=f"1px solid {st.Colors.border}",
                    border_radius="8px",
                    font_weight="500",
                    cursor="pointer",
                    _hover={
                        "background": st.Colors.LoginCard.login_bg,
                        "border_color": st.Colors.accent
                    },
                    transition="all 0.3s ease"
                ),
                
                rx.button(
                    rx.hstack(
                        rx.icon("check", size=20),
                        "Actualizar",
                        spacing="2",
                        align="center"
                    ),
                    on_click=ForgotPasswordState.reset_password,
                    size="3",
                    width="48%",
                    height="48px",
                    background=st.Colors.LoginCard.button_bg,
                    color="white",
                    border="none",
                    border_radius="8px",
                    font_weight="500",
                    cursor="pointer",
                    _hover={
                        "background": st.Colors.LoginCard.button_hover,
                        "transform": "scale(1.05)"
                    },
                    transition="all 0.3s ease"
                ),
                
                width="100%",
                justify="between"
            ),
            
            spacing="6",
            width="100%"
        ),
        
        spacing="8",
        width="100%"
    )

def ForgotPasswordCard() -> rx.Component:
    """Formulario de recuperación de contraseña elegante"""
    return rx.box(
        ReturnButton(),
        
        # Formulario principal
        rx.center(
            rx.vstack(
                # Card principal con efecto glass
                rx.box(
                    # Contenido dinámico según el paso
                    rx.cond(
                        ForgotPasswordState.step == 1,
                        EmailStep(),
                        rx.cond(
                            ForgotPasswordState.step == 2,
                            CodeStep(),
                            NewPasswordStep()
                        )
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
                    
                    # Link de regreso al login
                    rx.center(
                        rx.text(
                            [
                                "¿Recordaste tu contraseña? ",
                                rx.link(
                                    "Inicia sesión",
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

@rx.page(route="/forgot-password", title="Recuperar Contraseña")
def forgot_password() -> rx.Component:
    return ForgotPasswordCard()
