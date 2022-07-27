function solution(msg) {
  const answer = [];
  const d = {};
  for (let i = 1; i < 27; i++) {
    d[String.fromCharCode(i + 64)] = i;
  }

  let left,
    right = 0;
  const n = msg.length;
  let m = 26;

  while (right < n) {
    let now = msg.slice(left, right + 1);
    if (!(now in d)) {
      d[now] = ++m;
      answer.push(d[msg.slice(left, right)]);
      left = right;
    } else {
      right++;
    }
  }
  answer.push(d[msg.slice(left, right + 1)]);

  return answer;
}
