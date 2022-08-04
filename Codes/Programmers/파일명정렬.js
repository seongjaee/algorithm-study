function isNumber(str) {
  const ord = str.charCodeAt();
  return ord >= 48 && ord <= 57;
}

function solution(files) {
  const divideFileName = (file) => {
    let head = "";
    let number = "";
    let startIndex = 0;
    for (let i = 0; i < file.length; i++) {
      if (isNumber(file[i])) {
        startIndex = i;
        break;
      }
      head += file[i];
    }

    for (let i = startIndex; i < file.length; i++) {
      if (!isNumber(file[i])) {
        break;
      }
      number += file[i];
    }
    return [head.toLowerCase(), parseInt(number)];
  };

  const compare = (file1, file2) => {
    let [head1, number1] = divideFileName(file1.file);
    let [head2, number2] = divideFileName(file2.file);

    if (head1 === head2 && number1 === number2) {
      return file1.idx - file2.idx;
    } else if (head1 === head2) {
      return number1 - number2;
    } else {
      return head1 > head2 ? 1 : -1;
    }
  };

  const filesWithIndex = files.map((file, idx) => ({ file, idx }));
  filesWithIndex.sort(compare);
  return filesWithIndex.map((fileIdx) => fileIdx.file);
}
