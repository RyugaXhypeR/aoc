use std::collections::HashMap;
use std::fs;

const INPUT: &str = "../inputs/day_02.txt";

const TEST_INPUT: &str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

const IS_FINAL: bool = false;

fn get_input() -> String {
    if IS_FINAL {
        fs::read_to_string(INPUT).unwrap()
    } else {
        TEST_INPUT.to_string()
    }
}

fn clean_input(aoc_input: String) -> Vec<HashMap<String, Vec<u32>>> {
    let mut games = vec![];
    for line in aoc_input.split_terminator('\n') {
        let mut color_map: HashMap<String, Vec<u32>> = HashMap::new();

        for game in line.split(':').collect::<Vec<String>>()[1].split(';') {
            // TODO: Collect as (&str, &str) and directly unpack in the loop
            for ball_with_color in game
                .split(',')
                .map(|_game| _game.split_ascii_whitespace().collect::<Vec<String>>())
            {
                let num_balls = ball_with_color[0];
                let color = ball_with_color[1];
                color_map
                    .entry(&color)
                    .or_default()
                    .push(num_balls.parse().unwrap())
            }
        }
        games.push(color_map);
    }

    return games;
}

fn part1(input: String) -> u32 {
    unimplemented!()
}

fn part2(input: String) -> u32 {
    unimplemented!()
}

fn main() {
    let binding = get_input();
    let input = binding.as_str();
    let games = clean_input(input);
}
