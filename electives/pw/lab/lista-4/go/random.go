package main

import (
	"math/rand"
	"time"
)

// [internal function]
//
// Returns a new random number generator.
func getRandomNumberGenerator() *rand.Rand {

	seed := rand.NewSource(time.Now().UnixNano())

	random := rand.New(seed)

	return random

}

// RandomInteger returns a random integer.
func RandomInteger(end int) int {

	random := getRandomNumberGenerator()

	// edge case
	if end == 0 {
		return 0
	}
	return random.Intn(end)

}

// RandomFloat returns a random floating point number between [0, 1).
func RandomFloat() float64 {

	random := getRandomNumberGenerator()

	return random.Float64()

}

// SleepForSomeTime takes a moment of contemplation.
func SleepForSomeTime(sleepMax float64) {
	time.Sleep(time.Duration(1000*RandomFloat()*sleepMax) * time.Millisecond)
}

// SleepForExactTime takes a moment of contemplation of exact given duration.
func SleepForExactTime(sleepDuration float64) {
	time.Sleep(time.Duration(1000*sleepDuration) * time.Millisecond)
}
