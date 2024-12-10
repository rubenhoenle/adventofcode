package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestParseEquations(t *testing.T) {
	input := []string{
		"190: 10 19",
		"3267: 81 40 27",
		"83: 17 5",
		"156: 15 6",
		"7290: 6 8 6 15",
		"161011: 16 10 13",
		"192: 17 8 14",
		"21037: 9 7 18 13",
		"292: 11 6 16 20",
	}

	res, _ := parseEquations(input)

	assert.Equal(t, 190, res[0].result)
	assert.Equal(t, []int{10, 19}, res[0].numbers)

	assert.Equal(t, 3267, res[1].result)
	assert.Equal(t, []int{81, 40, 27}, res[1].numbers)

	assert.Equal(t, 83, res[2].result)
	assert.Equal(t, []int{17, 5}, res[2].numbers)

	assert.Equal(t, 156, res[3].result)
	assert.Equal(t, []int{15, 6}, res[3].numbers)

	assert.Equal(t, 7290, res[4].result)
	assert.Equal(t, []int{6, 8, 6, 15}, res[4].numbers)

	assert.Equal(t, 161011, res[5].result)
	assert.Equal(t, []int{16, 10, 13}, res[5].numbers)

	assert.Equal(t, 192, res[6].result)
	assert.Equal(t, []int{17, 8, 14}, res[6].numbers)

	assert.Equal(t, 21037, res[7].result)
	assert.Equal(t, []int{9, 7, 18, 13}, res[7].numbers)

	assert.Equal(t, 292, res[8].result)
	assert.Equal(t, []int{11, 6, 16, 20}, res[8].numbers)
}

func getExampleEquations() []equation {
	return []equation{
		{result: 190, numbers: []int{10, 19}},
		{result: 3267, numbers: []int{81, 40, 27}},
		{result: 83, numbers: []int{17, 5}},
		{result: 156, numbers: []int{15, 6}},
		{result: 7290, numbers: []int{6, 8, 6, 15}},
		{result: 161011, numbers: []int{16, 10, 13}},
		{result: 192, numbers: []int{17, 8, 14}},
		{result: 21037, numbers: []int{9, 7, 18, 13}},
		{result: 292, numbers: []int{11, 6, 16, 20}},
	}
}

func TestCountOperatorCombinations(t *testing.T) {
	equations := getExampleEquations()

	assert.Equal(t, 1, countOperatorCombinations(equations[0]))
	assert.Equal(t, 2, countOperatorCombinations(equations[1]))
	assert.Equal(t, 0, countOperatorCombinations(equations[2]))
	assert.Equal(t, 0, countOperatorCombinations(equations[3]))
	assert.Equal(t, 0, countOperatorCombinations(equations[4]))
	assert.Equal(t, 0, countOperatorCombinations(equations[5]))
	assert.Equal(t, 0, countOperatorCombinations(equations[6]))
	assert.Equal(t, 0, countOperatorCombinations(equations[7]))
	assert.Equal(t, 1, countOperatorCombinations(equations[8]))
}

func TestPart1Example(t *testing.T) {
	equations := getExampleEquations()

	assert.Equal(t, 3749, part1(equations))
}
