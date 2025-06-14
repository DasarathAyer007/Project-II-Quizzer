from model import save_user
def create_user(username,email,password):
    print("in controller")
    print(username,email,password)
    save_user(username,email,password)

