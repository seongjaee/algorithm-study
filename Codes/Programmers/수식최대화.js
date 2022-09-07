function parseExpression(expression) {
  let nowNumber = "";
  const formula = [];
  for (let char of expression) {
    const charCode = char.charCodeAt();
    if ("0".charCodeAt() <= charCode && charCode <= "9".charCodeAt()) {
      nowNumber += char;
    } else {
      formula.push(parseInt(nowNumber));
      formula.push(char);
      nowNumber = "";
    }
  }
  formula.push(parseInt(nowNumber));
  return formula;
}

function operate(num1, num2, operator) {
  if (operator === "+") {
    return num1 + num2;
  } else if (operator === "-") {
    return num1 - num2;
  } else {
    return num1 * num2;
  }
}

function calculate(formula, priority) {
  let now = [...formula];
  for (let operator of priority) {
    let i = 0;
    let temp = [];
    while (i < now.length) {
      if (now[i] === operator) {
        temp.push(operate(temp.pop(), now[i + 1], operator));
        i++;
      } else {
        temp.push(now[i]);
      }
      i++;
    }
    now = temp;
  }
  return Math.abs(now[0]);
}

function solution(expression) {
  let answer = 0;
  const formula = parseExpression(expression);
  const priorityList = ["+*-", "+-*", "-*+", "-+*", "*-+", "*+-"];
  priorityList.forEach((priority) => {
    answer = Math.max(calculate(formula, priority), answer);
  });

  return answer;
}
