package main

import (
	"fmt"
	"strings"

	"github.com/rubenhoenle/adventofcode/2024/utils"
)

const (
	DIRECTION_RIGHT = iota
	DIRECTION_LEFT
	DIRECTION_DOWN
	DIRECTION_UP
)

func findGuardPos(input []string) (int, int) {
	for y, line := range input {
		x := strings.Index(line, "^")
		if x > -1 {
			return y, x
		}
	}
	return -1, -1
}

func turnRight(direction int) int {
	switch direction {
	case DIRECTION_RIGHT:
		return DIRECTION_DOWN
	case DIRECTION_LEFT:
		return DIRECTION_UP
	case DIRECTION_DOWN:
		return DIRECTION_LEFT
	case DIRECTION_UP:
		return DIRECTION_RIGHT
	}
	return -1
}

func countPatrolledPositons(input []string) int {
	yMax := len(input) - 1
	xMax := len(input[0]) - 1

	y, x := findGuardPos(input)
	direction := DIRECTION_UP

	for {
		previousY, previousX := y, x

		switch direction {
		case DIRECTION_RIGHT:
			x++
		case DIRECTION_LEFT:
			x--
		case DIRECTION_DOWN:
			y++
		case DIRECTION_UP:
			y--
		}

		// check if out of bounds
		if y < 0 || x < 0 || y > yMax || x > xMax {
			break
		}

		// step back and turn right if an obstacle was hit
		if input[y][x] == '#' {
			y, x = previousY, previousX
			direction = turnRight(direction)
		}

		// mark as visited
		runes := []rune(input[y])
		runes[x] = 'X'
		input[y] = string(runes)
	}

	joined := strings.Join(input, "")
	return strings.Count(joined, "X")
}

func main() {
	input := utils.ReadLinesFromFile("input/06.txt")

	part1 := countPatrolledPositons(input)
	fmt.Printf("Part 1: %d\n", part1)
}
