$(document).ready(function () {
  $("#cards-box").empty();
  listing();
});

function listing() {
  $.ajax({
    type: "GET",
    url: "http://spartacodingclub.shop/post",
    data: {},
    success: function (response) {
      let rows = response["articles"];
      for (let i = 0; i < rows.length; i++) {
        let comment = rows[i]["comment"];
        let desc = rows[i]["desc"];
        let image = rows[i]["image"];
        let title = rows[i]["title"];
        let url = rows[i]["url"];

        let temp_html = `<div class="card">
        <img
          class="card-img-top"
          src=${image}
          alt="Card image cap"
        />
        <div class="card-body">
          <a href=${url} class="card-title"
            >${title}</a
          >
          <p class="card-text">
            ${desc}
          </p>
          <p class="card-coment">${comment}</p>
        </div>`;
        $("#cards-box").append(temp_html);
      }
    },
  });
}

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
