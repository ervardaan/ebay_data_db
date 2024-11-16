import pytest
import sqlite3

@pytest.fixture
def setup_database():
    """
    Setup a test SQLite database and populate it with sample data.
    """
    connection = sqlite3.connect(":memory:")  # In-memory database
    cursor = connection.cursor()
    
    # Sample table creation
    cursor.executescript("""
        CREATE TABLE user (
            userid TEXT PRIMARY KEY,
            rating INTEGER
        );
        CREATE TABLE seller (
            userid TEXT PRIMARY KEY,
            FOREIGN KEY (userid) REFERENCES user(userid)
        );
        CREATE TABLE bidder (
            userid TEXT PRIMARY KEY,
            FOREIGN KEY (userid) REFERENCES user(userid)
        );
    """)
    
    # Sample data insertion
    cursor.executescript("""
        INSERT INTO user (userid, rating) VALUES ('user1', 1100), ('user2', 500);
        INSERT INTO seller (userid) VALUES ('user1');
        INSERT INTO bidder (userid) VALUES ('user1'), ('user2');
    """)
    connection.commit()
    yield connection
    connection.close()


def test_query_users_high_rating(setup_database):
    """
    Test counting users with ratings > 1000.
    """
    connection = setup_database
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM user
        WHERE rating > 1000;
    """)
    result = cursor.fetchone()[0]
    assert result == 1


def test_query_users_seller_and_bidder(setup_database):
    """
    Test counting users who are both sellers and bidders.
    """
    connection = setup_database
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM user
        WHERE userid IN (SELECT userid FROM seller)
          AND userid IN (SELECT userid FROM bidder);
    """)
    result = cursor.fetchone()[0]
    assert result == 1
