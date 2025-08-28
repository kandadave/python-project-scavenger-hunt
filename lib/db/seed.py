from lib.crud import create_user, create_quest

def seed_data():
    user_id = create_user("Test User", "test@example.com", "Adventure")
    create_quest("Sample Quest", user_id, "New York", "Adventure", "Find the hidden artifact")
    print("Data seeded")

if __name__ == "__main__":
    seed_data()