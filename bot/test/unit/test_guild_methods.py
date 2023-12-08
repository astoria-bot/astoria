def test_guild_repr(session):
    """Create a Guild instance and add it to the database"""
    guild = Guild(id='1', guild_id='123', name='TestGuild')
    session.add(guild)
    session.commit()

    # Query the database to retrieve the added Guild
    queried_guild = session.query(Guild).filter_by(id='1').first()

    # Perform assertions
    assert queried_guild is not None
    assert repr(queried_guild) == "Guild(id='1', name='TestGuild', guild_id='123')"