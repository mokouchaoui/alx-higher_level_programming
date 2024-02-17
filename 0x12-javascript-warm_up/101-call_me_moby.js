#!/usr/bin/node
exports.callMeMoby = function (n, fun) {
  while (n-- > 0) {
    fun();
  }
};
