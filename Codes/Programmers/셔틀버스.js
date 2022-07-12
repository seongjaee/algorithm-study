// 최소 힙 구현
class Heap {
  constructor() {
    this.heap = [];
  }

  // 추가, 맨 끝에 삽입하고 자리 찾기
  add(data) {
    let i = this.heap.length;
    this.heap.push(data);

    while (i > 0) {
      const parent = Math.floor((i - 1) / 2);

      // 부모보다 크면 종료, 작으면 스왑
      if (this.heap[parent] <= this.heap[i]) {
        break;
      } else {
        const temp = this.heap[parent];
        this.heap[parent] = this.heap[i];
        this.heap[i] = temp;
        i = parent;
      }
    }
  }

  // 삭제, 루트를 반환, 루트 자리에 맨 끝 요소를 넣고 자리 찾기
  pop() {
    if (this.heap.length === 0) {
      throw "Pop from empty heap";
    }
    const root = this.heap[0];
    this.heap[0] = this.heap[this.heap.length - 1]; // 맨 끝 요소를 루트에 넣고
    this.heap.pop();

    let i = 0;
    const last = this.heap.length - 1;
    while (i < last) {
      let child = 2 * i + 1; // 왼쪽 자식

      // 오른쪽 자식이 더 작으면 오른쪽 사용
      if (child < last && this.heap[child] > this.heap[child + 1]) {
        child++;
      }
      // 자식보다 작아졌으면 종료
      if (child > last || this.heap[i] <= this.heap[child]) {
        break;
      }
      // 자식보다 크니까 스왑
      const temp = this.heap[i];
      this.heap[i] = this.heap[child];
      this.heap[child] = temp;
      i = child;
    }
    return root;
  }

  peek() {
    return this.heap[0];
  }
}
function time2Int(time) {
  const [h, m] = time.split(":");
  return +h * 60 + +m;
}

function int2Time(num) {
  const m = num % 60;
  const h = (num - m) / 60;
  const hh = ("" + h).padStart(2, "0");
  const mm = ("" + m).padStart(2, "0");
  return `${hh}:${mm}`;
}

function solution(n, t, m, timetable) {
  var answer = "";
  const timeHeap = new Heap();
  timetable.forEach((time) => timeHeap.add(time2Int(time)));

  let nowTime = time2Int("09:00");
  let bus = [];
  for (let i = 0; i < n; i++) {
    bus = [];
    while (true) {
      if (timeHeap.peek() <= nowTime) {
        // 맨 앞사람이 탈 수 있으면 태우자
        bus.push(timeHeap.pop());
      } else {
        break;
      }
      if (bus.length === m) {
        // 만차면 끝
        break;
      }
    }
    nowTime += t;
  }

  if (bus.length === m) {
    answer = int2Time(bus[m - 1] - 1); // 막차가 꽉찼으면 막차 마지막 사람보다 1분 일찍
  } else {
    answer = int2Time(nowTime - t); // 막차가 꽉차지 않았으면 막차 도착 시간
  }

  return answer;
}
