import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'oottam-secret-key-2024'
    # Supabase: 'postgresql://postgres:Loveangai%40123@db.ipjdnpdzqhrgioiaimik.supabase.co:5432/postgres'
    # Using SQLite for local development
    SQLALCHEMY_DATABASE_URI = 'sqlite:///oottam.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CART_SESSION_KEY = 'cart'