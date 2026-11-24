import sqlite3
import os


def create_table(db_path): # This function creates a table named "heroes" in the SQLite database specified by db_path. The table has four columns: id (an integer primary key), name (text), role (text), and level (integer). If the table already exists, it will not be created again.
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS heroes (
                id INTEGER PRIMARY KEY,
                name TEXT,
                role TEXT,
                level INTEGER
            )
            """
        )
        conn.commit()

def add_hero(db_path, name, role, level): # This function adds a new hero to the "heroes" table in the SQLite database specified by db_path. It takes the hero's name, role, and level as parameters and inserts them into the table. The id column is automatically generated as it is defined as an integer primary key.
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO heroes (name, role, level) VALUES (?, ?, ?)",
            (name, role, level),
        )
        conn.commit()

def heroes_by_level(db_path): # This function retrieves all heroes from the "heroes" table in the SQLite database specified by db_path, sorted by their level in descending order. If two heroes have the same level, they are sorted by name in ascending order. The function returns a list of tuples, where each tuple contains the hero's name, role, and level.
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name, role, level FROM heroes ORDER BY level DESC, name ASC"
        )
        return cursor.fetchall()

def heroes_in_role(db_path, role): # This function retrieves all heroes from the "heroes" table in the SQLite database specified by db_path that have the specified role. The heroes are sorted by name in ascending order. The function returns a list of tuples, where each tuple contains the hero's name and level.
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name, level FROM heroes WHERE role = ? ORDER BY name ASC", (role,)
        )
        return cursor.fetchall()

def average_level(db_path): # This function calculates the average level of all heroes in the "heroes" table in the SQLite database specified by db_path. It executes a SQL query to compute the average of the level column. If there are no heroes in the table, it returns 0. The function returns the average level as a float.
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(level) FROM heroes")
        result = cursor.fetchone()[0]
        return result if result is not None else 0

def count_by_role(db_path): # This function counts the number of heroes in each role in the "heroes" table in the SQLite database specified by db_path. It executes a SQL query that groups the heroes by their role and counts the number of heroes in each group. The function returns a dictionary where the keys are the roles and the values are the corresponding counts.
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT role, COUNT(*) FROM heroes GROUP BY role")
        return dict(cursor.fetchall())

def level_up(db_path, name): # This function increases the level of a specific hero in the "heroes" table in the SQLite database specified by db_path. It takes the hero's name as a parameter and executes a SQL query to increment the level of that hero by 1. The function commits the changes to the database.
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE heroes SET level = level + 1 WHERE name = ?", (name,))
        conn.commit()

def retire(db_path, name): # This function removes a specific hero from the "heroes" table in the SQLite database specified by db_path. It takes the hero's name as a parameter and executes a SQL query to delete the hero with that name from the table. The function commits the changes to the database.
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM heroes WHERE name = ?", (name,))
        conn.commit()

# The demonstration in main()
# main(db_path="guild.db") creates the table, adds Brenna (Warrior, 3), Corwin (Mage, 5), Dax (Rogue, 2) and Elsbeth (Mage, 4), then prints each result as in the sample run.
# Level up Dax, retire Brenna, and print the roster again.
# End the file with the main guard. Delete guild.db before running again, because main() adds the four heroes every time it runs

def main(db_path="guild.db"): # This function serves as the main entry point for the script. It creates the "heroes" table in the SQLite database specified by db_path and adds four heroes to it with predefined names, roles, and levels. The default database path is "guild.db".
    create_table(db_path)
    add_hero(db_path, "Corwin", "Mage", 5)
    add_hero(db_path, "Dax", "Rogue", 2)
    add_hero(db_path, "Elsbeth", "Mage", 4)
    print("By Level:")
    for hero in heroes_by_level(db_path):
        print(f"{hero[0]} the {hero[1]}, Level {hero[2]}")
    print("Mages:")
    for hero in heroes_in_role(db_path, "Mage"):
        print(hero)
    print("Average Level:", average_level(db_path))
    print("Count by Role:", count_by_role(db_path))
    level_up(db_path, "Dax")
    retire(db_path, "Brenna")
    print("After a level-up and a retirement:")
    for hero in heroes_by_level(db_path):
        print(f"{hero[0]} the {hero[1]}, Level {hero[2]}")

if __name__ == "__main__":
    if os.path.exists("guild.db"):
        os.remove("guild.db")
    main()