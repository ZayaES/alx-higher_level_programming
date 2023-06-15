#!/usr/bin/node

exports.converter = function (base) {
  return function conv (number) {
    return(number.toString(base));
    
  }
}
