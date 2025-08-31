import reflex as rx

class Colors:
    """Colores y estilos globales para la app."""
    background = "#deefff"
    card = "#ffffff"
    accent = "#3b82f6"
    border = "#cfd8dc"

    class LoginCard:
        text_primary = "#263238"
        text_secondary = "#607d8b"
        text_muted = "#90a4ae"

        login_bg = "rgba(248,250,252,0.85)"
        glass_card = "rgba(255,255,255,0.92)"
        glass_strong = "rgba(255,255,255,0.98)"

        input_bg = "#ffffff"
        input_border = "#cfd8dc"

        button_bg = "#3b82f6"
        button_hover = "#2563eb"

        shadow_medium = "0 4px 24px rgba(44,62,80,0.07)"
        shadow_large = "0 8px 32px rgba(44,62,80,0.12)"

        glass_border = "rgba(44,62,80,0.12)"

hover_button = {
    "_hover": {
        "transition": "0.3s",
        "transform": "scale(1.1)",
    }
}

logo = {
    "align": "left",
    "width": "100",
    "height": "100px",
}

menu_hover = {
    "_hover": {
        "transition": "0.3s",
        "transform": "translateX(20px) scale(1.1)",
        "cursor": "pointer",
    },
    "width": "100%",
    "margin": "1em 0 0 0",
}

hover = {
    "_hover": {
        "transition": "0.3s",
        "transform": "scale(1.1)",
        "cursor": "pointer",
    },
}