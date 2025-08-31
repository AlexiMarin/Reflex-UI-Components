import reflex as rx
from login.database_model_DELETE_THIS_DIR import model # --- > Import Here Your ORM Model
from login.database_model_DELETE_THIS_DIR.model import get_Session # --- > Import Here Your DB conecction
import bcrypt
import random
import string
from datetime import datetime, timedelta

_reset_codes = {}

def GenerateResetCode() -> str:
    """Generate a 6-digit random code for password reset."""
    return ''.join(random.choices(string.digits, k=6))

def PasswordHashed(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def PasswordVerify(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def CreateDatabase():
    model.Base.metadata.create_all(bind=model.get_engine())

def CreateUser(email: str, password: str): # --- > Improve your own model Logic
    try:
        with get_Session() as conn:
            user = model.User(email=email, password=PasswordHashed(password))
            conn.add(user)
            conn.commit()
    except Exception as e:
        raise ValueError("User with this email already exists") from e

def GetUserByEmail(email: str):
    with get_Session() as conn:
        user = conn.query(model.User).filter(model.User.email == email).first()
    if user:
        return user
    raise ValueError("User not found")

def UserAuth(password: str, email: str) -> bool:
    with get_Session() as conn:
        user = conn.query(model.User).filter(model.User.email == email).first()
        if not user:
            raise ValueError("User not found")
    return PasswordVerify(password, user.password)

def SendResetCode(email: str) -> bool:
    """
    Demo function to simulate sending a reset code to email.
    In production, this would send an actual email.
    """
    try:
        # Verify user exists
        GetUserByEmail(email)
        
        # Generate and store reset code
        code = GenerateResetCode()
        expires_at = datetime.now() + timedelta(minutes=15)  # Code expires in 15 minutes
        
        _reset_codes[email] = {
            "code": code,
            "expires": expires_at,
            "used": False
        }
        
        # In production, send email here
        return True
        
    except ValueError:
        # User not found
        return False

def VerifyResetCode(email: str, code: str) -> bool:
    """
    Demo function to verify the reset code.
    """
    if email not in _reset_codes:
        return False
    
    stored_data = _reset_codes[email]
    
    # Check if code matches
    if stored_data["code"] != code:
        return False
    
    # Check if code has expired
    if datetime.now() > stored_data["expires"]:
        return False
    
    # Check if code has already been used
    if stored_data["used"]:
        return False
    
    return True

def UpdateUserPassword(email: str, new_password: str, reset_code: str) -> bool:
    """
    Demo function to update user password after verifying reset code.
    """
    try:
        # Verify the reset code first
        if not VerifyResetCode(email, reset_code):
            return False
        
        # Update password in database
        with get_Session() as conn:
            user = conn.query(model.User).filter(model.User.email == email).first()
            if not user:
                return False
            
            user.password = PasswordHashed(new_password)
            conn.commit()
        
        # Mark reset code as used
        _reset_codes[email]["used"] = True
        return True
        
    except Exception as e:
        return False

def CleanupExpiredCodes():
    """
    Demo function to clean up expired reset codes.
    In production, this could be run as a scheduled task.
    """
    current_time = datetime.now()
    expired_emails = [
        email for email, data in _reset_codes.items()
        if current_time > data["expires"]
    ]
    
    for email in expired_emails:
        del _reset_codes[email]

def GetUserProfile(email: str) -> dict:
    """
    Demo function to get user profile information.
    """
    try:
        user = GetUserByEmail(email)
        return {
            "id": user.id,
            "email": user.email,
            "is_active": user.is_active,
            "created_at": "Demo Date"  # In production, add created_at field to model
        }
    except ValueError:
        return None

def DeactivateUser(email: str) -> bool:
    """
    Demo function to deactivate a user account.
    """
    try:
        with get_Session() as conn:
            user = conn.query(model.User).filter(model.User.email == email).first()
            if not user:
                return False
            
            user.is_active = False
            conn.commit()
            return True
    except Exception:
        return False

def ReactivateUser(email: str) -> bool:
    """
    Demo function to reactivate a user account.
    """
    try:
        with get_Session() as conn:
            user = conn.query(model.User).filter(model.User.email == email).first()
            if not user:
                return False
            
            user.is_active = True
            conn.commit()
            return True
    except Exception:
        return False

def GetAllUsers() -> list:
    """
    Demo function to get all users (admin function).
    """
    try:
        with get_Session() as conn:
            users = conn.query(model.User).all()
            return [
                {
                    "id": user.id,
                    "email": user.email,
                    "is_active": user.is_active
                }
                for user in users
            ]
    except Exception:
        return []

def ValidateEmailFormat(email: str) -> bool:
    """
    Demo function to validate email format.
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def ValidatePasswordStrength(password: str) -> dict:
    """
    Demo function to validate password strength.
    Returns dict with validation results.
    """
    result = {
        "valid": True,
        "errors": [],
        "score": 0
    }
    
    if len(password) < 6:
        result["valid"] = False
        result["errors"].append("Password must be at least 6 characters long")
    else:
        result["score"] += 1
    
    if not any(c.isupper() for c in password):
        result["errors"].append("Password should contain at least one uppercase letter")
    else:
        result["score"] += 1
    
    if not any(c.islower() for c in password):
        result["errors"].append("Password should contain at least one lowercase letter")
    else:
        result["score"] += 1
    
    if not any(c.isdigit() for c in password):
        result["errors"].append("Password should contain at least one number")
    else:
        result["score"] += 1
    
    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        result["errors"].append("Password should contain at least one special character")
    else:
        result["score"] += 1
    
    return result
