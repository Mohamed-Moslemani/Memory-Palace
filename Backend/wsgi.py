from app import create_app
from app.routes import auth

app = create_app()
app.register_blueprint(auth, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
