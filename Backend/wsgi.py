from app import create_app
from app.routes.auth_routes import auth_bp

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
