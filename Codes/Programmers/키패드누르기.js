function solution(numbers, hand) {
  const getDist = (posA, posB) => {
    return Math.abs(posA[0] - posB[0]) + Math.abs(posA[1] - posB[1]);
  };

  const handPos = {
    left: [3, 0],
    right: [3, 2],
  };

  const result = numbers.map((num) => {
    if (num % 3 === 1) {
      handPos.left = [parseInt(num / 3), 0];
      return "L";
    } else if (num % 3 === 2 || num === 0) {
      const pos = num !== 0 ? [parseInt(num / 3), 1] : [3, 1];
      const D = getDist(pos, handPos.left) - getDist(pos, handPos.right);
      if (D > 0) {
        handPos.right = pos;
        return "R";
      } else if (D < 0) {
        handPos.left = pos;
        return "L";
      } else if (hand === "left") {
        handPos.left = pos;
        return "L";
      } else {
        handPos.right = pos;
        return "R";
      }
    } else {
      handPos.right = [parseInt(num / 3) - 1, 2];
      return "R";
    }
  });

  return result.join("");
}
