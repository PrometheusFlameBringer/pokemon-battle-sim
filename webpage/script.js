const pokemon_a = document.getElementById("pokemon_a");
const pokemon_b = document.getElementById("pokemon_b");
const move_a = document.getElementById("move_a");
const move_b = document.getElementById("move_b");
const move_c = document.getElementById("move_c");
const move_d = document.getElementById("move_d");

move_a.innerHTML = "1";
move_b.innerHTML = "2";
move_c.innerHTML = "3";
move_d.innerHTML = "4";

function setPoke(poke) {
    poke_name = poke.querySelector('h1');
    poke_sprite = poke.querySelector('img');
    poke_name.innerHTML = "Clefable";
    poke_sprite.src = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/36.png";
}

setPoke(pokemon_a)
