function generate_keys() {
  $.getJSON("/gen_keys", function(data) {
    $("#master_key").text(data.master_key);
    $("#public_key").text(data.public_key);
  });
}
