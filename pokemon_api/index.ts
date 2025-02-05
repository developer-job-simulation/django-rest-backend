import { DB } from "https://deno.land/x/sqlite/mod.ts";

import pokedex from "./pokedex.json" assert { type: "json" };

// Open a database
const db = new DB("db.sqlite3");

// Run a simple query
for (const pokemon of pokedex) {
  let p = [
    pokemon.id,
    pokemon.name.chinese,
    pokemon.name.english,
    pokemon.name.french,
    pokemon.name.japanese,
    pokemon.base.HP,
    pokemon.base.Attack,
    pokemon.base.Defense,
    pokemon.base["Sp. Attack"],
    pokemon.base["Sp. Defense"],
    pokemon.base.Speed,
  ];
  db.query(
    "INSERT INTO pokemon (id, name_chinese, name_english, name_french, name_japanese, attack, defense, hp, special_attack, special_defense, speed) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
    p
  );
  for (const type of pokemon.type) {
    db.query("INSERT INTO pokemon_types (pokemon_id, type) VALUES (?,?)", [pokemon.id, type]);
  }
}

// Close connection
db.close();
