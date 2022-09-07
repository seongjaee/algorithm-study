Map.prototype.getDefault = function (key, value) {
  return this.has(key) ? this.get(key) : value;
};

function solution(gems) {
  const allCount = [...new Set(gems)].length;
  const counter = new Map();
  counter.set(gems[0], 1);

  let minLength = gems.length + 1;
  let answer = [];

  let left = 0;
  let right = 0;
  while (right < gems.length) {
    if (counter.size === allCount) {
      const leftCount = counter.get(gems[left]);
      if (leftCount === 1) {
        counter.delete(gems[left]);
      } else {
        counter.set(gems[left], leftCount - 1);
      }
      if (minLength > right - left + 1) {
        answer = [left + 1, right + 1];
        minLength = right - left + 1;
      }
      left++;
    } else {
      right++;
      if (right >= gems.length) {
        break;
      }
      counter.set(gems[right], counter.getDefault(gems[right], 0) + 1);
    }
  }

  return answer;
}
