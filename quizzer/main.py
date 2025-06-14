from routes import create_app

app=create_app()


if __name__=='__main__':
    with app.app_context():
        from model.config import db
        db.create_all()
        
    app.run(debug=True)