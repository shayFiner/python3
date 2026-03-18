#!/usr/bin/env python
"""Initialize demo users in the database"""

from app.database import SessionLocal, create_tables
from app.models.user import User
from app.utils.security import hash_password

# Create all tables
create_tables()

# Get database session
db = SessionLocal()

try:
    # Check if admin exists
    admin = db.query(User).filter(User.username == "admin").first()
    if not admin:
        admin = User(
            username="admin",
            email="admin@system.com",
            full_name="מנהל המערכת",
            hashed_password=hash_password("admin123"),
            is_admin=True,
            is_active=True
        )
        db.add(admin)
        print("✅ Created admin user (username: admin, password: admin123)")

    # Check if regular user exists
    user = db.query(User).filter(User.username == "user").first()
    if not user:
        user = User(
            username="user",
            email="user@system.com",
            full_name="שי בר",
            hashed_password=hash_password("1234"),
            is_admin=False,
            is_active=True
        )
        db.add(user)
        print("✅ Created regular user (username: user, password: 1234)")

    db.commit()
    print("✅ Demo users initialized successfully!")

except Exception as e:
    db.rollback()
    print(f"❌ Error: {e}")
finally:
    db.close()
