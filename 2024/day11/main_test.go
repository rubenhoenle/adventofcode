package main

import (
	"strings"
	"testing"

	"github.com/rubenhoenle/adventofcode/2024/utils"
	"github.com/stretchr/testify/assert"
)

func TestGetStonesMap(t *testing.T) {
	t.Run("case1", func(t *testing.T) {
		stones := []int{0, 1, 10, 99, 999}
		stoneMap := getStonesMap(stones)

		assert.Equal(t, 5, len(stoneMap))
		assert.Equal(t, 1, stoneMap[0])
		assert.Equal(t, 1, stoneMap[1])
		assert.Equal(t, 1, stoneMap[10])
		assert.Equal(t, 1, stoneMap[99])
		assert.Equal(t, 1, stoneMap[999])
	})

	t.Run("case2", func(t *testing.T) {
		stones := []int{1, 2024, 1, 0, 9, 9, 2021976}
		stoneMap := getStonesMap(stones)

		assert.Equal(t, 5, len(stoneMap))
		assert.Equal(t, 1, stoneMap[0])
		assert.Equal(t, 2, stoneMap[1])
		assert.Equal(t, 2, stoneMap[9])
		assert.Equal(t, 1, stoneMap[2024])
		assert.Equal(t, 1, stoneMap[2021976])
	})
}

func TestParseStoneInput(t *testing.T) {
	t.Run("case1", func(t *testing.T) {
		stones, err := parseStoneInput(strings.Split("0 1 10 99 999", " "))

		assert.NoError(t, err)
		assert.Equal(t, 5, len(stones))
		assert.Equal(t, 0, stones[0])
		assert.Equal(t, 1, stones[1])
		assert.Equal(t, 10, stones[2])
		assert.Equal(t, 99, stones[3])
		assert.Equal(t, 999, stones[4])
	})

	t.Run("case2", func(t *testing.T) {
		stones, err := parseStoneInput(strings.Split("1 2024 1 0 9 9 2021976", " "))

		assert.NoError(t, err)
		assert.Equal(t, 7, len(stones))
		assert.Equal(t, 1, stones[0])
		assert.Equal(t, 2024, stones[1])
		assert.Equal(t, 1, stones[2])
		assert.Equal(t, 0, stones[3])
		assert.Equal(t, 9, stones[4])
		assert.Equal(t, 9, stones[5])
		assert.Equal(t, 2021976, stones[6])
	})
}

func TestBlink(t *testing.T) {
	stones := []int{125, 17}

	stonesMap := getStonesMap(stones)

	t.Run("single iteration", func(t *testing.T) {
		res := blinkNTimes(1, stonesMap)

		assert.Equal(t, 3, len(res))
		assert.Equal(t, 3, utils.SumMapValues(res))
		assert.Equal(t, 1, res[253000])
		assert.Equal(t, 1, res[1])
		assert.Equal(t, 1, res[7])
	})

	t.Run("2 iterations", func(t *testing.T) {
		res := blinkNTimes(2, stonesMap)

		assert.Equal(t, 4, len(res))
		assert.Equal(t, 4, utils.SumMapValues(res))
		assert.Equal(t, 1, res[253])
		assert.Equal(t, 1, res[0])
		assert.Equal(t, 1, res[2024])
		assert.Equal(t, 1, res[14168])
	})

	t.Run("3 iterations", func(t *testing.T) {
		res := blinkNTimes(3, stonesMap)

		assert.Equal(t, 5, len(res))
		assert.Equal(t, 5, utils.SumMapValues(res))
		assert.Equal(t, 1, res[512072])
		assert.Equal(t, 1, res[1])
		assert.Equal(t, 1, res[20])
		assert.Equal(t, 1, res[24])
		assert.Equal(t, 1, res[28676032])
	})

	t.Run("4 iterations", func(t *testing.T) {
		res := blinkNTimes(4, stonesMap)

		assert.Equal(t, 8, len(res))
		assert.Equal(t, 9, utils.SumMapValues(res))
		assert.Equal(t, 1, res[512])
		assert.Equal(t, 1, res[72])
		assert.Equal(t, 1, res[2024])
		assert.Equal(t, 2, res[2])
		assert.Equal(t, 1, res[0])
		assert.Equal(t, 1, res[4])
		assert.Equal(t, 1, res[2867])
		assert.Equal(t, 1, res[6032])
	})

	t.Run("5 iterations", func(t *testing.T) {
		res := blinkNTimes(5, stonesMap)

		assert.Equal(t, 12, len(res))
		assert.Equal(t, 13, utils.SumMapValues(res))
		assert.Equal(t, 1, res[1036288])
		assert.Equal(t, 1, res[7])
		assert.Equal(t, 1, res[2])
		assert.Equal(t, 1, res[20])
		assert.Equal(t, 1, res[24])
		assert.Equal(t, 2, res[4048])
		assert.Equal(t, 1, res[1])
		assert.Equal(t, 1, res[8096])
		assert.Equal(t, 1, res[28])
		assert.Equal(t, 1, res[67])
		assert.Equal(t, 1, res[60])
		assert.Equal(t, 1, res[32])
	})

	t.Run("6 iterations", func(t *testing.T) {
		res := blinkNTimes(6, stonesMap)

		assert.Equal(t, 15, len(res))
		assert.Equal(t, 22, utils.SumMapValues(res))
		assert.Equal(t, 1, res[2097446912])
		assert.Equal(t, 1, res[14168])
		assert.Equal(t, 1, res[4048])
		assert.Equal(t, 4, res[2])
		assert.Equal(t, 2, res[0])
		assert.Equal(t, 1, res[4])
		assert.Equal(t, 2, res[40])
		assert.Equal(t, 2, res[48])
		assert.Equal(t, 1, res[2024])
		assert.Equal(t, 1, res[80])
		assert.Equal(t, 1, res[96])
		assert.Equal(t, 1, res[8])
		assert.Equal(t, 2, res[6])
		assert.Equal(t, 1, res[7])
		assert.Equal(t, 1, res[3])
	})
}

func TestE2E(t *testing.T) {
	stones, err := parseStoneInput(strings.Split("125 17", " "))

	assert.NoError(t, err)
	assert.Equal(t, 2, len(stones))

	stoneMap := getStonesMap(stones)

	res := blinkNTimes(25, stoneMap)

	assert.Equal(t, 55312, utils.SumMapValues(res))
}
