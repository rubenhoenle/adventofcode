package main

import (
	"fmt"
	"regexp"
	"sort"
	"strconv"

	"github.com/rubenhoenle/adventofcode/2024/utils"
)

func getSplitLists(input []string) ([]int, []int) {
	var leftList, rightList []int
	re := regexp.MustCompile(`\d+`)

	for _, line := range input {
		findings := re.FindAllString(line, -1)
		leftNum, _ := strconv.Atoi(findings[0])
		rightNum, _ := strconv.Atoi(findings[1])

		leftList = append(leftList, leftNum)
		rightList = append(rightList, rightNum)
	}
	return leftList, rightList
}

func part1(leftList []int, rightList []int) int {
	var differences []int

	for idx, leftNum := range leftList {
		rightNum := rightList[idx]

		difference := rightNum - leftNum
		if difference < 0 {
			difference = difference * -1
		}

		differences = append(differences, difference)
	}
	return utils.SliceSum(differences)
}

func part2(leftList []int, rightList []int) int {
	similarCount := 0

	for _, leftNum := range leftList {
		count := 0
		for _, it := range rightList {
			if it == leftNum {
				count++
			}
		}
		similarCount += count * leftNum
	}
	return similarCount
}

func main() {
	//lines := utils.ReadLinesFromFile("examples/01-1.txt")
	lines := utils.ReadLinesFromFile("input/01.txt")

	leftList, rightList := getSplitLists(lines)
	sort.Ints(leftList)
	sort.Ints(rightList)

	part1 := part1(leftList, rightList)
	part2 := part2(leftList, rightList)
	fmt.Printf("Part 1: %d\n", part1)
	fmt.Printf("Part 2: %d\n", part2)
}
