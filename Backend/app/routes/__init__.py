from app.routes.auth_routes import auth_bp
from app.routes.rag_routes import rag_bp
from app.routes.password_routes import password_bp

__all__ = [
    'auth_bp',
    'rag_bp',
    'password_bp'
]
