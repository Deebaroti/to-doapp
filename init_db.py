from app import app, db

# This script initializes the database with tables
with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")
