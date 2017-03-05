#! /bin/sh

cat << "EOS" > ./index.html
<!DOCTYPE html>
<html lang="ja">
<head>
<meta content="text/html; charset=UTF-8" http-equiv="content-type">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="mystyle.css">
</head>
<body>
EOS

pandoc +RTS -V0 -RTS index.md -f markdown_phpextra -t html5 >>./index.html

cat << "EOS" >> ./index.html

</body>
</html>
EOS
















