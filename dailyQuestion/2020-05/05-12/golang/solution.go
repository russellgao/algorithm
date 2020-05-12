type MinStack struct {
    stack   []int
    min_stack   []int
}


/** initialize your data structure here. */
func Constructor() MinStack {
    return MinStack{
        stack: []int{},
        min_stack: []int{math.MaxInt64},
    }
}


func (this *MinStack) Push(x int)  {
    this.stack = append(this.stack,x)
    top := this.min_stack[len(this.min_stack)-1]
    this.min_stack = append(this.min_stack, min(x,top))
}


func (this *MinStack) Pop()  {
    this.stack = this.stack[:len(this.stack)-1]
    this.min_stack = this.min_stack[:len(this.min_stack)-1]
}


func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1]
}


func (this *MinStack) GetMin() int {
    return this.min_stack[len(this.min_stack)-1]
}

func min(x,y int) int {
    if x > y {
        return y
    }
    return x
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */