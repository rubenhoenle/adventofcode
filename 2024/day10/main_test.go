package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestParseInput(t *testing.T) {
	input := []string{
		"0123",
		"1234",
		"8765",
		"9876",
	}

	parsed, err := parseInput(input)

	assert.NoError(t, err)
	assert.Equal(t, 4, len(parsed))
	assert.Equal(t, []int{0, 1, 2, 3}, parsed[0])
	assert.Equal(t, []int{1, 2, 3, 4}, parsed[1])
	assert.Equal(t, []int{8, 7, 6, 5}, parsed[2])
	assert.Equal(t, []int{9, 8, 7, 6}, parsed[3])
}

func TestPart1(t *testing.T) {
	input := []string{
		"89010123",
		"78121874",
		"87430965",
		"96549874",
		"45678903",
		"32019012",
		"01329801",
		"10456732",
	}

	trailMap, err := parseInput(input)
	assert.NoError(t, err)

	res, _ := findTrail(trailMap, 0, 2, 0, true, []trailStep{})
	assert.Equal(t, 5, res)

	res, _ = findTrail(trailMap, 0, 4, 0, true, []trailStep{})
	assert.Equal(t, 6, res)

	res, _ = findTrail(trailMap, 2, 4, 0, true, []trailStep{})
	assert.Equal(t, 5, res)

	res, _ = findTrail(trailMap, 4, 6, 0, true, []trailStep{})
	assert.Equal(t, 3, res)

	res, _ = findTrail(trailMap, 5, 2, 0, true, []trailStep{})
	assert.Equal(t, 1, res)

	res, _ = findTrail(trailMap, 5, 5, 0, true, []trailStep{})
	assert.Equal(t, 3, res)

	res, _ = findTrail(trailMap, 6, 0, 0, true, []trailStep{})
	assert.Equal(t, 5, res)

	res, _ = findTrail(trailMap, 6, 6, 0, true, []trailStep{})
	assert.Equal(t, 3, res)

	res, _ = findTrail(trailMap, 7, 1, 0, true, []trailStep{})
	assert.Equal(t, 5, res)

	// final test
	assert.Equal(t, 36, findAllTrailsOnMap(trailMap, true))
}

func TestPart2(t *testing.T) {
	input := []string{
		"89010123",
		"78121874",
		"87430965",
		"96549874",
		"45678903",
		"32019012",
		"01329801",
		"10456732",
	}

	trailMap, err := parseInput(input)
	assert.NoError(t, err)

	res, _ := findTrail(trailMap, 0, 2, 0, false, []trailStep{})
	assert.Equal(t, 20, res)

	res, _ = findTrail(trailMap, 0, 4, 0, false, []trailStep{})
	assert.Equal(t, 24, res)

	res, _ = findTrail(trailMap, 2, 4, 0, false, []trailStep{})
	assert.Equal(t, 10, res)

	res, _ = findTrail(trailMap, 4, 6, 0, false, []trailStep{})
	assert.Equal(t, 4, res)

	res, _ = findTrail(trailMap, 5, 2, 0, false, []trailStep{})
	assert.Equal(t, 1, res)

	res, _ = findTrail(trailMap, 5, 5, 0, false, []trailStep{})
	assert.Equal(t, 4, res)

	res, _ = findTrail(trailMap, 6, 0, 0, false, []trailStep{})
	assert.Equal(t, 5, res)

	res, _ = findTrail(trailMap, 6, 6, 0, false, []trailStep{})
	assert.Equal(t, 8, res)

	res, _ = findTrail(trailMap, 7, 1, 0, false, []trailStep{})
	assert.Equal(t, 5, res)

	// final test
	assert.Equal(t, 81, findAllTrailsOnMap(trailMap, false))
}
