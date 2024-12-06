package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"github.com/rubenhoenle/adventofcode/2024/utils"
)

func getMultiplyStatementsPart1(input string) []string {
	re := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)`)
	return re.FindAllString(input, -1)
}

func part2(input string) int {
	re := regexp.MustCompile(`(?:don't\(\)(?:.*?do\(\)|.*?$))|mul\((\d{1,3}),(\d{1,3})\)`)
	matches := re.FindAllStringSubmatch(input, -1)

	sum := 0
	for _, it := range matches {
		if len(it) < 3 {
			continue
		}
		a, _ := strconv.Atoi(it[1])
		b, _ := strconv.Atoi(it[2])
		sum += a * b
	}
	return sum
}

func calcMultiplyStatement(multiplyStmt string) (int, error) {
	re := regexp.MustCompile(`\d+`)
	matches := re.FindAllString(multiplyStmt, -1)

	a, err := strconv.Atoi(matches[0])
	if err != nil {
		return 0, err
	}
	b, err := strconv.Atoi(matches[1])
	if err != nil {
		return 0, err
	}

	return a * b, nil
}

func sumMultiplyStatements(multiplyStmts []string) (int, error) {
	sum := 0
	for _, stmt := range multiplyStmts {
		res, err := calcMultiplyStatement(stmt)
		if err != nil {
			return 0, err
		}
		sum += res
	}
	return sum, nil
}

func part1(input string) (int, error) {
	multiplyStatements := getMultiplyStatementsPart1(input)
	return sumMultiplyStatements(multiplyStatements)
}

func main() {
	inputLines := utils.ReadLinesFromFile("input/03.txt")
	input := strings.Join(inputLines, "")

	part1Result, _ := part1(input)
	fmt.Printf("Part 1: %d\n", part1Result)

	part2Result := part2(input)
	fmt.Printf("Part 2: %d\n", part2Result)
}
