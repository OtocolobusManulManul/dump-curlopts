# dump-curlopts
script that dumps the integer optcodes for each curl_easy_setopt option

curl.h does not provide exact consnant values for each curlopt code, so this script parses the file and autogenerates constant definitions. I could only see this being useful to anyone else trying to reverse a libcurl network stack.

also contains the preexisting dumpfile I generated
