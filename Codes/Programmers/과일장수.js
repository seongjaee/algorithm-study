function solution(k, m, score) {
  let answer = 0;
  score.sort((a, b) => a - b);
  while (score.length >= m) {
    let minValue = k;
    for (let i = 0; i < m; i++) {
      minValue = Math.min(minValue, score.pop());
    }
    answer += minValue * m;
  }
  return answer;
}
