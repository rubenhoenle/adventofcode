package main

import (
	"fmt"

	"github.com/rubenhoenle/adventofcode/2024/utils"
)

func findWord(input []string, word string, y, x, directionY int, directionX int) bool {
	maxY := len(input) - 1
	if maxY < 0 {
		maxY = 0
	}
	maxX := len(input[0]) - 1
	if maxX < 0 {
		maxX = 0
	}

	for idx, char := range word {
		checkY := y + (directionY * idx)
		checkX := x + (directionX * idx)

		// check if we're running out of bounds...
		if checkY < 0 || checkX < 0 || checkY > maxY || checkX > maxX {
			return false
		}

		if string(input[checkY][checkX]) != string(char) {
			return false
		}
	}
	return true
}

func countWordOccurences(input []string, word string) int {
	sum := 0
	for y, line := range input {
		for x, _ := range line {
			// downwards
			if findWord(input, word, y, x, 1, 0) {
				sum++
			}
			// upwards
			if findWord(input, word, y, x, -1, 0) {
				sum++
			}
			// right
			if findWord(input, word, y, x, 0, 1) {
				sum++
			}
			// left
			if findWord(input, word, y, x, 0, -1) {
				sum++
			}
			// left upwards diagonally
			if findWord(input, word, y, x, -1, -1) {
				sum++
			}
			// left downwards diagonally
			if findWord(input, word, y, x, 1, -1) {
				sum++
			}
			// right upwards diagonally
			if findWord(input, word, y, x, -1, 1) {
				sum++
			}
			// right downwards diagonally
			if findWord(input, word, y, x, 1, 1) {
				sum++
			}
		}
	}
	return sum
}

func main() {
	input := utils.ReadLinesFromFile("input/04.txt")

	part1 := countWordOccurences(input, "XMAS")
	fmt.Printf("Part 1: %d\n", part1)
}
