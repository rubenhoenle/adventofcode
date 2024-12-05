package main

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/rubenhoenle/adventofcode/2024/utils"
)

func getMultiplyStatements(input string) []string {
	re := regexp.MustCompile(`mul\(\d{1,3},\d{1,3}\)`)
	return re.FindAllString(input, -1)
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

func part1(inputLine string) (int, error) {
	multiplyStatements := getMultiplyStatements(inputLine)
	return sumMultiplyStatements(multiplyStatements)
}

func main() {
	inputLine := utils.ReadLinesFromFile("input/03.txt")[0]

	part1Result, _ := part1(inputLine)
	fmt.Printf("Part 1: %d\n", part1Result)
}
