package main

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/rubenhoenle/adventofcode/2024/utils"
)

const (
	OPERATOR_PLUS = iota
	OPERATOR_MULTIPLY
)

type equation struct {
	result  int
	numbers []int
}

func parseEquations(input []string) ([]equation, error) {
	equations := []equation{}
	re := regexp.MustCompile(`\d+`)

	for _, line := range input {
		matches := re.FindAllString(line, -1)

		e := equation{result: 0, numbers: []int{}}
		for idx, m := range matches {
			val, err := strconv.Atoi(m)
			if err != nil {
				return []equation{}, err
			}

			if idx == 0 {
				e.result = val
			} else {
				e.numbers = append(e.numbers, val)
			}
		}
		equations = append(equations, e)
	}

	return equations, nil
}

func getOperatorCombinations(length int) [][]int {
	totalCombinations := 1 << length // 2^length combinations
	result := make([][]int, totalCombinations)

	for i := 0; i < totalCombinations; i++ {
		combination := make([]int, length)
		for j := 0; j < length; j++ {
			// Check if the j-th bit of i is set to decide between A and B
			if i&(1<<j) == 0 {
				combination[j] = OPERATOR_PLUS
			} else {
				combination[j] = OPERATOR_MULTIPLY
			}
		}
		result[i] = combination
	}

	return result
}

func countOperatorCombinations(e equation) int {
	sum := 0

	for _, opCombination := range getOperatorCombinations(len(e.numbers) - 1) {
		res := e.numbers[0]
		for idx, op := range opCombination {
			switch op {
			case OPERATOR_PLUS:
				res = res + e.numbers[idx+1]
			case OPERATOR_MULTIPLY:
				res = res * e.numbers[idx+1]
			}
		}

		if res == e.result {
			sum++
		}
	}

	return sum
}

func part1(equations []equation) int {
	sum := 0
	for _, e := range equations {
		if countOperatorCombinations(e) > 0 {
			sum += e.result
		}
	}
	return sum
}

func main() {
	input := utils.ReadLinesFromFile("input/07.txt")
	equations, _ := parseEquations(input)

	part1Result := part1(equations)
	fmt.Printf("Part 1: %d\n", part1Result)
}
