function check(place) {
  const visited = Array.from(Array(5), () => Array(5).fill(false));
  const delta = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  function visit_two(sy, sx) {
    let queue = [[sy, sx]];
    visited[sy][sx] = true;

    for (let i = 0; i < 2; i++) {
      const temp = [];
      while (queue.length > 0) {
        const [y, x] = queue.shift();
        for (let d of delta) {
          const ny = y + d[0];
          const nx = x + d[1];

          if (ny < 0 || ny >= 5 || nx < 0 || nx >= 5 || visited[ny][nx]) {
            continue;
          }
          if (place[ny][nx] === "X") {
            continue;
          }
          if (place[ny][nx] === "P") {
            return true;
          }
          visited[ny][nx] = true;
          temp.push([ny, nx]);
        }
      }
      queue = temp;
    }
    return false;
  }

  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (place[i][j] === "P" && !visited[i][j]) {
        if (visit_two(i, j)) {
          return 0;
        }
      }
    }
  }
  return 1;
}

function solution(places) {
  return places.map((place) => check(place));
}
