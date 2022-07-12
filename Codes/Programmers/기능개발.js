function solution(progresses, speeds) {
  const remainTime = progresses.map((p, idx) =>
    Math.ceil((100 - p) / speeds[idx])
  );

  var answer = [];
  let now = 0;
  remainTime.forEach((time) => {
    if (time > now) {
      answer.push(1);
      now = time;
    } else {
      answer[answer.length - 1]++;
    }
  });
  return answer;
}
