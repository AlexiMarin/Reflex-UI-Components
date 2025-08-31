# README - Login Component Package

## Instalación y Uso

### 1. Copiar la carpeta `login/` a tu proyecto Reflex

### 2. Dependencias requeridas:
```bash
pip install bcrypt sqlalchemy
```

### 3. Configurar tu base de datos:

Edita `login/backend/functions.py` y cambia estas líneas:
```python
from connect import *  # --- > Cambia por tu conexión a BD engine
from database import model  # --- > Cambia por tu modelo ORM
```

### 4. Asegúrate de tener un modelo User con:
```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
```

### 5. Uso en tu app:
```python
import reflex as rx
from login import LoginCard, RegisterCard

app = rx.App()
```

```python
import reflex as rx
from login import 

app = rx.App()
```

### 6. Personalización:

- **Colores**: Edita `login/styles/styles.py`
- **Textos**: Edita los componentes en `login/pages/`
- **Lógica**: Edita `login/backend/functions.py`
- **Redirecciones**: Cambia `/dashboard` en `LoginSates.py`

### Características:
- Diseño moderno y responsive
- Validación de formularios
- Hash de contraseñas con bcrypt
- Toasts de éxito/error
- Componentes reutilizables
- Estilos configurables

¡Listo para usar!
