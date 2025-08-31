import reflex as rx
from login.backend import functions as f

class RegisterState(rx.State):
    """State to manage registration attempts."""

    name: str
    email: str
    password: str
    confirm_password: str
    
    @rx.event
    def register(self):
        # Validate required fields
        if not self.email or not self.password or not self.confirm_password:
            return rx.toast.error("Por favor completa todos los campos")
        
        # Validate email format
        if not f.ValidateEmailFormat(self.email):
            return rx.toast.error("Formato de email inválido")
        
        # Validate passwords match
        if self.password != self.confirm_password:
            return rx.toast.error("Las contraseñas no coinciden")
        
        # Validate password strength
        validation = f.ValidatePasswordStrength(self.password)
        if not validation["valid"]:
            return rx.toast.error(validation["errors"][0])
        
        # Validate email doesn't exist
        try:
            existing_user = f.GetUserByEmail(self.email)
            return rx.toast.error("El email ya está registrado")
        except ValueError:
            # User doesn't exist, which is what we want
            pass

        try:
            f.CreateUser(self.email, self.password)
            # Clear form
            self.name = ""
            self.email = ""
            self.password = ""
            self.confirm_password = ""
            return [
                rx.toast.success("Usuario registrado exitosamente"),
                rx.redirect("/login")
            ]
        except Exception:
            return rx.toast.error("Error al crear el usuario")
