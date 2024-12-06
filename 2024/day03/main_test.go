package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestGetMultiplyStatementsPart1(t *testing.T) {
	input := "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

	multiplyStatements := getMultiplyStatementsPart1(input)

	assert.Equal(t, 4, len(multiplyStatements))

	assert.Contains(t, multiplyStatements, "mul(2,4)")
	assert.Contains(t, multiplyStatements, "mul(5,5)")
	assert.Contains(t, multiplyStatements, "mul(11,8)")
	assert.Contains(t, multiplyStatements, "mul(8,5)")
}

func TestCalcMultiplyStatement(t *testing.T) {
	res1, _ := calcMultiplyStatement("mul(2,4)")
	assert.Equal(t, 8, res1)

	res2, _ := calcMultiplyStatement("mul(5,5)")
	assert.Equal(t, 25, res2)

	res3, _ := calcMultiplyStatement("mul(11,8)")
	assert.Equal(t, 88, res3)

	res4, _ := calcMultiplyStatement("mul(8,5)")
	assert.Equal(t, 40, res4)
}

func TestSumMultiplyStatements(t *testing.T) {
	multiplyStatements := []string{"mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"}

	res, _ := sumMultiplyStatements(multiplyStatements)
	assert.Equal(t, 161, res)
}

func TestPart1Example(t *testing.T) {
	input := "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

	res, _ := part1(input)
	assert.Equal(t, 161, res)
}

func TestPart2Example(t *testing.T) {
	input := "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

	res := part2(input)
	assert.Equal(t, 48, res)
}
