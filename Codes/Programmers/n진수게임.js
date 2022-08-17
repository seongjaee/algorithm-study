function convert(num, n) {
  let res = "";
  while (num > 0) {
    const r = num % n;
    if (r >= 10) {
      res += String.fromCharCode("A".charCodeAt() + r - 10);
    } else {
      res += `${r}`;
    }
    num = parseInt((num - r) / n);
  }
  return res.split("").reverse().join("");
}

function solution(n, t, m, p) {
  p--;
  let answer = "";
  let nowNum = 0;
  let nowIndex = 0;
  let convertedNum = "0";
  let turn = 0;

  while (answer.length < t) {
    if (turn === p) {
      answer += convertedNum[nowIndex];
    }

    turn = (turn + 1) % m;
    nowIndex++;

    if (nowIndex === convertedNum.length) {
      nowNum++;
      convertedNum = convert(nowNum, n);
      nowIndex = 0;
    }
  }

  return answer;
}
