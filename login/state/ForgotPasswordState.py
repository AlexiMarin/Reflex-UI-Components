import reflex as rx
from login.backend import functions as f

class ForgotPasswordState(rx.State):
    """State to manage forgot password attempts."""

    email: str
    reset_code: str
    new_password: str
    confirm_password: str
    step: int = 1  # 1: email, 2: reset code, 3: new password
    
    @rx.event
    def send_reset_code(self):
        """Send reset code to email."""
        if not self.email:
            return rx.toast.error("Por favor ingresa tu email")
        
        if not f.ValidateEmailFormat(self.email):
            return rx.toast.error("Formato de email inválido")
        
        success = f.SendResetCode(self.email)
        if success:
            self.step = 2
            return rx.toast.success("Código de recuperación enviado a tu email")
        else:
            return rx.toast.error("Email no encontrado en nuestro sistema")
    
    @rx.event
    def verify_reset_code(self):
        """Verify the reset code."""
        if not self.reset_code:
            return rx.toast.error("Por favor ingresa el código")
        
        if len(self.reset_code) != 6 or not self.reset_code.isdigit():
            return rx.toast.error("El código debe tener 6 dígitos")
        
        if f.VerifyResetCode(self.email, self.reset_code):
            self.step = 3
            return rx.toast.success("Código verificado correctamente")
        else:
            return rx.toast.error("Código inválido o expirado")
    
    @rx.event
    def reset_password(self):
        """Reset the password."""
        if not self.new_password or not self.confirm_password:
            return rx.toast.error("Por favor completa todos los campos")
        
        if self.new_password != self.confirm_password:
            return rx.toast.error("Las contraseñas no coinciden")
        
        # Validate password strength
        validation = f.ValidatePasswordStrength(self.new_password)
        if not validation["valid"]:
            return rx.toast.error(validation["errors"][0])
        
        success = f.UpdateUserPassword(self.email, self.new_password, self.reset_code)
        if success:
            # Reset form
            self.email = ""
            self.reset_code = ""
            self.new_password = ""
            self.confirm_password = ""
            self.step = 1
            return [
                rx.toast.success("Contraseña actualizada exitosamente"),
                rx.redirect("/login")
            ]
        else:
            return rx.toast.error("Error al actualizar la contraseña")
    
    @rx.event
    def go_back(self):
        """Go back to previous step."""
        if self.step > 1:
            self.step -= 1
