import reflex as rx
from login.backend import functions as f

class LoginState(rx.State):
    """State to managemet login attemps."""

    email: str
    password: str
    remember_me: bool = False

    def on_load(self):
        """Load saved credentials if remember_me was checked."""
        # En Reflex necesitamos usar rx.Cookie directamente
        pass

    @rx.event
    def login(self):
        # Validate required fields
        if not self.email or not self.password:
            return rx.toast.error("Por favor completa todos los campos")
        
        # Validate email format
        if not f.ValidateEmailFormat(self.email):
            return rx.toast.error("Formato de email inválido")
        
        try:
            user = f.GetUserByEmail(self.email)
            
            # Check if user is active
            if not user.is_active:
                return rx.toast.error("Cuenta desactivada. Contacta al administrador")
            
            if f.UserAuth(self.password, self.email):
                # Clear form
                self.email = ""
                self.password = ""
                return [
                    rx.toast.success("Login exitoso"),
                    rx.redirect("/dashboard")
                ]
            else:
                return rx.toast.error("Credenciales incorrectas")
        except ValueError:
            return rx.toast.error("Usuario no encontrado")