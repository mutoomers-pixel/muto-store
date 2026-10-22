from flask import Flask, render_template_string
app = Flask(__name__)

games = [
    {"name": "Grand Theft Auto V", "id": "BLUS31156", "cover": "https://upload.wikimedia.org/wikipedia/en/a/a5/Grand_Theft_Auto_V.png"},
    {"name": "Gran Turismo 6", "id": "BCUS98114", "cover": "https://m.media-amazon.com/images/I/71YyPj6oX5L._AC_SL1000_.jpg"},
    {"name": "FIFA 17", "id": "BLES02235", "cover": "https://m.media-amazon.com/images/I/81xU9d4NfNL._AC_SL1500_.jpg"},
    {"name": "The Last of Us", "id": "BCUS98174", "cover": "https://upload.wikimedia.org/wikipedia/en/4/46/Video_Game_Cover_-_The_Last_of_Us.jpg"},
    {"name": "God of War III", "id": "BCUS98111", "cover": "https://upload.wikimedia.org/wikipedia/en/6/63/God_of_War_3_art.jpg"},
    {"name": "Red Dead Redemption", "id": "BLUS30482", "cover": "https://upload.wikimedia.org/wikipedia/en/a/a7/Red_Dead_Redemption.jpg"},
    {"name": "Uncharted 2: Among Thieves", "id": "BCUS98123", "cover": "https://upload.wikimedia.org/wikipedia/en/a/a3/Uncharted_2_Among_Thieves_Box_Art.jpg"},
    {"name": "Uncharted 3: Drake's Deception", "id": "BCUS98168", "cover": "https://upload.wikimedia.org/wikipedia/en/8/87/Uncharted_3_Box_Art.jpg"},
    {"name": "Grand Theft Auto IV", "id": "BLUS30127", "cover": "https://upload.wikimedia.org/wikipedia/en/b/b7/Grand_Theft_Auto_IV_cover.jpg"},
    {"name": "Call of Duty: Black Ops II", "id": "BLUS31011", "cover": "https://upload.wikimedia.org/wikipedia/en/0/05/Call_of_Duty_Black_Ops_II_cover.png"},
    {"name": "Metal Gear Solid 4: Guns of the Patriots", "id": "BLUS30109", "cover": "https://upload.wikimedia.org/wikipedia/en/e/e0/MGS4_North_American_cover_art.jpg"},
    {"name": "Batman: Arkham City", "id": "BLUS30538", "cover": "https://upload.wikimedia.org/wikipedia/en/0/00/Batman_Arkham_City_Game_Cover.jpg"},
    {"name": "Skyrim", "id": "BLUS30778", "cover": "https://upload.wikimedia.org/wikipedia/en/1/15/The_Elder_Scrolls_V_Skyrim_cover.png"},
    {"name": "Minecraft: PlayStation 3 Edition", "id": "BLUS31419", "cover": "https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png"},
    {"name": "Need for Speed: Most Wanted (2012)", "id": "BLUS31010", "cover": "https://upload.wikimedia.org/wikipedia/en/8/8e/Need_for_Speed_Most_Wanted_2012_box_art.jpg"},
    {"name": "PES 2017", "id": "BLES02237", "cover": "https://m.media-amazon.com/images/I/81P2h0i-nGL._AC_SL1500_.jpg"},
    {"name": "Mortal Kombat Komplete Edition", "id": "BLUS30895", "cover": "https://upload.wikimedia.org/wikipedia/en/1/1f/Mortal_Kombat_box_art.png"},
    {"name": "Tekken 6", "id": "BLUS30359", "cover": "https://upload.wikimedia.org/wikipedia/en/5/5a/Tekken_6_Coverart.jpg"},
    {"name": "Assassin's Creed IV: Black Flag", "id": "BLUS31128", "cover": "https://upload.wikimedia.org/wikipedia/en/2/22/Assassin%27s_Creed_IV_Black_Flag_cover.jpg"},
    {"name": "Far Cry 3", "id": "BLUS30922", "cover": "https://upload.wikimedia.org/wikipedia/en/1/10/Far_Cry_3_box_art.jpg"},
    {"name": "Bioshock Infinite", "id": "BLUS30639", "cover": "https://upload.wikimedia.org/wikipedia/en/a/a3/BioShock_Infinite_Cover.png"},
    {"name": "Dark Souls II", "id": "BLUS31126", "cover": "https://upload.wikimedia.org/wikipedia/en/e/ed/Dark_Souls_II_cover.jpg"},
    {"name": "Mass Effect 2", "id": "BLUS30628", "cover": "https://upload.wikimedia.org/wikipedia/en/0/05/MassEffect2boxart.jpg"},
    {"name": "Borderlands 2", "id": "BLUS30982", "cover": "https://upload.wikimedia.org/wikipedia/en/5/51/Borderlands2boxart.jpg"},
    {"name": "Demon's Souls", "id": "BCUS98170", "cover": "https://upload.wikimedia.org/wikipedia/en/c/c2/Demon%27s_Souls_Cover_Art.jpg"},
    {"name": "Infamous 2", "id": "BCUS98125", "cover": "https://upload.wikimedia.org/wikipedia/en/e/e0/Infamous_2_box_art.jpg"},
    {"name": "Killzone 3", "id": "BCUS98235", "cover": "https://upload.wikimedia.org/wikipedia/en/1/1a/Killzone_3_box_art.jpg"},
    {"name": "Resistance 3", "id": "BCUS98229", "cover": "https://upload.wikimedia.org/wikipedia/en/c/c0/Resistance_3_box_art.jpg"},
    {"name": "LittleBigPlanet 2", "id": "BCUS98208", "cover": "https://upload.wikimedia.org/wikipedia/en/d/df/LittleBigPlanet_2_Box_Art.jpg"},
    {"name": "Heavy Rain", "id": "BCUS98164", "cover": "https://upload.wikimedia.org/wikipedia/en/7/73/Heavy_Rain_Cover.jpg"},
    {"name": "Beyond: Two Souls", "id": "BCUS98298", "cover": "https://upload.wikimedia.org/wikipedia/en/e/e3/Beyond_Two_Souls_box_art.jpg"},
    {"name": "MotorStorm Apocalypse", "id": "BCUS98204", "cover": "https://upload.wikimedia.org/wikipedia/en/8/87/MotorStorm_Apocalypse_Cover.jpg"},
    {"name": "Gran Turismo 5", "id": "BCUS98158", "cover": "https://upload.wikimedia.org/wikipedia/en/6/6b/Gran_Turismo_5_cover_art.jpg"},
    {"name": "Blur", "id": "BLUS30366", "cover": "https://upload.wikimedia.org/wikipedia/en/5/53/Blurbox.jpg"},
    {"name": "Need for Speed: Hot Pursuit", "id": "BLUS30566", "cover": "https://upload.wikimedia.org/wikipedia/en/9/94/NFS_Hot_Pursuit_2010_cover.jpg"},
    {"name": "Dirt 3", "id": "BLUS30689", "cover": "https://upload.wikimedia.org/wikipedia/en/2/23/Dirt_3_cover_art.jpg"},
    {"name": "Dead Space 2", "id": "BLUS30624", "cover": "https://upload.wikimedia.org/wikipedia/en/e/e5/DeadSpace2box.jpg"},
    {"name": "Resident Evil 5", "id": "BLUS30258", "cover": "https://upload.wikimedia.org/wikipedia/en/d/d4/RE5_box.jpg"},
    {"name": "Devil May Cry 4", "id": "BLUS30089", "cover": "https://upload.wikimedia.org/wikipedia/en/e/e7/Devil_May_Cry_4_cover.jpg"},
    {"name": "Bayonetta", "id": "BLUS30367", "cover": "https://upload.wikimedia.org/wikipedia/en/d/d6/Bayonetta_box_art.png"},
    {"name": "Castlevania: Lords of Shadow", "id": "BLUS30410", "cover": "https://upload.wikimedia.org/wikipedia/en/b/b3/Lords_of_shadow_box.jpg"},
    {"name": "Dragon Ball Xenoverse", "id": "BLUS31498", "cover": "https://upload.wikimedia.org/wikipedia/en/b/b2/Dragon_Ball_Xenoverse_cover_art.jpg"},
    {"name": "Naruto Shippuden: Ultimate Ninja Storm 3", "id": "BLUS31066", "cover": "https://upload.wikimedia.org/wikipedia/en/1/1b/Naruto_Shippuden_Ultimate_Ninja_Storm_3_cover.jpg"},
    {"name": "WWE 2K17", "id": "BLUS31589", "cover": "https://upload.wikimedia.org/wikipedia/en/d/dc/WWE_2K17_cover.jpg"},
    {"name": "NBA 2K18", "id": "BLUS31611", "cover": "https://upload.wikimedia.org/wikipedia/en/2/20/NBA_2K18_cover_art.jpg"},
    {"name": "Call of Duty: Modern Warfare 3", "id": "BLUS30838", "cover": "https://upload.wikimedia.org/wikipedia/en/d/d5/Call_of_Duty_Modern_Warfare_3_cover.png"},
    {"name": "Battlefield 3", "id": "BLUS30762", "cover": "https://upload.wikimedia.org/wikipedia/en/6/69/Battlefield_3_box_art.jpg"},
    {"name": "Crysis 3", "id": "BLUS30976", "cover": "https://upload.wikimedia.org/wikipedia/en/9/91/Crysis_3_Box_Art.jpg"},
    {"name": "Max Payne 3", "id": "BLUS30557", "cover": "https://upload.wikimedia.org/wikipedia/en/2/21/Max_Payne_3_Cover.jpg"},
    {"name": "Mafia II", "id": "BLUS30364", "cover": "https://upload.wikimedia.org/wikipedia/en/c/cb/MafiaII.jpg"}
]

html_template = """
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="theme-color" content="#121212">
    <title>MUTO STORE</title>
    <link rel="manifest" href="data:application/manifest+json,{
      "name": "MUTO STORE",
      "short_name": "MUTO STORE",
      "start_url": "/",
      "display": "standalone",
      "background_color": "#121212",
      "theme_color": "#121212"
    }">
    <style>
        body { background-color: #121212; color: #fff; font-family: sans-serif; margin: 0; padding: 15px; user-select: none; }
        h1 { color: #0070d1; text-align: center; margin-top: 10px; margin-bottom: 2px; font-size: 24px; }
        .subtitle { color: #888; text-align: center; font-size: 12px; margin-bottom: 20px; }
        .list-container { display: flex; flex-direction: column; gap: 12px; max-width: 500px; margin: 0 auto; }
        .game-item { display: flex; align-items: center; background: #1e1e1e; border-radius: 10px; padding: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); border: 1px solid #2a2a2a; }
        .game-item img { width: 70px; height: 95px; object-fit: cover; border-radius: 6px; flex-shrink: 0; }
        .game-info { margin-left: 15px; text-align: left; flex-grow: 1; }
        .game-title { font-size: 15px; font-weight: bold; color: #ffffff; margin-bottom: 6px; line-height: 1.2; }
        .game-id { font-size: 12px; color: #0070d1; font-weight: bold; background: #121212; display: inline-block; padding: 3px 8px; border-radius: 4px; border: 1px solid #0070d1; }
    </style>
</head>
<body>
    <h1>MUTO STORE</h1>
    <div class="subtitle">PS3 Oyun Arşivi (50 Oyun)</div>
    <div class="list-container">
        {% for game in games %}
        <div class="game-item">
            <img src="{{ game.cover }}" alt="{{ game.name }}" onerror="this.src='https://via.placeholder.com/70x95/111/fff?text=No+Cover'">
            <div class="game-info">
                <div class="game-title">{{ game.name }}</div>
                <div class="game-id">{{ game.id }}</div>
            </div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template, games=games)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
