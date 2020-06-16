package main

import (
	"fmt"
	"strconv"
	"strings"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func main() {
	obj := Constructor()
	data := "1,2,3,null,null,4,5"
	ans := obj.deserialize(data)
	data1 := obj.serialize(ans)
	fmt.Println(data1)
	fmt.Println(ans)

}

type Codec struct {
	list []string
}

func Constructor() Codec {
	return Codec{}
}

func (this *Codec) rserialize(root *TreeNode, str string) string {
	if root == nil {
		str += "null,"
	} else {
		str += strconv.Itoa(root.Val) + ","
		str = this.rserialize(root.Left, str)
		str = this.rserialize(root.Right, str)
	}
	return str
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	return this.rserialize(root, "")
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	list := strings.Split(data, ",")
	for i := 0; i < len(list); i++ {
		if list[i] != "" {
			this.list = append(this.list, list[i])
		}
	}
	return this.rdeserialize()
}

func (this *Codec) rdeserialize() *TreeNode {
	if len(this.list) == 0 {
		return nil
	}
	if this.list[0] == "null" {
		this.list = this.list[1:]
		return nil
	}
	val, _ := strconv.Atoi(this.list[0])
	this.list = this.list[1:]
	root := &TreeNode{Val: val}
	root.Left = this.rdeserialize()
	root.Right = this.rdeserialize()
	return root
}
