type ListNode struct {
   Val int
   Next *ListNode

// 方法一 : 递归
func reverseKGroup(head *ListNode, k int) *ListNode {
    current := head
    count := 0
    for current != nil && count != k {
        current = current.Next
        count += 1
    }
    if count == k {
        current = reverseKGroup(current, k)
        for count != 0 {
            tmp := head.Next
            head.Next = current
            current = head
            head = tmp
            count -= 1
        }
        head = current
    }
    return head
}