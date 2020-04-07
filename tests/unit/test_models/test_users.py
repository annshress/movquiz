def test_create_user(new_user):
    """
    user creation will not fill password
    user is inactive
    """
    assert new_user.password is None, 'Password should have been None.'
    assert new_user.is_active is False, 'User should have been inactive.'
