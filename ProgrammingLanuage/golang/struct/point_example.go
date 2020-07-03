package main

import (
	"fmt"
)

type myInterface interface {
	ChangeName(string)
	SayName()
}

type myStruct struct {
	Name string
}

func (m *myStruct) ChangeName(newName string) {
	m.Name = newName
}

func (m myStruct) SayName() {
	fmt.Println(m.Name)
}

func SetName(s myInterface, name string) {
	s.ChangeName(name)
}

func main() {
	mystruct := myStruct{Name: "xiaop"}

	//SetName(mystruct,"poilk")
	// 这个写法会报错，因为指针类型实现的接口函数只能算是指针类型实现的

	SetName(&mystruct, "Chow")
	// 这个没有问题，用结构体类型实现的方法也作为是指针类型实现的
}

// 参考
https://juejin.im/post/5cc2ddf16fb9a032514bb41f

