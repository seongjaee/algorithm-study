function Node(data) {
  this.data = data;
  this.next = null;
}
function Queue() {
  this.head = null;
  this.rear = null;
  this.length = 0;
  this.isEmpty = function () {
    return this.length === 0;
  };

  this.enqueue = function (data) {
    const newNode = new Node(data);
    if (this.isEmpty()) {
      this.head = newNode;
      this.rear = newNode;
    } else {
      this.rear.next = newNode;
      this.rear = newNode;
    }
    this.length++;
  };

  this.dequeue = function () {
    if (this.isEmpty()) {
      throw "Queue is empty";
    }
    this.length--;
    const result = this.head.data;
    this.head = this.head.next;
    return result;
  };
}

function solution(queue1, queue2) {
  let maxCount = (queue1.length + queue2.length) * 2;
  let leftSum = queue1.reduce((prev, curr) => prev + curr, 0);
  let rightSum = queue2.reduce((prev, curr) => prev + curr, 0);
  const leftQueue = new Queue();
  queue1.forEach((num) => leftQueue.enqueue(num));
  const rightQueue = new Queue();
  queue2.forEach((num) => rightQueue.enqueue(num));

  let cnt = 0;
  while (cnt < maxCount) {
    if (leftSum < rightSum) {
      const num = rightQueue.dequeue();
      leftQueue.enqueue(num);
      rightSum -= num;
      leftSum += num;
    } else if (leftSum > rightSum) {
      const num = leftQueue.dequeue();
      rightQueue.enqueue(num);
      leftSum -= num;
      rightSum += num;
    } else {
      break;
    }
    cnt++;
  }
  return cnt < maxCount ? cnt : -1;
}
