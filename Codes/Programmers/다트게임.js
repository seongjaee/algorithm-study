function solution(dartResult) {
  const isNumber = (num) => (48 <= num.charCodeAt()) & (num.charCodeAt() <= 57);

  const f = {
    S: () => {},
    D: () => {
      score[score.length - 1] **= 2;
    },
    T: () => {
      score[score.length - 1] **= 3;
    },
    "*": () => {
      score[score.length - 1] *= 2;
      if (score.length > 1) {
        score[score.length - 2] *= 2;
      }
    },
    "#": () => {
      score[score.length - 1] *= -1;
    },
  };

  const score = [];
  let number = "";
  for (char of dartResult) {
    if (isNumber(char)) {
      number += char;
      continue;
    }
    if (number.length) {
      score.push(+number);
      number = "";
    }
    f[char]();
  }
  return score.reduce((a, b) => a + b);
}
