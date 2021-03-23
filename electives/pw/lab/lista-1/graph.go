package main

import (
	"strconv"
	"strings"
)

// The list of columns that are currently being rendered.
type Columns []int

// Add a new column.
func (cols *Columns) Add(newCol int) int {

	// look for an empty, already created, column
	for i, c := range *cols {
		if c == -1 {
			(*cols)[i] = newCol
			return i
		}
	}

	// no empty column found, add a new one
	*cols = append(*cols, newCol)

	return len(*cols) - 1

}

// Remove column by index.
func (cols *Columns) RemoveByIndex(index int) {

	(*cols)[index] = -1

}

func (cols *Columns) TerminateByIndex(index int) {

	(*cols)[index] = -2

}

func (cols Columns) PrintGraph(vertices []*Node) {

	n := len(vertices)

	numOffset := strings.Repeat(" ", len(strconv.Itoa(n-1)))

	for i := 0; i < n; i++ {

		print(i)
		currentOffset := strings.Repeat(" ", len(numOffset)-len(strconv.Itoa(i)))
		print(currentOffset)

		// remove those edges that have been terminated
		for j, col := range cols {
			if col == -2 {
				cols.RemoveByIndex(j)
			}
		}
		// terminate edges that arrived at their destination
		for j, col := range cols {
			if col == i {
				cols.TerminateByIndex(j)
			}
		}

		// add new edges
		current := vertices[i]
		// mark them as new for the renderer
		newCols := make(map[int]bool)
		for _, neighbour := range current.neighbours {
			x := cols.Add(neighbour.id)
			newCols[x] = true
		}

		// print edges
		for j, col := range cols {
			if newCols[j] {
				print("  ·  ")
			} else if col > -1 {
				print("  |  ")
			} else if col == -2 {
				print("  ↓  ")
			} else {
				print("     ")
			}
		}
		print("\n")
		print(numOffset)
		for _, col := range cols {
			if col > -1 {
				print("  |  ")
			} else {
				print("     ")
			}
		}

		print("\n")

	}
}
