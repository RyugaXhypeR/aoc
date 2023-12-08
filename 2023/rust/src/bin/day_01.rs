mod day_02;

use std::fs;

const INPUT: &str = "../inputs/day_01.txt";

const NUM_STR: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

const TEST_INPUT_P1: &str = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";

const TEST_INPUT_P2: &str = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen";

fn get_input() -> &'static str {
    fs::read_to_string(INPUT).unwrap().as_str()
}

fn part1(input: &str) -> u32 {
    input
        .lines()
        .map(|line| {
            line.chars()
                .filter(|&c| c.is_ascii_digit())
                .collect::<String>()
        })
        .map(|x| {
            (x.chars().next().unwrap().to_string()
                + &x.chars().nth(x.len() - 1).unwrap().to_string())
                .parse::<u32>()
                .unwrap()
        })
        .sum()
}

fn part2(input: &str) -> u32 {
    let mut buffer = String::new();
    let mut sum: u32 = 0;

    for line in input.lines() {
        for (i, ch) in line.chars().enumerate() {
            if ch.is_ascii_digit() {
                buffer.push(ch);
                continue;
            }
            for (j, num_str) in NUM_STR.iter().enumerate() {
                if line[i..].starts_with(num_str) {
                    buffer.push_str(&(j + 1).to_string());
                    break;
                }
            }
        }
        sum += (buffer.chars().next().unwrap().to_string()
            + &buffer.chars().last().unwrap().to_string())
            .parse::<u32>()
            .unwrap();
        buffer.clear();
    }
    sum
}

fn main() {
    let input = get_input();

    println!("{}", part1(&input));
    println!("{}", part2(&input));
}
