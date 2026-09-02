#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_hidenp.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 11:58:11 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 12:02:03 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def hidenp(small: str, big: str) -> bool:
    it = iter(big)
    return all(c in it for c in small)


if __name__ == "__main__":
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing", "subsequence testing"))
