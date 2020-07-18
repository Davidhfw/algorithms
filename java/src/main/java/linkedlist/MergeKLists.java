package main.java.linkedlist;

import java.util.Comparator;
import java.util.PriorityQueue;

public class MergeKLists {

    public static ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        PriorityQueue<ListNode> queue = new PriorityQueue<>(lists.length, new Comparator<ListNode>() {

            @Override
            public int compare(ListNode o1, ListNode o2) {
                if(o1.val < o2.val) return -1;
                else if (o1.val == o2.val) return 0;
                else return 1;
            }
        });
       ListNode dummy = new ListNode(0);
       ListNode p = dummy;
       for(ListNode node: lists) {
           if(node != null) queue.add(node);
       }
       while(!queue.isEmpty()) {
           p.next = queue.poll();
           p = p.next;
           if(p.next != null) queue.add(p.next);
       }
       return dummy;
    }

    public static void main(String[] args) {
        ListNode listNode1 = new ListNode(1);
        listNode1.next = new ListNode(2);
        listNode1.next.next = new ListNode(4);
        ListNode listNode2 = new ListNode(2);
        listNode2.next = new ListNode(3);
        listNode2.next = new ListNode(7);
        ListNode listNode3 = new ListNode(3);
        listNode3.next = new ListNode(8);
        ListNode[] lists = new ListNode[] {listNode1, listNode2,listNode3};
        ListNode dummy = MergeKLists.mergeKLists(lists);
        while(dummy.next != null) {
            System.out.println(dummy.next.val);
            dummy = dummy.next;
        }

    }
}
