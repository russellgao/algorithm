package main

import "fmt"

func main() {
	obj := Constructor()
	x := 6
	obj.Push(x)
	obj.Push(9)
	param_2 := obj.Pop()
	param_3 := obj.Peek()
	param_4 := obj.Empty()

	fmt.Println(param_2)
	fmt.Println(param_3)
	fmt.Println(param_4)
}

type MyQueue struct {
	inQueue  []int
	outQueue []int
}

/*Initialize your data structure here. */
func Constructor() MyQueue {
	return MyQueue{}
}

/*Push element x to the back of queue. */
func (this *MyQueue) Push(x int) {
	this.inQueue = append(this.inQueue, x)
}

func (this *MyQueue) in2out() {
	for len(this.inQueue) > 0 {
		this.outQueue = append(this.outQueue, this.inQueue[len(this.inQueue)-1])
		this.inQueue = this.inQueue[:len(this.inQueue)-1]
	}
}

/*Removes the element from in front of queue and returns that element. */
func (this *MyQueue) Pop() int {
	if len(this.outQueue) == 0 {
		this.in2out()
	}
	x := this.outQueue[len(this.outQueue)-1]
	this.outQueue = this.outQueue[:len(this.outQueue)-1]
	return x
}

/*Get the front element. */
func (this *MyQueue) Peek() int {
	if len(this.outQueue) == 0 {
		this.in2out()
	}
	return this.outQueue[len(this.outQueue)-1]
}

/*Returns whether the queue is empty. */
func (this *MyQueue) Empty() bool {
	return len(this.inQueue) == 0 && len(this.outQueue) == 0
}

/**
Your MyQueue object will be instantiated and called as such:
obj := Constructor();
obj.Push(x);
param_2 := obj.Pop();
param_3 := obj.Peek();
param_4 := obj.Empty();
*/
