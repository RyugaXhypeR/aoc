use std::fs::read_to_string;

use itertools::Itertools;

fn parse_input(aoc_raw_input: &str) -> Vec<(u64, u64)> {
    aoc_raw_input
        .split(",")
        .map(|raw_interval| {
            raw_interval
                .split("-")
                .map(|p| p.trim().parse::<u64>().unwrap())
                .collect_tuple()
                .unwrap()
        })
        .collect()
}

/// Optimized for given input. The difference between `hi` and `lo` would at max be 1 (atleast in
/// my input); round down `hi` to nearest even integer less than `hi` (could also round up `lo` to
/// nearest even integer, but rounding down is less chars).
///
/// Since now we only have single digit range to generate doublet numbers in, we have to find the
/// bounds for the doublets. For this, we either  have to upscale `lo` or downscale `hi`.
///
/// After finding the bounds, its simply summing half of the doublets and then multiplying `r2`
/// (basically duplicates the half).
///
/// More general solution (for summing doublets within any range) would look like:
///
/// ```py
/// def sum_doublets(lo: int, hi: int) -> int:
///     nd_lo = len(str(lo)) // 2
///     nd_hi = len(str(hi)) // 2
///
///     result = 0
///     for digits in range(nd_lo, nd_hi + 1):
///         r2 = 10**digits + 1
///
///         result += r2 * sum(range(
///             min(math.ceil(lo / r2), r2 / 10),
///             max(hi // r2, r2 - 2)))
///
///     return result
/// ```
fn sum_doublets(lo: u64, hi: u64) -> u64 {
    let r2 = 10u64.pow((hi.ilog10() + 1 & !1) >> 1) + 1;
    (lo.div_ceil(r2).max(r2 / 10)..=(hi / r2).min(r2 - 2)).sum::<u64>() * r2
}

fn part_one(nums: &[(u64, u64)]) -> u64 {
    nums.iter().map(|&(lo, hi)| sum_doublets(lo, hi)).sum()
}

fn part_two(nums: &[(u64, u64)]) -> u64 {
    0
}

fn main() {
    let aoc_raw_input = read_to_string("../inputs/day_02.txt").expect("Input file not found!");
    let aoc_input = parse_input(&aoc_raw_input);

    println!("{}", part_one(&aoc_input));
    println!("{}", part_two(&aoc_input));
}

#[cfg(test)]
mod tests {
    use super::*;

    use textwrap::dedent;

    #[test]
    fn test_part_one_example() {
        let nums = parse_input(&dedent(
            r#"
                11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
                1698522-1698528,446443-446449,38593856-38593862,565653-565659,
                824824821-824824827,2121212118-2121212124
            "#,
        ));

        let result = part_one(&nums);
        assert_eq!(result, 1227775554);
    }

    #[test]
    fn test_part_two_example() {
        let nums = parse_input(&dedent(
            r#"
                11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
                1698522-1698528,446443-446449,38593856-38593862,565653-565659,
                824824821-824824827,2121212118-2121212124
            "#,
        ));

        let result = part_two(&nums);
        assert_eq!(result, 4174379265);
    }
}
