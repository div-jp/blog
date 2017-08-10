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

<header>
<p><a href="https://div-jp.github.io/blog/">index</a></p>
</header>

EOS

pandoc +RTS -V0 -RTS index.md -f markdown_phpextra -t html5 >>./index.html

cat << "EOS" >> ./index.html

<footer>
<p><a href="https://div-jp.github.io/blog/">index</a></p>
</footer>

</body>
</html>
EOS
















