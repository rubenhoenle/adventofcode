package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

func getTestInput() []string {
	input := []string{
		"....#.....",
		".........#",
		"..........",
		"..#.......",
		".......#..",
		"..........",
		".#..^.....",
		"........#.",
		"#.........",
		"......#...",
	}
	return input
}

func TestFindGuardPosition(t *testing.T) {
	input := getTestInput()

	y, x := findGuardPos(input)
	assert.Equal(t, 6, y)
	assert.Equal(t, 4, x)
}

func TestTurnRight(t *testing.T) {
	assert.Equal(t, DIRECTION_UP, turnRight(DIRECTION_LEFT))
	assert.Equal(t, DIRECTION_LEFT, turnRight(DIRECTION_DOWN))
	assert.Equal(t, DIRECTION_DOWN, turnRight(DIRECTION_RIGHT))
	assert.Equal(t, DIRECTION_RIGHT, turnRight(DIRECTION_UP))
}

func TestCountPatrolledPositions(t *testing.T) {
	input := getTestInput()

	count := countPatrolledPositons(input)

	for _, it := range input {
		fmt.Println(it)
	}

	assert.Equal(t, 41, count)
}
