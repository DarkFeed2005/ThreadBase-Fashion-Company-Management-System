import hashlib

def hash_password(password):
    """Hash a password for storing."""
    return hashlib.sha256(password.encode()).hexdigest()

def validate_email(email):
    """Basic email validation"""
    return "@" in email and "." in email

def validate_phone(phone):
    """Basic phone number validation"""
    return phone.isdigit() and len(phone) >= 10