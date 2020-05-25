package main

import (
	"fmt"
)

type LRUCache struct {
	size     int
	capacity int
	cache    map[int]*DLinkNode
	head     *DLinkNode
	tail     *DLinkNode
}

type DLinkNode struct {
	key   int
	value int
	prev  *DLinkNode
	next  *DLinkNode
}

func initDLinkNode(key, value int) *DLinkNode {
	return &DLinkNode{
		key:   key,
		value: value,
	}
}

func Constructor(capacity int) LRUCache {
	lru := LRUCache{
		capacity: capacity,
		cache:    map[int]*DLinkNode{},
		head:     initDLinkNode(0, 0),
		tail:     initDLinkNode(0, 0),
	}
	lru.head.next = lru.tail
	lru.tail.prev = lru.head
	return lru
}

func (this *LRUCache) Get(key int) int {
	node, ok := this.cache[key]
	if !ok {
		return -1
	}
	this.move_to_head(node)
	return node.value
}

func (this *LRUCache) Put(key int, value int) {
	node, ok := this.cache[key]
	if !ok {
		node := initDLinkNode(key, value)
		this.size++
		this.cache[key] = node
		this.add_node(node)
		if this.size > this.capacity {
			tail := this.pop_node()
			delete(this.cache, tail.key)
			this.size--
		}
	} else {
		node.value = value
		this.move_to_head(node)
	}

}

func (this *LRUCache) add_node(node *DLinkNode) {
	node.next = this.head.next
	node.prev = this.head

	this.head.next.prev = node
	this.head.next = node
}

func (this *LRUCache) delete_node(node *DLinkNode) {
	prev := node.prev
	next := node.next

	node.prev.next = next
	node.next.prev = prev
}

func (this *LRUCache) move_to_head(node *DLinkNode) {
	this.delete_node(node)
	this.add_node(node)
}

func (this *LRUCache) pop_node() *DLinkNode {
	prev := this.tail.prev
	this.delete_node(prev)
	return prev
}

func main() {
	s := 2334
	result := Constructor(s)
	fmt.Println(result)
}
