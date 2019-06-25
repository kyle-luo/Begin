






def init_db():
    db.create_all()

    new_user = User(username='testuser', password='testpassword', email='testemail@test.com')
    db.session.add(new_user)
    db.session.commit()

if __name__ == '__main__':
    init_db()