package main

import (
	"fmt"
	"slices"
	"sort"
	"strconv"
	"strings"

	"github.com/rubenhoenle/adventofcode/2024/utils"
)

func parseInput(input []string) [][]int {
	reports := make([][]int, len(input))
	for lineIdx, line := range input {
		var levelsStr []string = strings.Fields(line)

		report := make([]int, len(levelsStr))
		for idx, it := range levelsStr {
			level, _ := strconv.Atoi(it)
			report[idx] = level
		}
		reports[lineIdx] = report
	}
	return reports
}

func checkReportSafety(report []int) bool {
	reversed := make([]int, len(report))
	copy(reversed, report)

	slices.Reverse(reversed)
	if !(sort.IntsAreSorted(report) || sort.IntsAreSorted(reversed)) {
		return false
	}

	for idx, _ := range report {
		if idx == 0 {
			continue
		}
		diff := report[idx] - report[idx-1]
		if diff < -3 || diff > 3 || diff == 0 {
			return false
		}
	}
	return true
}

func countSafeReports(reports [][]int) int {
	count := 0
	for _, report := range reports {
		if checkReportSafety(report) {
			count++
		}
	}
	return count
}

func main() {
	lines := utils.ReadLinesFromFile("input/02.txt")
	reports := parseInput(lines)

	part1 := countSafeReports(reports)
	fmt.Printf("Part 1: %d\n", part1)
}