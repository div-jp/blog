#! /bin/sh


IndexList(){

#サーバにあるようなindex.htmlをインデックス一覧を表示するやつと同じ機能の関数。
#ディレクトリ以下全てをインデックスとしてリスト表示。
#実行し出力されたind.htmlをFirefoxなどのブラウザにD&Dする。
#上げるときは必ずUTF-8でアップロードすること。


#頭出し機能あり。
#頭出ししたい場合は、ファイル名の拡張子の直前に半角で「tm=30」とつければおｋ。
#この場合は動画の30秒から再生が始まる。書式はvideoタグの仕様と同じ。



	local mydir="./"

cat << EOF
<html lang="ja">
<head>
<title>テスト</title>
<meta NAME="ROBOTS" CONTENT="NOINDEX,NOFOLLOW,NOARCHIVE">
<meta charset="UTF-8">
<style type="text/css">
<!--
body {
  background-color: #222;
}
dl,
dt,
dd {
  box-sizing: border-box;
}
dl {
  background: #eee;
  border-right: 1px solid #ccc;
  border-bottom: 1px solid #ccc;
  border-left: 1px solid #ccc;
  width :90%;
  margin :20px auto 0 auto;
}
dt,
dd {
  padding: 5px 10px 0 10px;
  border-top: 1px solid #ccc;
}
dt {
  width: 40%;
  float: left;
  font-size:80%;
}
dd {
  background: #fff;
  margin-left: 40%;
  padding-bottom: 5px;
  border-left: 1px solid #ccc;
  font-size:80%;
}
dd:after {
  content: '';
  display: block;
  clear: both;
}
-->
</style>
<script type="text/javascript">
	function preview(path1){
		let a = document.getElementById('videopreview')
		let b = a.getElementsByTagName('source');
		b[0].src = path1;
		a.load();
	}
</script>
</head>
<body>
<video id="videopreview" width="100%" height="100%" autoplay loop controls>
	<source src="" type='video/mp4'>
</video>
<dl>
EOF

find ${mydir} -type f              |
LC_ALL=C sort                      |
awk 'BEGIN {FS="/";OFS="/";}
{
	Line = $0;
	FileName = $NF;

	$NF = "";

	print Line"\t"$0"\t"FileName

}'                                 |
awk 'BEGIN {FS="\t";OFS="\t";}
{
  #拡張子と時間の処理
  Extension = substr($3, index($3, "."), (length($3)));
  Time = substr($3, index($3, "tm="), index($3, "."));
  if (Time ~ /tm=/){
    gsub(Extension , "", Time);
    gsub("tm", "#t", Time);
  }else{
    Time = "";
  }

	print $0,Extension,Time

}'                                 |
awk 'BEGIN {FS="\t";}
{
  #html出力
  if( $4 ~ /\.mp4/ ){
    print "<dt>"$2"</dt><dd><a href=\"#videopreview\" onClick=\"preview(\047"$1$5"\047)\">"$3"</a></dd>"
  }else{
    print "<dt>"$2"</dt><dd><a href=\""$1"\">"$3"</a></dd>"
  }
}'

cat << EOF
</dl>
</body>
</html>
EOF

}



if [ -t 0 ]; then
  IndexList >ind.html
else
  printf "Content-type: text/html\n\n"
  IndexList
fi



