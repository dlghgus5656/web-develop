function openclose() {
  let status = $("#posting-box").css("display");
  if (status == "block") {
    $("#posting-box").hide();
    $("#btn-posting-box").text("포스팅박스 열기");
  } else {
    $("#posting-box").show();
    $("#btn-posting-box").text("포스팅박스 닫기");
  }
}
