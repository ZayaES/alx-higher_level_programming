#!/usr/bin/node

exports.converter = function (base) {
  return function conv(number) {
    let i = 0;
    let rem;
    const alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    const answerArray = [];

    while (number !== 0) {
      rem = number % base;
      if (rem > 9) {
        rem = alp[rem - 10];
      }
      number = Math.floor(number / base);
      answerArray[i] = rem;
      i++;
    }
    answerArray.reverse();
    answer = answerArray.join('');
    return answer;
  }
}
