package main

import "fmt"

type CQueue struct {
	stack_in  []int
	stack_out []int
}

func Constructor() CQueue {
	return CQueue{stack_in: []int{}, stack_out: []int{}}
}

func (this *CQueue) AppendTail(value int) {
	this.stack_in = append(this.stack_in, value)
}

func (this *CQueue) DeleteHead() int {
	if len(this.stack_out) == 0 {
		for len(this.stack_in) != 0 {
			item := this.stack_in[len(this.stack_in)-1]
			this.stack_out = append(this.stack_out, item)
			this.stack_in = this.stack_in[0 : len(this.stack_in)-1]
		}
	}
	if len(this.stack_out) != 0 {
		item := this.stack_out[len(this.stack_out)-1]
		this.stack_out = this.stack_out[0 : len(this.stack_out)-1]
		return item
	}
	return -1
}

func main() {
	obj := Constructor()
	obj.AppendTail(1)
	obj.AppendTail(2)
	obj.AppendTail(3)
	fmt.Println(obj.DeleteHead())
	fmt.Println(obj.DeleteHead())
	obj.AppendTail(4)
	fmt.Println(obj.DeleteHead())
	fmt.Println(obj.DeleteHead())
	fmt.Println(obj.DeleteHead())

}
