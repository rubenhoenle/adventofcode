package utils

import (
	"bufio"
	"fmt"
	"os"
)

func ReadLinesFromFile(filepath string) []string {
	var lines []string

	readFile, err := os.Open(filepath)
	if err != nil {
		fmt.Println(err)
	}

	fileScanner := bufio.NewScanner(readFile)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		line := fileScanner.Text()
		if len(line) > 0 {
			lines = append(lines, line)
		}
	}

	readFile.Close()
	return lines
}

func SliceSum(slice []int) int {
	sum := 0
	for _, val := range slice {
		sum += val
	}
	return sum
}
