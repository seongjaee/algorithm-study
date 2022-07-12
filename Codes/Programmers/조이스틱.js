function solution(name) {
  // A로 만드는 비용
  const toMakeA = (char) =>
    Math.min(char.charCodeAt() - 65, 91 - char.charCodeAt());

  const n = name.length;
  const visited = Array(n).fill(false); // A 인가요?
  let aCount = 0;
  let minValue = Infinity;

  [...name].forEach((char, index) => {
    if (char === "A") {
      visited[index] = true;
      aCount++;
    }
  });

  function dfs(i, count, A) {
    if (A === n) {
      minValue = Math.min(minValue, count);
      return;
    }

    // 가지치기
    if (count >= minValue) return;

    // 오른쪽으로 가서 A 아닌 곳 찾기
    let j = i;
    while (true) {
      j++;
      const nj = (j + n) % n;
      if (!visited[nj]) {
        visited[nj] = true;
        dfs(nj, count + j - i + toMakeA(name[nj]), A + 1);
        visited[nj] = false;
        break;
      }
    }

    // 왼쪽으로 가서 A 아닌 곳 찾기
    j = i;
    while (true) {
      j--;
      const nj = (j + n) % n;
      if (!visited[nj]) {
        visited[nj] = true;
        dfs(nj, count + i - j + toMakeA(name[nj]), A + 1);
        visited[nj] = false;
        break;
      }
    }
  }

  if (name[0] === "A") {
    dfs(0, 0, aCount);
  } else {
    visited[0] = true;
    dfs(0, toMakeA(name[0]), aCount + 1);
  }

  return minValue;
}
