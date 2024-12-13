package main

import (
	"fmt"
	"strconv"

	"github.com/rubenhoenle/adventofcode/2024/utils"
)

func parseInput(input []string) ([][]int, error) {
	parsed := [][]int{}
	for _, line := range input {
		parsedLine := make([]int, len(line))
		for idx, char := range line {
			var err error
			parsedLine[idx], err = strconv.Atoi(string(char))
			if err != nil {
				return [][]int{}, err
			}
		}
		parsed = append(parsed, parsedLine)
	}
	return parsed, nil
}

type trailStep struct {
	y int
	x int
}

func contains(stepSlice []trailStep, step trailStep) bool {
	for _, it := range stepSlice {
		if it.y == step.y && it.x == step.x {
			return true
		}
	}
	return false
}

func findTrail(trailMap [][]int, y int, x int, expectedVal int, deduplication bool, visitedTrailEnds []trailStep) (int, []trailStep) {
	// check if out of bounds or wrong value
	maxY := len(trailMap) - 1
	maxX := len(trailMap[0]) - 1
	if y < 0 || x < 0 || y > maxY || x > maxX || trailMap[y][x] != expectedVal {
		return 0, visitedTrailEnds
	}

	if expectedVal == 9 {
		if trailMap[y][x] == 9 && (!deduplication || (deduplication && !contains(visitedTrailEnds, trailStep{y: y, x: x}))) {
			visitedTrailEnds = append(visitedTrailEnds, trailStep{y: y, x: x})
			return 1, visitedTrailEnds
		}
		return 0, visitedTrailEnds
	}

	below, visitedTrailEnds := findTrail(trailMap, y+1, x, expectedVal+1, deduplication, visitedTrailEnds) // below
	above, visitedTrailEnds := findTrail(trailMap, y-1, x, expectedVal+1, deduplication, visitedTrailEnds) // above
	right, visitedTrailEnds := findTrail(trailMap, y, x+1, expectedVal+1, deduplication, visitedTrailEnds) // right
	left, visitedTrailEnds := findTrail(trailMap, y, x-1, expectedVal+1, deduplication, visitedTrailEnds)  // left

	return below + above + right + left, visitedTrailEnds
}

func findAllTrailsOnMap(trailMap [][]int, deduplication bool) int {
	scoreSum := 0
	for y := range trailMap {
		for x := range trailMap[y] {
			incr, _ := findTrail(trailMap, y, x, 0, deduplication, []trailStep{})
			scoreSum += incr
		}
	}
	return scoreSum
}

func main() {
	input := utils.ReadLinesFromFile("input/10.txt")

	trailMap, _ := parseInput(input)

	part1Res := findAllTrailsOnMap(trailMap, true)
	fmt.Printf("Part 1: %d\n", part1Res)

	part2Res := findAllTrailsOnMap(trailMap, false)
	fmt.Printf("Part 2: %d\n", part2Res)
}
