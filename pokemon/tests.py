from rest_framework.test import APITestCase


class PokemonAPITests(APITestCase):
    fixtures = ["fixture.json"]

    def test_get_all_pokemon_with_types(self):
        """
        Ensure we can retrieve all Pokémon and their types.
        """
        response = self.client.get('http://127.0.0.1:8000/pokemon/')
        self.assertEqual(response.status_code, 200)
        for pokemon in response.json():
            self.assertTrue(pokemon['types'])

    def test_get_pokemon_by_id(self):
        """
        Ensure we can retrieve a Pokémon by id.
        """
        response = self.client.get('http://127.0.0.1:8000/pokemon/482/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "id": 482, "name_english": "Azelf", "name_japanese": "アグノム", "name_chinese": "亚克诺姆",
            "name_french": "Créfadet", "hp": 75, "attack": 70, "defense": 125, "special_attack": 125,
            "special_defense": 70, "speed": 115, "types": [{"type": "Psychic"}]
        })

    def test_get_pokemon_by_id_not_found(self):
        """
        Ensure we get a 404 on a Pokémon by id that doesn't exist.
        """
        response = self.client.get('http://127.0.0.1:8000/pokemon/999999999/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'error': 'Not found'})

    def test_get_pokemon_by_name(self):
        """
        Ensure we can retrieve a Pokémon by name.
        """
        response = self.client.get('http://127.0.0.1:8000/pokemon/name/mew/')
        self.assertEqual(response.json(), {
            "id": 151,
            "name_english": "Mew",
            "name_japanese": "ミュウ",
            "name_chinese": "梦幻",
            "name_french": "Mew",
            "hp": 100,
            "attack": 100,
            "defense": 100,
            "special_attack": 100,
            "special_defense": 100,
            "speed": 100,
            "types": [{"type": "Psychic"}]
        })

    def test_get_pokemon_by_name_not_found(self):
        """
        Ensure we get a 404 on pokemon name that does not exist.
        """
        response = self.client.get('http://127.0.0.1:8000/pokemon/name/webdevwithseb/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {
            "error": 'Not found'
        })

    def test_get_pokemon_by_type(self):
        """
        Ensure we can retrieve Pokémon by type.
        """
        response = self.client.get('http://127.0.0.1:8000/pokemon/type/fairy/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {"id": 35, "name_english": "Clefairy", "name_japanese": "ピッピ", "name_chinese": "皮皮",
             "name_french": "Mélofée", "hp": 70, "attack": 48, "defense": 45, "special_attack": 60,
             "special_defense": 65, "speed": 35, "types": [{"type": "Fairy"}]},
            {"id": 36, "name_english": "Clefable", "name_japanese": "ピクシー", "name_chinese": "皮可西",
             "name_french": "Mélodelfe", "hp": 95, "attack": 73, "defense": 70, "special_attack": 95,
             "special_defense": 90, "speed": 60, "types": [{"type": "Fairy"}]},
            {"id": 39, "name_english": "Jigglypuff", "name_japanese": "プリン", "name_chinese": "胖丁",
             "name_french": "Rondoudou", "hp": 115, "attack": 20, "defense": 45, "special_attack": 45,
             "special_defense": 25, "speed": 20, "types": [{"type": "Fairy"}, {"type": "Normal"}]},
            {"id": 40, "name_english": "Wigglytuff", "name_japanese": "プクリン", "name_chinese": "胖可丁",
             "name_french": "Grodoudou", "hp": 140, "attack": 45, "defense": 70, "special_attack": 85,
             "special_defense": 50, "speed": 45, "types": [{"type": "Fairy"}, {"type": "Normal"}]},
            {"id": 122, "name_english": "Mr. Mime", "name_japanese": "バリヤード", "name_chinese": "魔墙人偶",
             "name_french": "M. Mime", "hp": 40, "attack": 65, "defense": 45, "special_attack": 100,
             "special_defense": 120, "speed": 90, "types": [{"type": "Fairy"}, {"type": "Psychic"}]},
            {"id": 173, "name_english": "Cleffa", "name_japanese": "ピィ", "name_chinese": "皮宝宝",
             "name_french": "Mélo", "hp": 50, "attack": 28, "defense": 25, "special_attack": 45, "special_defense": 55,
             "speed": 15, "types": [{"type": "Fairy"}]},
            {"id": 174, "name_english": "Igglybuff", "name_japanese": "ププリン", "name_chinese": "宝宝丁",
             "name_french": "Toudoudou", "hp": 90, "attack": 15, "defense": 30, "special_attack": 40,
             "special_defense": 20, "speed": 15, "types": [{"type": "Fairy"}, {"type": "Normal"}]},
            {"id": 175, "name_english": "Togepi", "name_japanese": "トゲピー", "name_chinese": "波克比",
             "name_french": "Togepi", "hp": 35, "attack": 65, "defense": 20, "special_attack": 40,
             "special_defense": 65, "speed": 20, "types": [{"type": "Fairy"}]},
            {"id": 176, "name_english": "Togetic", "name_japanese": "トゲチック", "name_chinese": "波克基古",
             "name_french": "Togetic", "hp": 55, "attack": 85, "defense": 40, "special_attack": 80,
             "special_defense": 105, "speed": 40, "types": [{"type": "Fairy"}, {"type": "Flying"}]},
            {"id": 183, "name_english": "Marill", "name_japanese": "マリル", "name_chinese": "玛力露",
             "name_french": "Marill", "hp": 70, "attack": 50, "defense": 20, "special_attack": 20,
             "special_defense": 50, "speed": 40, "types": [{"type": "Fairy"}, {"type": "Water"}]},
            {"id": 184, "name_english": "Azumarill", "name_japanese": "マリルリ", "name_chinese": "玛力露丽",
             "name_french": "Azumarill", "hp": 100, "attack": 80, "defense": 50, "special_attack": 60,
             "special_defense": 80, "speed": 50, "types": [{"type": "Fairy"}, {"type": "Water"}]},
            {"id": 209, "name_english": "Snubbull", "name_japanese": "ブルー", "name_chinese": "布鲁",
             "name_french": "Snubbull", "hp": 60, "attack": 50, "defense": 80, "special_attack": 40,
             "special_defense": 40, "speed": 30, "types": [{"type": "Fairy"}]},
            {"id": 210, "name_english": "Granbull", "name_japanese": "グランブル", "name_chinese": "布鲁皇",
             "name_french": "Granbull", "hp": 90, "attack": 75, "defense": 120, "special_attack": 60,
             "special_defense": 60, "speed": 45, "types": [{"type": "Fairy"}]},
            {"id": 280, "name_english": "Ralts", "name_japanese": "ラルトス", "name_chinese": "拉鲁拉丝",
             "name_french": "Tarsal", "hp": 28, "attack": 25, "defense": 25, "special_attack": 45,
             "special_defense": 35, "speed": 40, "types": [{"type": "Fairy"}, {"type": "Psychic"}]},
            {"id": 281, "name_english": "Kirlia", "name_japanese": "キルリア", "name_chinese": "奇鲁莉安",
             "name_french": "Kirlia", "hp": 38, "attack": 35, "defense": 35, "special_attack": 65,
             "special_defense": 55, "speed": 50, "types": [{"type": "Fairy"}, {"type": "Psychic"}]},
            {"id": 282, "name_english": "Gardevoir", "name_japanese": "サーナイト", "name_chinese": "沙奈朵",
             "name_french": "Gardevoir", "hp": 68, "attack": 65, "defense": 65, "special_attack": 125,
             "special_defense": 115, "speed": 80, "types": [{"type": "Fairy"}, {"type": "Psychic"}]},
            {"id": 298, "name_english": "Azurill", "name_japanese": "ルリリ", "name_chinese": "露力丽",
             "name_french": "Azurill", "hp": 50, "attack": 40, "defense": 20, "special_attack": 20,
             "special_defense": 40, "speed": 20, "types": [{"type": "Fairy"}, {"type": "Normal"}]},
            {"id": 303, "name_english": "Mawile", "name_japanese": "クチート", "name_chinese": "大嘴娃",
             "name_french": "Mysdibule", "hp": 50, "attack": 85, "defense": 85, "special_attack": 55,
             "special_defense": 55, "speed": 50, "types": [{"type": "Fairy"}, {"type": "Steel"}]},
            {"id": 439, "name_english": "Mime Jr.", "name_japanese": "マネネ", "name_chinese": "魔尼尼",
             "name_french": "Mime Jr", "hp": 20, "attack": 45, "defense": 25, "special_attack": 70,
             "special_defense": 90, "speed": 60, "types": [{"type": "Fairy"}, {"type": "Psychic"}]},
            {"id": 468, "name_english": "Togekiss", "name_japanese": "トゲキッス", "name_chinese": "波克基斯",
             "name_french": "Togekiss", "hp": 85, "attack": 95, "defense": 50, "special_attack": 120,
             "special_defense": 115, "speed": 80, "types": [{"type": "Fairy"}, {"type": "Flying"}]},
            {"id": 546, "name_english": "Cottonee", "name_japanese": "モンメン", "name_chinese": "木棉球",
             "name_french": "Doudouvet", "hp": 40, "attack": 60, "defense": 27, "special_attack": 37,
             "special_defense": 50, "speed": 66, "types": [{"type": "Fairy"}, {"type": "Grass"}]},
            {"id": 547, "name_english": "Whimsicott", "name_japanese": "エルフーン", "name_chinese": "风妖精",
             "name_french": "Farfaduvet", "hp": 60, "attack": 85, "defense": 67, "special_attack": 77,
             "special_defense": 75, "speed": 116, "types": [{"type": "Fairy"}, {"type": "Grass"}]},
            {"id": 669, "name_english": "Flabébé", "name_japanese": "フラベベ", "name_chinese": "花蓓蓓",
             "name_french": "Flabébé", "hp": 44, "attack": 39, "defense": 38, "special_attack": 61,
             "special_defense": 79, "speed": 42, "types": [{"type": "Fairy"}]},
            {"id": 670, "name_english": "Floette", "name_japanese": "フラエッテ", "name_chinese": "花叶蒂",
             "name_french": "FLOETTE", "hp": 54, "attack": 47, "defense": 45, "special_attack": 75,
             "special_defense": 98, "speed": 52, "types": [{"type": "Fairy"}]},
            {"id": 671, "name_english": "Florges", "name_japanese": "フラージェス", "name_chinese": "花洁夫人",
             "name_french": "Florges", "hp": 78, "attack": 68, "defense": 65, "special_attack": 112,
             "special_defense": 154, "speed": 75, "types": [{"type": "Fairy"}]},
            {"id": 682, "name_english": "Spritzee", "name_japanese": "シュシュプ", "name_chinese": "粉香香",
             "name_french": "Fluvetin", "hp": 78, "attack": 60, "defense": 52, "special_attack": 63,
             "special_defense": 65, "speed": 23, "types": [{"type": "Fairy"}]},
            {"id": 683, "name_english": "Aromatisse", "name_japanese": "フレフワン", "name_chinese": "芳香精",
             "name_french": "Cocotine", "hp": 101, "attack": 72, "defense": 72, "special_attack": 99,
             "special_defense": 89, "speed": 29, "types": [{"type": "Fairy"}]},
            {"id": 684, "name_english": "Swirlix", "name_japanese": "ペロッパフ", "name_chinese": "绵绵泡芙",
             "name_french": "Sucroquin", "hp": 62, "attack": 66, "defense": 48, "special_attack": 59,
             "special_defense": 57, "speed": 49, "types": [{"type": "Fairy"}]},
            {"id": 685, "name_english": "Slurpuff", "name_japanese": "ペロリーム", "name_chinese": "胖甜妮",
             "name_french": "Cupcanaille", "hp": 82, "attack": 86, "defense": 80, "special_attack": 85,
             "special_defense": 75, "speed": 72, "types": [{"type": "Fairy"}]},
            {"id": 700, "name_english": "Sylveon", "name_japanese": "ニンフィア", "name_chinese": "仙子伊布",
             "name_french": "Nymphali", "hp": 95, "attack": 65, "defense": 65, "special_attack": 110,
             "special_defense": 130, "speed": 60, "types": [{"type": "Fairy"}]},
            {"id": 702, "name_english": "Dedenne", "name_japanese": "デデンネ", "name_chinese": "咚咚鼠",
             "name_french": "DEDENNE", "hp": 67, "attack": 57, "defense": 58, "special_attack": 81,
             "special_defense": 67, "speed": 101, "types": [{"type": "Electric"}, {"type": "Fairy"}]},
            {"id": 703, "name_english": "Carbink", "name_japanese": "メレシー", "name_chinese": "小碎钻",
             "name_french": "Strassie", "hp": 50, "attack": 150, "defense": 50, "special_attack": 50,
             "special_defense": 150, "speed": 50, "types": [{"type": "Fairy"}, {"type": "Rock"}]},
            {"id": 707, "name_english": "Klefki", "name_japanese": "クレッフィ", "name_chinese": "钥圈儿",
             "name_french": "Trousselin", "hp": 57, "attack": 91, "defense": 80, "special_attack": 80,
             "special_defense": 87, "speed": 75, "types": [{"type": "Fairy"}, {"type": "Steel"}]},
            {"id": 716, "name_english": "Xerneas", "name_japanese": "ゼルネアス", "name_chinese": "哲尔尼亚斯",
             "name_french": "Xerneas", "hp": 126, "attack": 95, "defense": 131, "special_attack": 131,
             "special_defense": 98, "speed": 99, "types": [{"type": "Fairy"}]},
            {"id": 719, "name_english": "Diancie", "name_japanese": "ディアンシー", "name_chinese": "蒂安希",
             "name_french": "Diancie", "hp": 50, "attack": 150, "defense": 100, "special_attack": 100,
             "special_defense": 150, "speed": 50, "types": [{"type": "Fairy"}, {"type": "Rock"}]},
            {"id": 730, "name_english": "Primarina", "name_japanese": "アシレーヌ", "name_chinese": "西狮海壬",
             "name_french": "Oratoria", "hp": 80, "attack": 74, "defense": 74, "special_attack": 126,
             "special_defense": 116, "speed": 60, "types": [{"type": "Fairy"}, {"type": "Water"}]},
            {"id": 742, "name_english": "Cutiefly", "name_japanese": "アブリー", "name_chinese": "萌虻",
             "name_french": "Bombydou", "hp": 40, "attack": 40, "defense": 45, "special_attack": 55,
             "special_defense": 40, "speed": 84, "types": [{"type": "Bug"}, {"type": "Fairy"}]},
            {"id": 743, "name_english": "Ribombee", "name_japanese": "アブリボン", "name_chinese": "蝶结萌虻",
             "name_french": "Rubombelle", "hp": 60, "attack": 60, "defense": 55, "special_attack": 95,
             "special_defense": 70, "speed": 124, "types": [{"type": "Bug"}, {"type": "Fairy"}]},
            {"id": 755, "name_english": "Morelull", "name_japanese": "ネマシュ", "name_chinese": "睡睡菇",
             "name_french": "Spododo", "hp": 40, "attack": 55, "defense": 35, "special_attack": 65,
             "special_defense": 75, "speed": 15, "types": [{"type": "Fairy"}, {"type": "Grass"}]},
            {"id": 756, "name_english": "Shiinotic", "name_japanese": "マシェード", "name_chinese": "灯罩夜菇",
             "name_french": "Lampignon", "hp": 60, "attack": 80, "defense": 45, "special_attack": 90,
             "special_defense": 100, "speed": 30, "types": [{"type": "Fairy"}, {"type": "Grass"}]},
            {"id": 764, "name_english": "Comfey", "name_japanese": "キュワワー", "name_chinese": "花疗环环",
             "name_french": "Guérilande", "hp": 51, "attack": 90, "defense": 52, "special_attack": 82,
             "special_defense": 110, "speed": 100, "types": [{"type": "Fairy"}]},
            {"id": 778, "name_english": "Mimikyu", "name_japanese": "ミミッキュ", "name_chinese": "谜拟Ｑ",
             "name_french": "Denticrisse", "hp": 55, "attack": 80, "defense": 90, "special_attack": 50,
             "special_defense": 105, "speed": 96, "types": [{"type": "Fairy"}, {"type": "Ghost"}]},
            {"id": 785, "name_english": "Tapu Koko", "name_japanese": "カプ・コケコ", "name_chinese": "卡璞・鸣鸣",
             "name_french": "Tokopiyon", "hp": 70, "attack": 85, "defense": 115, "special_attack": 95,
             "special_defense": 75, "speed": 130, "types": [{"type": "Electric"}, {"type": "Fairy"}]},
            {"id": 786, "name_english": "Tapu Lele", "name_japanese": "カプ・テテフ", "name_chinese": "卡璞・蝶蝶",
             "name_french": "Tokotoro", "hp": 70, "attack": 75, "defense": 85, "special_attack": 130,
             "special_defense": 115, "speed": 95, "types": [{"type": "Fairy"}, {"type": "Psychic"}]},
            {"id": 787, "name_english": "Tapu Bulu", "name_japanese": "カプ・ブルル", "name_chinese": "卡璞・哞哞",
             "name_french": "Tokopisco", "hp": 70, "attack": 115, "defense": 130, "special_attack": 85,
             "special_defense": 95, "speed": 75, "types": [{"type": "Fairy"}, {"type": "Grass"}]},
            {"id": 788, "name_english": "Tapu Fini", "name_japanese": "カプ・レヒレ", "name_chinese": "卡璞・鳍鳍",
             "name_french": "Cosmog", "hp": 70, "attack": 115, "defense": 75, "special_attack": 95,
             "special_defense": 130, "speed": 85, "types": [{"type": "Fairy"}, {"type": "Water"}]},
            {"id": 801, "name_english": "Magearna", "name_japanese": "マギアナ", "name_chinese": "玛机雅娜",
             "name_french": "Marshadow", "hp": 80, "attack": 115, "defense": 95, "special_attack": 130,
             "special_defense": 115, "speed": 65, "types": [{"type": "Fairy"}, {"type": "Steel"}]}])

    def test_get_pokemon_by_type_bad_request(self):
        response = self.client.get('http://127.0.0.1:8000/pokemon/type/jobsimulator/')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Bad request"})

    def test_get_pokemon_by_hp(self):
        response = self.client.get('http://127.0.0.1:8000/pokemon/hp/?gte=200&gt=250')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {"id": 242, "name_english": "Blissey", "name_japanese": "ハピナス", "name_chinese": "幸福蛋",
             "name_french": "Leuphorie", "hp": 255, "attack": 10, "defense": 10, "special_attack": 75,
             "special_defense": 135, "speed": 55, "types": [{"type": "Normal"}]}])

    def test_get_pokemon_by_hp_no_results(self):
        response = self.client.get('http://127.0.0.1:8000/pokemon/hp/?gte=1000&gt=250')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"error": "Not found"})

    def test_get_pokemon_by_hp_bad_comparator(self):
        response = self.client.get('http://127.0.0.1:8000/pokemon/hp/?cow=250')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": 'Invalid Operator. Must be one of ["gt","gte","lt","lte"]'})
