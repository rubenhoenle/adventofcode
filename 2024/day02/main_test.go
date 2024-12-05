package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestParseInput(t *testing.T) {
	input := []string{
		"7 6 4 2 1",
		"1 2 7 8 9",
		"9 7 6 2 1",
		"1 3 2 4 5",
		"8 6 4 4 1",
		"1 3 6 7 9",
	}

	parsed := parseInput(input)

	assert.Equal(t, []int{7, 6, 4, 2, 1}, parsed[0])
	assert.Equal(t, []int{1, 2, 7, 8, 9}, parsed[1])
	assert.Equal(t, []int{9, 7, 6, 2, 1}, parsed[2])
	assert.Equal(t, []int{1, 3, 2, 4, 5}, parsed[3])
	assert.Equal(t, []int{8, 6, 4, 4, 1}, parsed[4])
	assert.Equal(t, []int{1, 3, 6, 7, 9}, parsed[5])
}

func TestCountSafeReports(t *testing.T) {
	assert.True(t, checkReportSafety([]int{7, 6, 4, 2, 1}))
	assert.False(t, checkReportSafety([]int{1, 2, 7, 8, 9}))
	assert.False(t, checkReportSafety([]int{9, 7, 6, 2, 1}))
	assert.False(t, checkReportSafety([]int{1, 3, 2, 4, 5}))
	assert.False(t, checkReportSafety([]int{8, 6, 4, 4, 1}))
	assert.True(t, checkReportSafety([]int{1, 3, 6, 7, 9}))

	input := [][]int{
		{7, 6, 4, 2, 1},
		{1, 2, 7, 8, 9},
		{9, 7, 6, 2, 1},
		{1, 3, 2, 4, 5},
		{8, 6, 4, 4, 1},
		{1, 3, 6, 7, 9},
	}

	safeReports := countSafeReports(input)

	assert.Equal(t, 2, safeReports)
}
