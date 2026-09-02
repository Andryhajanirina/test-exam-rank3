#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   py_echo_validator.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: andry-ha <andry-ha@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/09/02 11:32:09 by andry-ha            #+#    #+#            #
#   Updated: 2026/09/02 11:48:58 by andry-ha           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

# Write a function that checks if a string is a palindrome,
#   ignoring spaces and case.
def echo_validator(text: str) -> bool:
    clean_text = "".join([c.lower().strip() for c in text if c.isalpha])
    return clean_text == clean_text[::-1] if clean_text else False


if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))
    print(echo_validator("Was it a car or a cat I saw"))
    print(echo_validator("hello"))
    print(echo_validator("Madam Im Adam"))
    print(echo_validator(""))
