import sqlite3


def trigger_insertion(data_f):

    conn = sqlite3.connect('sql.db')

    conn.execute("""
        CREATE TABLE IF NOT EXISTS POKEMON(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Tier TEXT,
            HP int not null,
            Attack int not null,
            Defense int not null,
            Special_Attack int not null,
            Special_Defense int not null,
            Speed int not null,
            Type1 TEXT NOT NULL,
            Type2 TEXT,
            Abilities1 TEXT NOT NULL,
            Abilities2 TEXT,
            Abilities3 TEXT,
            Abilities4 TEXT
        )
    """)
        
    print("Table created successfully")
    conn.commit()


    for i, data in data_f.iterrows():
        conn.execute("""
            INSERT INTO POKEMON (
                Name,
                Tier,
                HP,
                Attack,
                Defense,
                Special_Attack,
                Special_Defense,
                Speed,
                Type1,
                Type2,
                Abilities1,
                Abilities2,
                Abilities3,
                Abilities4
            ) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (
            data["Name"],
            data['Tier'],
            data["HP"],
            data['Attack'],
            data['Defense'],
            data['Special Attack'],
            data['Special Defense'],
            data['Speed'],
            data['Type1'],
            data['Type2'],
            data['Abilities1'],
            data["Abilities2"],
            data['Abilities3'],
            data['Abilities4'])
        )
        conn.commit()

    print("Data inserted")
    conn.close()





