// script.jsの設定を一部書き換え
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);

// 画像転送 & 推定の実行
function submitAct(){
    $.ajax({
        url:'/api/image',
        type:'POST',
        data:{
            'img':canvas.toDataURL()
        }
    })
    // Ajaxリクエストが成功した時発動
    .done( (data) => {
        console.log('access success');
        document.getElementById("result_text").innerHTML = data;
    })
    // Ajaxリクエストが失敗した時発動
    .fail( (data) => {
        console.log('access failed');
    })
    // Ajaxリクエストが成功・失敗どちらでも発動
    .always( (data) => {
        console.log(data);
    });
}

function clearResult(){
    document.getElementById("result_text").innerHTML = '識別中...'
}